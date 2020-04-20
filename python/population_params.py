import numpy as np

population = {}
# Total population
population["N"] = 10666108;
# Age groups
population["ageran"] = np.arange(5, 96, 10)
# Age population fractions
population["agefrac"] = np.array([0.126, 0.137, 0.139, 0.132, 0.130, 0.129, 0.104, 0.061, 0.036, 0.007]);
# Must sum to 1
population["agefrac"] = population["agefrac"]/sum(population["agefrac"])
population["meanage"] = sum(population["ageran"] * population["agefrac"])
# Number of age fractions
population["nran"] = len(population["ageran"])

# Fraction of hospitalized individuals per age group
population["hosp_frac"] = np.array([0.1, 0.3, 1.2, 3.2, 4.9, 10.2, 16.6, 24.3, 27.3, 27.3])/100

# Fraction of ICU needed given hospitalization
population["hosp_crit"] = np.array([5, 5, 5, 5, 6.3, 12.2, 27.4, 43.2, 70.9, 70.9])/100

# Fraction of deaths given ICU
population["crit_die"] = 0.5 * np.ones(population["nran"]);

# Fraction of asymptomatic per group
population["p"] = np.array([0.95, 0.95, 0.90, 0.8, 0.7, 0.6, 0.4, 0.2, 0.2, 0.2])
population["overall_p"] = sum(population["p"] * population["agefrac"])

# Set up indexes for each group
population["S_ids"] = np.arange(0, population["nran"])
population["E_ids"] = np.arange(population["nran"], 2*population["nran"])
population["Ia_ids"] = np.arange(2*population["nran"], 3*population["nran"])
population["Is_ids"] = np.arange(3*population["nran"], 4*population["nran"])
population["Ihsub_ids"] = np.arange(4*population["nran"], 5*population["nran"])
population["Ihcri_ids"] = np.arange(5*population["nran"], 6*population["nran"])
population["R_ids"] = np.arange(6*population["nran"], 7*population["nran"])
population["D_ids"] = np.arange(7*population["nran"], 8*population["nran"])
population["Hcum_ids"] = np.arange(8*population["nran"], 9*population["nran"])
