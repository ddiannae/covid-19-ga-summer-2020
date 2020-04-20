pars = {}

#From exposed to infectious. 1/gamma_e = mean exposed period
pars["gamma_e"] = 1/4

#From asymptomatic to recovered. Resolution rate for asymptomatic. 1/gamma_a = mean asymptomatic period
pars["gamma_a"] = 1/6

#From symptomatic to recovered. Resolution rate for symptomatic. 1/gamma_s = mean symptomatic period
pars["gamma_s"] = 1/6

#From subacute to recovered. 1/gamma_h = mean hospital period
pars["gamma_h"] = 1/10

#From susceptible to asymptomatic exposed. beta_a = transmission for asymptomatic
pars["beta_a"] = 4/10

#From susceptible to symptomatic exposed. beta_s = transmission for symptomatic
pars["beta_s"] = 8/10

# Transmission for asymptomatic / Resolution rate for asymptomatic
pars["Ra"] = pars["beta_a"]/pars["gamma_a"]

# Transmission for symptomatic / Resolution rate for symptomatic
pars["Rs"] = pars["beta_s"]/pars["gamma_s"]

# Trigger at 5000 total cases, irrespective of type
pars["Itrigger"] = 500000
