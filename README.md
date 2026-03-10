# Congenital Heart Disease Burden Model

Reproducible Python model estimating excess congenital heart disease mortality and disability adjusted life years associated with disruption of pediatric cardiac care.

---

## Overview

Congenital heart disease (CHD) is the most common congenital anomaly worldwide, affecting approximately 9–10 per 1000 live births. Advances in pediatric cardiac surgery have significantly improved survival outcomes in settings where specialized care is available.

In situations where health systems are disrupted, access to surgical and catheter based interventions may be limited. Under these conditions, congenital heart disease can lead to substantial preventable mortality and long term disability.

This repository contains a transparent and reproducible population model used to estimate congenital heart disease burden associated with disruption of pediatric cardiac care.

---

## Model Structure

The model estimates disease burden using a deterministic population framework consisting of the following steps.

1. Estimate births during the study period  
2. Estimate congenital heart disease incidence  
3. Estimate excess mortality associated with treatment disruption  
4. Calculate Years of Life Lost (YLL)  
5. Calculate Years Lived with Disability (YLD)  
6. Compute total Disability Adjusted Life Years (DALYs)

Sensitivity analysis is included to explore uncertainty in untreated mortality assumptions.

---

## Equations

Births per year

```
births_per_year = population * crude_birth_rate
```

Total births during study period

```
total_births = births_per_year * study_years
```

Congenital heart disease cases

```
chd_cases = total_births * prevalence
```

Excess mortality

```
excess_deaths = chd_cases * (untreated_mortality - treated_mortality)
```

Years of Life Lost

```
YLL = deaths * (life_expectancy - mean_age_death)
```

Years Lived With Disability

```
YLD = survivors * disability_weight * study_years
```

Total disease burden

```
DALYs = YLL + YLD
```

---

## Sensitivity Analysis

Untreated mortality varies depending on lesion severity and access to supportive care.

To account for this uncertainty, the model evaluates multiple untreated mortality scenarios.

Scenarios evaluated

```
0.20 untreated mortality
0.25 untreated mortality
0.30 untreated mortality
0.35 untreated mortality
```

Each scenario recalculates excess mortality, Years of Life Lost, Years Lived with Disability, and total DALYs.

---

## Repository Structure

```
.
├── chd_burden_model.py
├── README.md
└── LICENSE
```

**chd_burden_model.py**  
Python script implementing the congenital heart disease burden model and sensitivity analysis.

---

## Running the Model

### Requirements

Python 3.8 or newer.

### Run the script

```
python chd_burden_model.py
```

The script prints results directly to the terminal in a clean format suitable for manuscript reporting.

---

## Example Output

```
Births per year: 60900
Total births (study period): 152250

CHD cases: 1522

Excess deaths: 320

Years of Life Lost (YLL): 23296
Years Lived with Disability (YLD): 247

Total DALYs: 23543
```

Sensitivity analysis results appear below the baseline model output.

---

## Methodology

The model follows the Global Burden of Disease framework for calculating disability adjusted life years.

DALYs are defined as

```
DALYs = Years of Life Lost (YLL) + Years Lived with Disability (YLD)
```

YLL represents premature mortality relative to life expectancy.

YLD represents non fatal health loss weighted by disability severity.

Model parameters are derived from published epidemiological literature and demographic estimates.

---

## Reproducibility

The script contains all equations used in the analysis. All parameters and assumptions are explicitly defined in the code to allow transparent reproduction and modification.

---

## Citation

If you use this model in research or analysis, please cite:

Boyd A. Congenital Heart Disease Burden Model. GitHub repository.

---

## License

This project is licensed under the MIT License.
