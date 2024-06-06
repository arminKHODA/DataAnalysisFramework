# COPD Data Processing Package

This package includes a set of Python scripts for processing and analyzing data related to Chronic Obstructive Pulmonary Disease (COPD). The package currently contains the following scripts:

1. `COPD.py`
2. `cal.py`
3. `genData.py`
4. `getData.py`
5. `readData.py`
6. `writeData.py`

## Features

- Retrieve raw data.
- Process and generate new data from raw inputs.
- Calculate statistical measures from the processed data.
- Write the statistical results to a file.
- Read and display the results from the file.

## Requirements

- Python 3.x

## Usage

1. **COPD.py**
    - This is the main script that integrates the functionalities of the other scripts.
    - It performs the following tasks:
        1. Retrieves raw data.
        2. Processes the data.
        3. Calculates statistics from the processed data.
        4. Writes the statistics to a file.
        5. Reads and prints the data from the file.

    ### Running COPD.py
    ```bash
    python COPD.py
    ```

    This will execute all the functions in sequence and display the results.

2. **cal.py**
    - Contains a function to calculate statistical measures such as mean, median, and standard deviation from the processed data.

    ### Function
    ```python
    calculate_statistics(data)
    ```
    - `data`: The processed data for which statistics need to be calculated.

3. **genData.py**
    - Contains a function to process or generate new data from the raw data.

    ### Function
    ```python
    generate_data(raw_data)
    ```
    - `raw_data`: The raw data to be processed.

4. **getData.py**
    - Contains a function to retrieve raw data.

    ### Function
    ```python
    get_data()
    ```
    - Returns a list of raw data.

5. **readData.py**
    - Contains a function to read and display data from a file.

    ### Function
    ```python
    read_data()
    ```
    - Reads and prints the contents of `output.txt`.

6. **writeData.py**
    - Contains a function to write data to a file.

    ### Function
    ```python
    write_data(data)
    ```
    - `data`: The data to be written to the file.

## Example Usage

### Running each script individually

1. **Retrieve raw data**
    ```python
    from getData import get_data
    data = get_data()
    ```

2. **Process data**
    ```python
    from genData import generate_data
    processed_data = generate_data(data)
    ```

3. **Calculate statistics**
    ```python
    from cal import calculate_statistics
    statistics = calculate_statistics(processed_data)
    ```

4. **Write data to file**
    ```python
    from writeData import write_data
    write_data(statistics)
    ```

5. **Read data from file**
    ```python
    from readData import read_data
    read_data()
    ```

## License

free License.
