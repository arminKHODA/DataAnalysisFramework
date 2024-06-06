import os
import glob
import subprocess
import pandas as pd
import re
import glob
import lib.genData as genData

def add_data_to_database():
    print("Adding data to the database...")
    script_path = 'lib/getData.py'
    subprocess.run(['python', script_path])

def read_data_from_database():
    print("Reading data from the database...")
    script_path = 'lib/readData.py'
    subprocess.run(['python', script_path])

def generate_rate_from_database():
    print("generate rate from the database...")
    data_directory = 'lib/data'
    genData.generate_rate_from_database(data_directory)

def remove_all_database():
    data_directory = 'lib/data'
    data_files = glob.glob(os.path.join(data_directory, '*_data.csv'))

    if not data_files:
        print("No data files found.")
        return

    print("Found the following data files:")
    for file in data_files:
        print(file)

    choice = input("Enter 'all' to remove all files, enter a file name to remove that file, or 'ask' to decide for each file: ")

    if choice.lower() == 'all':
        for file in data_files:
            os.remove(file)
            print(f"Removed {file}")
    elif choice.lower() == 'ask':
        for file in data_files:
            remove = input(f"Do you want to remove {file}? (yes/no): ").lower()
            if remove == 'yes':
                os.remove(file)
                print(f"Removed {file}")
    else:
        # User provided a specific file name
        specific_file = os.path.join(data_directory, choice)
        if specific_file in data_files:
            os.remove(specific_file)
            print(f"Removed {specific_file}")
        else:
            print("File not found or invalid option.")

def add_hardcode_database():
    print("Adding hardcoded data (us2019|ug2019) to the database...")
    script_path = 'lib/writeData.py'
    subprocess.run(['python', script_path])

def main():
    while True:
        print("\n")
        print("Welcome to COPD (version 0.001 alpha)")
        print("Please select:")
        print("1. Add data to database")
        print("2. Read data from database")
        print("3. Generate rate from current database")
        print("4. Remove all database")
        print("5. Add us2019|ug2019 to database")
        
        option = input("\nSelect your option: ")
        
        if option == '1':
            add_data_to_database()
        elif option == '2':
            read_data_from_database()
        elif option == '3':
            generate_rate_from_database()
        elif option == '4':
            remove_all_database()
        elif option == '5':
            add_hardcode_database()
        else:
            print("Invalid option. Please try again.")
        
        # Ask the user if they want to continue or exit
        continue_option = input("\nDo you want to perform another operation? (yes/no): ").lower()
        if continue_option != 'yes':
            print("Exiting COPD. Goodbye ;) ")
            break

if __name__ == "__main__":
    main()
    print("-------")