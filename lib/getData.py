import csv

def save_data_to_csv(data, filename):
    # Save data to a CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def main():
    # Get input from the user
    country = input("What is your country? ")
    year = input("What is your year? ")

    # Prompt the user for death rates for each age group for the specified country
    data = [
        ['Age group (years)', f'Death rate, {country}, {year}',],
        ['0-4', float(input(f"What is the rate for ages 0-4 in {country}? ")), ],
        ['5-9', float(input(f"What is the rate for ages 5-9 in {country}? ")), ],
        ['10-14', float(input(f"What is the rate for ages 10-14 in {country}? ")), ],
        ['15-19', float(input(f"What is the rate for ages 15-19 in {country}? ")), ],
        ['20-24', float(input(f"What is the rate for ages 20-24 in {country}? ")), ],
        ['25-29', float(input(f"What is the rate for ages 25-29 in {country}? ")), ],
        ['30-34', float(input(f"What is the rate for ages 30-34 in {country}? ")), ],
        ['35-39', float(input(f"What is the rate for ages 35-39 in {country}? ")), ],
        ['40-44', float(input(f"What is the rate for ages 40-44 in {country}? ")), ],
        ['45-49', float(input(f"What is the rate for ages 45-49 in {country}? ")), ],
        ['50-54', float(input(f"What is the rate for ages 50-54 in {country}? ")), ],
        ['55-59', float(input(f"What is the rate for ages 55-59 in {country}? ")), ],
        ['60-64', float(input(f"What is the rate for ages 60-64 in {country}? ")), ],
        ['65-69', float(input(f"What is the rate for ages 65-69 in {country}? ")), ],
        ['70-74', float(input(f"What is the rate for ages 70-74 in {country}? ")), ],
        ['75-79', float(input(f"What is the rate for ages 75-79 in {country}? ")), ],
        ['80-84', float(input(f"What is the rate for ages 80-84 in {country}? ")), ],
        ['85+', float(input(f"What is the rate for ages 85+ in {country}? ")), ]
    ]

    filename = f'lib/data/{country}_{year}_data.csv'
    save_data_to_csv(data, filename)
    print(f"Data has been saved to {filename}")

if __name__ == "__main__":
    main()
