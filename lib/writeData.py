import csv

def save_data_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def main():
    # hard code the data 
    
    # US 2019 Data
    us_data = [
        ['Age group (years)', 'Death rate, US, 2019'],
        ['0-4', 0.04],
        ['5-9', 0.02],
        ['10-14', 0.02],
        ['15-19', 0.02],
        ['20-24', 0.06],
        ['25-29', 0.11],
        ['30-34', 0.29],
        ['35-39', 0.56],
        ['40-44', 1.42],
        ['45-49', 4.00],
        ['50-54', 14.13],
        ['55-59', 37.22],
        ['60-64', 66.48],
        ['65-69', 108.66],
        ['70-74', 213.10],
        ['75-79', 333.06],
        ['80-84', 491.10],
        ['85+', 894.45]
    ]

    # Uganda 2019 Data
    ug_data = [
        ['Age group (years)', 'Death rate, Uganda, 2019'],
        ['0-4', 0.40],
        ['5-9', 0.17],
        ['10-14', 0.07],
        ['15-19', 0.23],
        ['20-24', 0.38],
        ['25-29', 0.40],
        ['30-34', 0.75],
        ['35-39', 1.11],
        ['40-44', 2.04],
        ['45-49', 5.51],
        ['50-54', 13.26],
        ['55-59', 33.25],
        ['60-64', 69.62],
        ['65-69', 120.78],
        ['70-74', 229.88],
        ['75-79', 341.06],
        ['80-84', 529.31],
        ['85+', 710.40]
    ]

    us_filename = 'lib/data/US_2019_data.csv'
    ug_filename = 'lib/data/Uganda_2019_data.csv'

    save_data_to_csv(us_data, us_filename)
    save_data_to_csv(ug_data, ug_filename)

    print(f"Data has been saved to {us_filename} and {ug_filename}")

if __name__ == "__main__":
    main()
