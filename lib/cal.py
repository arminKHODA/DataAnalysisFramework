# Reporting to Line Manager:
"""
To: [Line Manager]
From: [armin]
Date: [17/3/2024]

Subject: Python Script for Calculating Death Rates from COPD

Dear [Line Manager's Name],

I have developed a Python script to calculate both crude death rates and age-standardized death rates for chronic obstructive pulmonary disease (COPD) in the United States and Uganda for the year 2019. Below is a brief overview of the process:

1. Crude Death Rate Calculation:
   - For each country, the sum of all age-specific death rates is calculated, representing the total number of deaths per 100,000 people in the population.

2. Age-Standardized Death Rate Calculation:
   - The WHO standard population is used as the reference population.
   - Age-specific death rates for each country are applied to the corresponding age groups in the WHO standard population.
   - The weighted sum of these rates is calculated to obtain the age-standardized death rate, providing a fair comparison between countries by adjusting for differences in age distributions.

Assumptions:
- We assume the age distributions of the United States and Uganda are consistent with the WHO standard population for the purpose of age standardization.
- The death rates provided are accurate and representative of the entire population.

Reasons for Differences:
- Crude death rates reflect the actual mortality experience of each country's population without adjusting for age differences. Therefore, differences in crude death rates may reflect variations in population age structures.
- Age-standardized death rates, on the other hand, provide a more accurate comparison between countries by accounting for differences in age distributions. It allows us to compare mortality rates while controlling for the confounding effect of age.

Please review the attached Python script for implementation details. Feel free to reach out if you need further clarification or adjustments.

Best regards,
[Alireza Khodatars (Armin)]
"""

# Age-specific death rates for COPD in 2019 (deaths per 100,000 people)
death_rates_us = [
    0.04, 0.02, 0.02, 0.02, 0.06, 0.11, 0.29, 0.56, 1.42, 4.00, 
    14.13, 37.22, 66.48, 108.66, 213.10, 333.06, 491.10, 894.45
]

death_rates_uganda = [
    0.40, 0.17, 0.07, 0.23, 0.38, 0.40, 0.75, 1.11, 2.04, 5.51, 
    13.26, 33.25, 69.62, 120.78, 229.88, 341.06, 529.31, 710.40
]

# Calculate Crude Death Rate
crude_death_rate_us = sum(death_rates_us)
crude_death_rate_uganda = sum(death_rates_uganda)

# WHO Standard Population
# Age groups: 0-4, 5-9, ..., 85+
# Corresponding population counts (in thousands)
standard_population = [
    38780, 38513, 36277, 37521, 36831, 34660, 30970, 27333, 
    24779, 22595, 21859, 21320, 19199, 15417, 10295, 5996, 2440, 1030
]

# Calculate Age-Standardized Death Rate
def calculate_age_standardized_rate(death_rates, standard_population):
    weighted_sum = sum(dr * pop for dr, pop in zip(death_rates, standard_population))
    total_population = sum(standard_population)
    return (weighted_sum / total_population) * 100000

age_standardized_rate_us = calculate_age_standardized_rate(death_rates_us, standard_population)
age_standardized_rate_uganda = calculate_age_standardized_rate(death_rates_uganda, standard_population)

# Print Results
print("Crude Death Rate (COPD) in 2019:")
print("United States: {:.1f} deaths per 100,000 people".format(crude_death_rate_us))
print("Uganda: {:.1f} deaths per 100,000 people\n".format(crude_death_rate_uganda))

print("Age-Standardized Death Rate (COPD) in 2019:")
print("United States: {:.1f} deaths per 100,000 people".format(age_standardized_rate_us))
print("Uganda: {:.1f} deaths per 100,000 people".format(age_standardized_rate_uganda))
