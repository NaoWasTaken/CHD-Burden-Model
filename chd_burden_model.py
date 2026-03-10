"""
CHD BURDEN MODEL
Gaza Health System Disruption Study

Purpose
-------
Estimate congenital heart disease burden attributable to disruption of
paediatric cardiac care during the Gaza conflict period.

Outputs
-------
Clean terminal results formatted for manuscript extraction.

Author: Aviel Boyd
"""


# --------------------------------------------------
# PARAMETERS
# --------------------------------------------------

population = 2100000

birth_rate = 29 / 1000

study_years = 2.5

chd_prevalence = 10 / 1000

untreated_mortality = 0.27
treated_mortality = 0.06

life_expectancy = 74.3
mean_age_death = 1.5

disability_weight = 0.081


# --------------------------------------------------
# EQUATION 1
# births_per_year = population * birth_rate
# --------------------------------------------------

births_per_year = population * birth_rate


# --------------------------------------------------
# EQUATION 2
# total_births = births_per_year * study_years
# --------------------------------------------------

total_births = births_per_year * study_years


# --------------------------------------------------
# EQUATION 3
# chd_cases = total_births * chd_prevalence
# --------------------------------------------------

chd_cases = total_births * chd_prevalence


# --------------------------------------------------
# EQUATION 4
# excess_deaths = chd_cases * (untreated_mortality - treated_mortality)
# --------------------------------------------------

excess_deaths = chd_cases * (untreated_mortality - treated_mortality)


# --------------------------------------------------
# EQUATION 5
# years_lost = life_expectancy - mean_age_death
# --------------------------------------------------

years_lost = life_expectancy - mean_age_death


# --------------------------------------------------
# EQUATION 6
# YLL = excess_deaths * years_lost
# --------------------------------------------------

yll = excess_deaths * years_lost


# --------------------------------------------------
# EQUATION 7
# survivors = chd_cases - excess_deaths
# --------------------------------------------------

survivors = chd_cases - excess_deaths


# --------------------------------------------------
# EQUATION 8
# YLD = survivors * disability_weight * study_years
# --------------------------------------------------

yld = survivors * disability_weight * study_years


# --------------------------------------------------
# EQUATION 9
# DALYs = YLL + YLD
# --------------------------------------------------

dalys = yll + yld


# --------------------------------------------------
# BASELINE OUTPUT
# --------------------------------------------------

print("\n--- BASE MODEL RESULTS ---\n")

print(f"Births per year: {round(births_per_year)}")

print(f"Total births (study period): {round(total_births)}")

print(f"CHD cases: {round(chd_cases)}")

print(f"Excess deaths: {round(excess_deaths)}")

print(f"Years of Life Lost (YLL): {round(yll)}")

print(f"Years Lived with Disability (YLD): {round(yld)}")

print(f"Total DALYs: {round(dalys)}")

print("\n--------------------------\n")


# --------------------------------------------------
# SENSITIVITY ANALYSIS
# --------------------------------------------------

print("\n--- SENSITIVITY ANALYSIS ---\n")

mortality_scenarios = [0.20, 0.25, 0.30, 0.35]

for mortality in mortality_scenarios:

    excess = chd_cases * (mortality - treated_mortality)

    yll_s = excess * years_lost

    survivors_s = chd_cases - excess

    yld_s = survivors_s * disability_weight * study_years

    dalys_s = yll_s + yld_s

    print(f"Untreated mortality {mortality:.2f} -> DALYs: {round(dalys_s)}")

print("\n-----------------------------\n")


"""
--------------------------------------------------
METHODOLOGY
--------------------------------------------------

Study Design
------------
This script implements a deterministic population model estimating
the burden of congenital heart disease attributable to disruption
of paediatric cardiac care during the Gaza conflict period.

Two components of burden are represented:

1. Birth cohort cases occurring during the study period
2. Excess mortality attributable to loss of surgical treatment access

Population and Birth Estimates
------------------------------
Annual births are estimated using:

births_per_year = population * crude_birth_rate

Total births over the study period are:

total_births = births_per_year * study_years

Congenital Heart Disease Incidence
----------------------------------
Birth prevalence of congenital heart disease is assumed to be:

10 per 1000 live births

Estimated CHD cases are therefore:

chd_cases = total_births * prevalence

Treatment Disruption
--------------------
Under normal conditions a large proportion of CHD cases would
receive surgical or catheter-based intervention.

Conflict conditions may prevent access to these services.

Excess mortality is therefore modeled as:

excess_deaths = cases * (untreated_mortality - treated_mortality)

Years of Life Lost
------------------
YLL is calculated as:

YLL = deaths * (life_expectancy - mean_age_death)

Years Lived With Disability
---------------------------
Surviving CHD patients may experience chronic disability.

YLD is calculated as:

YLD = survivors * disability_weight * study_years

Disability weights follow Global Burden of Disease methodology.

Total Burden
------------
Total DALYs are calculated as:

DALYs = YLL + YLD

Sensitivity Analysis
--------------------
Because untreated mortality varies between lesion types and
clinical settings, sensitivity analysis is performed by varying
the untreated mortality parameter across plausible ranges.

Scenarios evaluated:

0.20 untreated mortality
0.25 untreated mortality
0.30 untreated mortality
0.35 untreated mortality

Each scenario recalculates excess mortality, YLL, YLD,
and total DALYs.

Purpose
-------
The model provides a transparent and reproducible estimate
of the burden attributable to disruption of paediatric cardiac care.

All parameters can be modified to test alternative assumptions.
"""
