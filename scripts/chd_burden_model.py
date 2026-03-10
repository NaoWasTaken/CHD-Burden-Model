"""
Congenital Heart Disease Burden Model

Deterministic population model estimating excess congenital heart disease
mortality and disability adjusted life years associated with disruption
of pediatric cardiac care.

Structure

1. Parameter definitions
2. Baseline deterministic model
3. Terminal output
4. Results file export
5. Probabilistic uncertainty simulation
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
# BASELINE MODEL CALCULATIONS
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
# TERMINAL OUTPUT
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
# WRITE BASELINE RESULTS FILE
# --------------------------------------------------

with open("results/baseline_results.txt", "w") as f:

    f.write("Baseline Model Results\n\n")

    f.write(f"Births per year: {round(births_per_year)}\n")
    f.write(f"Total births: {round(total_births)}\n")
    f.write(f"CHD cases: {round(chd_cases)}\n")
    f.write(f"Excess deaths: {round(excess_deaths)}\n")
    f.write(f"Years of Life Lost (YLL): {round(yll)}\n")
    f.write(f"Years Lived with Disability (YLD): {round(yld)}\n")
    f.write(f"Total DALYs: {round(dalys)}\n")


# --------------------------------------------------
# PROBABILISTIC UNCERTAINTY SIMULATION
# --------------------------------------------------

print("\nUNCERTAINTY SIMULATION\n")

runs = 10000

dalys_results = []

for i in range(runs):

    # sample untreated mortality from normal distribution
    mortality = random.normalvariate(0.27, 0.04)

    # constrain to valid probability range
    mortality = max(0, min(1, mortality))

    excess = chd_cases * (mortality - treated_mortality)

    yll_u = excess * years_lost

    survivors_u = chd_cases - excess

    yld_u = survivors_u * disability_weight * study_years

    daly_u = yll_u + yld_u

    dalys_results.append(daly_u)


dalys_results.sort()

lower = dalys_results[int(0.025 * runs)]
median = dalys_results[int(0.50 * runs)]
upper = dalys_results[int(0.975 * runs)]


print(f"Median DALYs: {round(median)}")
print(f"95% uncertainty interval: {round(lower)} - {round(upper)}")


# --------------------------------------------------
# WRITE UNCERTAINTY RESULTS
# --------------------------------------------------

with open("results/uncertainty_summary.txt", "w") as f:

    f.write("Uncertainty Simulation Results\n\n")

    f.write(f"Simulation runs: {runs}\n\n")

    f.write(f"Median DALYs: {round(median)}\n")
    f.write(f"Lower 95 percent interval: {round(lower)}\n")
    f.write(f"Upper 95 percent interval: {round(upper)}\n")


print("\nResults written to /results directory\n")
