import os
import pandas as pd

def find_csv_files(directory):
    # Find all CSV files in the directory that match the naming pattern
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('_data.csv')]

def read_and_print_data(file_path):
    # Read and print the data using pandas
    df = pd.read_csv(file_path)
    print(df)

def print_file_list_and_get_choice(csv_files):
    print("Available data files:")
    for i, file_path in enumerate(csv_files, start=1):
        print(f"{i}. {os.path.basename(file_path)}")
    print("\nType 'all' to print all files, or type the name of a file to print just that file:")
    return input("Your choice: ")

def main():
    # Adjust the path based on the script's running location
    data_directory = './lib/data'  # Adjusted to relative path
    csv_files = find_csv_files(data_directory)
    
    if csv_files:
        user_choice = print_file_list_and_get_choice(csv_files)
        
        if user_choice.lower() == 'all':
            for file_path in csv_files:
                print(f"Reading data from {file_path}")
                read_and_print_data(file_path)
                input("Press Enter to continue to the next file...")
                print("\n")
        else:
            selected_file = next((f for f in csv_files if os.path.basename(f) == user_choice), None)
            if selected_file:
                print(f"Reading data from {selected_file}")
                read_and_print_data(selected_file)
            else:
                print(f"File '{user_choice}' not found. Please check the file name and try again.")
    else:
        print("No data file saved in the 'lib' directory.")

if __name__ == "__main__":
    main()
