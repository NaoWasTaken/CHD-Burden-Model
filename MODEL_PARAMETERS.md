# Model Parameters

This document describes the parameters used in the congenital heart disease burden model.

All parameters are defined directly in `chd_burden_model.py` and documented here for transparency and reproducibility.

---

# Population Parameters

Population

```
2100000
```

Estimated population of the Gaza Strip during the study period.

Birth rate

```
29 / 1000
```

Crude birth rate used to estimate annual births.

Study period

```
2.5 years
```

Duration of the conflict period analyzed in the model.

---

# Disease Parameters

Congenital heart disease prevalence

```
10 / 1000 births
```

Estimated global birth prevalence of congenital heart disease.

This value is consistent with published epidemiological estimates.

---

# Treatment Parameters

Untreated mortality

```
0.27
```

Estimated mortality among congenital heart disease patients without access to surgical treatment.

Treated mortality

```
0.06
```

Estimated mortality among patients receiving surgical or catheter based intervention.

Excess mortality is calculated as:

```
excess_deaths = chd_cases * (untreated_mortality - treated_mortality)
```

---

# Life Expectancy

Life expectancy

```
74.3 years
```

Average life expectancy used to calculate years of life lost.

Mean age at death

```
1.5 years
```

Approximate mean age of mortality among untreated congenital heart disease cases.

Years of Life Lost calculation

```
YLL = deaths * (life_expectancy - mean_age_death)
```

---

# Disability Parameters

Disability weight

```
0.081
```

Disability weight representing chronic health loss among surviving congenital heart disease patients.

Years lived with disability

```
YLD = survivors * disability_weight * study_years
```

---

# Sensitivity Analysis

Because untreated mortality varies depending on lesion severity and access to supportive care, multiple mortality scenarios are evaluated.

Scenarios tested

```
0.20 untreated mortality
0.25 untreated mortality
0.30 untreated mortality
0.35 untreated mortality
```

Each scenario recalculates:

- excess deaths  
- years of life lost  
- years lived with disability  
- total DALYs

---

# Total Burden

Total burden is calculated using the Global Burden of Disease framework.

```
DALYs = YLL + YLD
```

Where

- YLL represents premature mortality
- YLD represents non fatal health loss
