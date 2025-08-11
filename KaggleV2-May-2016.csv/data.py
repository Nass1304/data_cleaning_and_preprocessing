# Import necessary libraries
import pandas as pd
import numpy as np
import os

def clean_and_prepare_data(file_name):
    """
    Loads, cleans, and prepares the 'KaggleV2-May-2016.csv' dataset.

    Args:
        file_name (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: The cleaned and prepared DataFrame, or None if an error occurs.
    """
    # --- DEBUGGING STEP: Print the current working directory ---
    current_directory = os.getcwd()
    print(f"Current working directory: {current_directory}")

    # Check if the file exists to provide a helpful error message
    file_path = os.path.join(current_directory, file_name)
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_name}' was not found.")
        print(f"The script is looking for it at: {file_path}")
        print("Please ensure the CSV file is in the same directory as this script and the filename is spelled correctly.")
        return None

    try:
        # Load the data from the provided CSV file.
        df = pd.read_csv(file_path)
        print(f"Successfully loaded '{file_name}'.")

    except Exception as e:
        print(f"An unexpected error occurred while loading the data: {e}")
        return None

    # --- Initial Data Inspection ---
    print("\n--- Initial Data Information ---")
    print(f"Shape of the DataFrame: {df.shape}")
    print("\nFirst 5 rows of the raw data:")
    print(df.head())
    print("\nColumn data types and non-null counts:")
    print(df.info())

    # --- Step 1: Handling Duplicates ---
    initial_rows = df.shape[0]
    df.drop_duplicates(inplace=True)
    duplicates_removed = initial_rows - df.shape[0]
    print(f"\n--- Removed {duplicates_removed} duplicate row(s) ---")

    # --- Step 2: Handling Inconsistent Data Formats ---
    # Convert date/time columns to a proper datetime format.
    df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
    df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])
    print("\n--- Converted 'ScheduledDay' and 'AppointmentDay' to datetime format ---")

    # The 'No-show' column has a typo. Let's rename it for clarity.
    df.rename(columns={'No-show': 'No_show'}, inplace=True)
    print("--- Renamed 'No-show' column to 'No_show' ---")

    # --- Step 3: Handling Missing Values ---
    print("\n--- Missing values before imputation ---")
    print(df.isnull().sum())

    # Based on the initial info, there appear to be no missing values in this dataset.
    # If there were, this section would handle them.

    # --- Step 4: Data Validation and Potential Outliers ---
    # Check for negative values in the 'Age' column, which are physically impossible.
    if (df['Age'] < 0).any():
        negative_age_count = (df['Age'] < 0).sum()
        df = df[df['Age'] >= 0]
        print(f"\n--- Removed {negative_age_count} row(s) with negative age values ---")

    # --- Final Data Inspection ---
    print("\n--- Final Cleaned Data Information ---")
    print(f"Shape of the final cleaned DataFrame: {df.shape}")
    print("\nFirst 5 rows of the cleaned data:")
    print(df.head())
    print("\nFinal column data types and non-null counts:")
    print(df.info())

    return df

if __name__ == "__main__":
    file_name = "KaggleV2-May-2016.csv"

    cleaned_df = clean_and_prepare_data(file_name)

    if cleaned_df is not None:
        print("\nData cleaning and preparation complete.")
        # The cleaned DataFrame is stored in the 'cleaned_df' variable.
        # You can now proceed with further analysis, such as:
        # - Creating new features (e.g., 'Days_to_Appointment')
        # - Visualizing the data with libraries like Matplotlib or Seaborn
        # - Encoding categorical features for a machine learning model
        # For example, to save the cleaned data to a new file:
        # cleaned_df.to_csv("cleaned_KaggleV2-May-2016.csv", index=False)
