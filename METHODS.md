# Methods

This document describes the methodology implemented in the congenital heart disease burden model.

## Study Design

A deterministic population model was developed to estimate congenital heart disease burden attributable to disruption of pediatric cardiac care.

The model estimates excess mortality and disability adjusted life years during the study period.

## Population Estimates

Annual births are estimated using

```
births_per_year = population * birth_rate
```

Total births during the study period are

```
total_births = births_per_year * study_years
```

## Congenital Heart Disease Incidence

Congenital heart disease cases are estimated using birth prevalence.

```
chd_cases = total_births * prevalence
```

## Treatment Disruption

Excess mortality associated with disruption of treatment access is estimated using

```
excess_deaths = chd_cases * (untreated_mortality - treated_mortality)
```

## Years of Life Lost

Years of Life Lost are calculated as

```
YLL = deaths * (life_expectancy - mean_age_death)
```

## Years Lived With Disability

Surviving cases contribute to disability burden

```
YLD = survivors * disability_weight * study_years
```

## Total Burden

Total burden is calculated as

```
DALYs = YLL + YLD
```

## Sensitivity Analysis

Sensitivity analysis evaluates different untreated mortality scenarios to account for uncertainty in clinical outcomes.
