"""
CHD Burden Model

Population model estimating congenital heart disease mortality
and disability-adjusted life years under disruption of pediatric
cardiac care.

Outputs:
- baseline model results
- sensitivity analysis
- Monte Carlo uncertainty analysis
- results written to /results directory
"""

import os
import random

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
# RESULTS DIRECTORY
# --------------------------------------------------

os.makedirs("results", exist_ok=True)

# --------------------------------------------------
# BASELINE MODEL
# --------------------------------------------------

births_per_year = population * birth_rate

total_births = births_per_year * study_years

chd_cases = total_births * chd_prevalence

excess_deaths = chd_cases * (untreated_mortality - treated_mortality)

years_lost = life_expectancy - mean_age_death

yll = excess_deaths * years_lost

survivors = chd_cases - excess_deaths

yld = survivors * disability_weight * study_years

dalys = yll + yld

# --------------------------------------------------
# PRINT RESULTS
# --------------------------------------------------

print("\nMODEL RESULTS\n")

print(f"Equation 1 (Births per year): {round(births_per_year)}")
print(f"Equation 2 (Total births): {round(total_births)}")
print(f"Equation 3 (CHD cases): {round(chd_cases)}")
print(f"Equation 4 (Excess deaths): {round(excess_deaths)}")
print(f"Equation 5 (Years of Life Lost): {round(yll)}")
print(f"Equation 6 (Years Lived with Disability): {round(yld)}")
print(f"Equation 7 (DALYs): {round(dalys)}")

# --------------------------------------------------
# WRITE BASELINE RESULTS
# --------------------------------------------------

with open("results/baseline_results.txt","w") as f:

    f.write("Baseline Model Results\n\n")

    f.write(f"Births per year: {round(births_per_year)}\n")
    f.write(f"Total births: {round(total_births)}\n")
    f.write(f"CHD cases: {round(chd_cases)}\n")
    f.write(f"Excess deaths: {round(excess_deaths)}\n")
    f.write(f"YLL: {round(yll)}\n")
    f.write(f"YLD: {round(yld)}\n")
    f.write(f"DALYs: {round(dalys)}\n")

# --------------------------------------------------
# MONTE CARLO UNCERTAINTY ANALYSIS
# --------------------------------------------------

print("\nMONTE CARLO UNCERTAINTY ANALYSIS\n")

runs = 10000

dalys_results = []

for i in range(runs):

    mortality = random.uniform(0.20,0.35)

    excess = chd_cases * (mortality - treated_mortality)

    yll_u = excess * years_lost

    survivors_u = chd_cases - excess

    yld_u = survivors_u * disability_weight * study_years

    daly_u = yll_u + yld_u

    dalys_results.append(daly_u)

dalys_results.sort()

lower = dalys_results[int(0.025 * runs)]
upper = dalys_results[int(0.975 * runs)]
median = dalys_results[int(0.50 * runs)]

print(f"Median DALYs: {round(median)}")
print(f"95% uncertainty interval: {round(lower)} - {round(upper)}")

# --------------------------------------------------
# WRITE MONTE CARLO RESULTS
# --------------------------------------------------

with open("results/monte_carlo_summary.txt","w") as f:

    f.write("Monte Carlo Uncertainty Analysis\n\n")

    f.write(f"Runs: {runs}\n\n")

    f.write(f"Median DALYs: {round(median)}\n")
    f.write(f"Lower 95% interval: {round(lower)}\n")
    f.write(f"Upper 95% interval: {round(upper)}\n")

print("\nResults written to /results directory\n")
