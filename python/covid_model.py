import numpy as np

def SEIRplus(t, y, epi_pars, population_pars):

    dydt = np.zeros(len(y))

    # Total asymptomatic
    Ia = sum(y[population_pars["Ia_ids"]])

    # Total symptomatic
    Is = sum(y[population_pars["Is_ids"]])

    # Total recovered
    R = sum(y[population_pars["R_ids"]])

    # Total susceptible
    S = sum(y[population_pars["S_ids"]])

    # Total exposed
    E = sum(y[population_pars["E_ids"]])

    # Dynamics -  Base Model

    # Susceptible
    dydt[population_pars["S_ids"]] = -epi_pars["beta_a"] * y[population_pars["S_ids"]] * Ia - \
                            epi_pars["beta_s"] * y[population_pars["S_ids"]] * Is

    # Exposed
    dydt[population_pars["E_ids"]] = epi_pars["beta_a"] * y[population_pars["S_ids"]] * Ia + \
                            epi_pars["beta_s"] * y[population_pars["S_ids"]] * Is - epi_pars["gamma_e"] * y[population_pars["E_ids"]]

    # Infectious asymptomatically
    dydt[population_pars["Ia_ids"]] = np.transpose(population_pars["p"]) * epi_pars["gamma_e"] * y[population_pars["E_ids"]] - \
                            epi_pars["gamma_a"] * y[population_pars["Ia_ids"]]

    # Infectious symptomatically
    dydt[population_pars["Is_ids"]] = np.transpose(np.ones(len(population_pars["p"])) - population_pars["p"]) * epi_pars["gamma_e"] * \
                            y[population_pars["E_ids"]] - epi_pars["gamma_s"] * y[population_pars["Is_ids"]]

    # Symptomatic cases requiring hospital care (subacute)
    dydt[population_pars["Ihsub_ids"]]= np.transpose(population_pars["hosp_frac"]) * (1 - np.transpose(population_pars["hosp_crit"])) * \
                            epi_pars["gamma_s"] * y[population_pars["Is_ids"]] - epi_pars["gamma_h"] * y[population_pars["Ihsub_ids"]]

    # Symptomatic cases requiring ICU intervention (acute/critical)
    dydt[population_pars["Ihcri_ids"]]= np.transpose(population_pars["hosp_frac"]) * np.transpose(population_pars["hosp_crit"]) * \
                            epi_pars["gamma_s"] * y[population_pars["Is_ids"]] - epi_pars["gamma_h"] * y[population_pars["Ihcri_ids"]]

    # Recovered
    dydt[population_pars["R_ids"]]= epi_pars["gamma_a"] * y[population_pars["Ia_ids"]] + \
                            epi_pars["gamma_s"] * y[population_pars["Is_ids"]] * (1 - np.transpose(population_pars["hosp_frac"])) + \
                            epi_pars["gamma_h"] * y[population_pars["Ihsub_ids"]] + \
                            epi_pars["gamma_h"] * y[population_pars["Ihcri_ids"]] * (1 - np.transpose(population_pars["crit_die"]))

    # Deaths
    dydt[population_pars["D_ids"]] = epi_pars["gamma_h"] * y[population_pars["Ihcri_ids"]] * np.transpose(population_pars["crit_die"])

    # HFR. Hospitalization fatality risk. Infectious and hospitalized
    dydt[population_pars["Hcum_ids"]]= np.transpose(population_pars["hosp_frac"]) * (1 - np.transpose(population_pars["hosp_crit"])) * \
                            epi_pars["gamma_s"] * y[population_pars["Is_ids"]] + np.transpose(population_pars["hosp_frac"]) * \
                            np.transpose(population_pars["hosp_crit"]) * epi_pars["gamma_s"] * y[population_pars["Is_ids"]]
    # Is it the same as?
    #dydt[population_pars["Hcum_ids"]]= np.transpose(population_pars["hosp_frac"]) * epi_pars["gamma_s"] * y[population_pars["Is_ids"]]

    return dydt
