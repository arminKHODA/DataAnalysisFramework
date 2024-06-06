import pandas as pd
import os
import re
import glob

WHO_STANDARD_POPULATION = {
    '0-4': 8860, '5-9': 8690, '10-14': 8600, '15-19': 8470, '20-24': 8220,
    '25-29': 7930, '30-34': 7610, '35-39': 7150, '40-44': 6590, '45-49': 6040,
    '50-54': 5370, '55-59': 4550, '60-64': 3720, '65-69': 2960, '70-74': 2210,
    '75-79': 1520, '80-84': 910, '85+': 635
}

def list_data_files(data_directory):
    csv_files = glob.glob(os.path.join(data_directory, '*.csv'))
    data_files = {}
    for i, file_path in enumerate(csv_files, 1):
        file_name = os.path.basename(file_path)
        match = re.match(r'(.+)_(\d+)_data\.csv', file_name)
        if match:
            country_year = f"{match.group(1).replace('_', ' ')} {match.group(2)}"
            data_files[str(i)] = (country_year, file_path)
    return data_files

def prompt_for_population(country, year):
    print(f"Data for {country} {year} selected.")
    user_input = input("Enter the total population for the calculation or press enter to provide a default value: ")
    if user_input.strip():
        total_population = int(user_input)
    else:
        total_population = None
    return total_population

def prompt_for_age_group_population(default_population):
    print("Do you want to input population figures for each age group? (yes/no)")
    response = input().strip().lower()
    age_group_populations = {}
    if response == 'yes':
        age_groups = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', 
                      '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85+']
        for age_group in age_groups:
            print(f"Enter population for age group {age_group}:")
            population = input().strip()
            if population.isdigit():
                age_group_populations[age_group] = int(population)
            else:
                print(f"No valid input provided for age group {age_group}, using default.")
                age_group_populations[age_group] = default_population
    else:
        print("Using WHO standard population for all age groups.")
        age_group_populations = WHO_STANDARD_POPULATION
    
    return age_group_populations

def get_death_rate_column(data):
    for column in data.columns:
        if 'death rate' in column.lower() or 'rate' in column.lower():
            return column
    return None

# -------------------
def calculate_age_standardized_death_rate(data, total_population, age_group_populations):
    sum_expected_deaths = 0
    total_standard_population = sum(WHO_STANDARD_POPULATION.values())

    # Correcting the column name from 'Age Group' to 'Age group (years)'
    for age_group, standard_population in WHO_STANDARD_POPULATION.items():
        # Make sure we access the correct column name here
        age_group_data = data[data['Age group (years)'] == age_group]

        # Assuming the total deaths per age group are calculated elsewhere and stored in 'total_deaths'
        age_group_death_rate = (age_group_data['total_deaths'].sum() / total_population) * 100000

        # Calculate expected deaths for this age group
        expected_deaths = age_group_death_rate * (standard_population / total_standard_population)
        sum_expected_deaths += expected_deaths

    # Calculate the age-standardized death rate
    asdr = (sum_expected_deaths / total_standard_population) * 100000
    return asdr

def process_death_rates(data, country, year, total_population):
    death_rate_column = get_death_rate_column(data)
    if not death_rate_column:
        print("Error: Unable to find a death rate column in the data file. Please check the file format.")
        return

    print(f"Using total population: {total_population}")

    # Calculate and print death rates for each age group
    if 'Age Group' in data.columns:  # Assuming 'Age Group' is the column name
        for age_group in data['Age Group'].unique():
            age_group_data = data[data['Age Group'] == age_group]
            age_group_total_deaths = (age_group_data[death_rate_column] * total_population / 100000).sum()
            age_group_death_rate = (age_group_total_deaths / total_population) * 100000
            print(f"{age_group} Death Rate: {age_group_death_rate:.1f} per 100,000 people")

    # Calculate total deaths and crude death rate
    data['total_deaths'] = pd.to_numeric(data[death_rate_column], errors='coerce') * total_population / 100000
    total_deaths = data['total_deaths'].sum()  # Ensure that total_deaths is numeric
    crude_death_rate = (total_deaths / total_population) * 100000

    print(f"Country: {country}")
    print(f"Year: {year}")
    print(f"Total Deaths: {total_deaths:.1f}")
    print(f"Crude Death Rate: {crude_death_rate:.1f} per 100,000 people")


def generate_rate_from_database(data_directory):
    data_files = list_data_files(data_directory)
    if not data_files:
        print("No data files found in the directory.")
        return
    
    for key, (country_year, _) in data_files.items():
        print(f"{key}. {country_year}")

    selection = input("Select the dataset number to calculate the rate: ")
    if selection not in data_files:
        print("Invalid selection. Exiting the rate calculation.")
        return

    _, selected_file = data_files[selection]
    
    data = pd.read_csv(selected_file)
    country, year = data_files[selection][0].split()[:2]

    # Determine if user wants to enter population
    total_population = prompt_for_population(country, year) or 328239523
    # Determine if user wants to enter age group population data or use WHO Standard
    age_group_populations = prompt_for_age_group_population(total_population)

    process_death_rates(data, country, year, total_population)
    asdr = calculate_age_standardized_death_rate(data, total_population, age_group_populations)
    print(f"Age-Standardized Death Rate: {asdr:.1f} per 100,000 people")


if __name__ == "__main__":
    data_directory = 'lib/data'
    generate_rate_from_database(data_directory)
