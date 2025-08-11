Data Cleaning and Preprocessing for KaggleV2-May-2016 Dataset
This repository contains a Python script for cleaning and preparing the KaggleV2-May-2016.csv dataset, which includes information on patient appointments. The goal of this project is to transform the raw data into a clean, structured format ready for further exploratory data analysis and machine learning model development.

Project Goal
The primary objective of this script is to handle common data quality issues such as duplicates, inconsistent data types, and invalid entries, ensuring the dataset is reliable for analysis.

How to Use
Download the data: Place the KaggleV2-May-2016.csv file in the same directory as this script.

Install dependencies: Ensure you have pandas and numpy installed. If not, you can install them using pip:

pip install pandas numpy

Run the script: Execute the data_cleaner.py script.

python data_cleaner.py

Key Features of the Script
Duplicate Removal: Identifies and removes duplicate records.

Data Type Conversion: Converts date columns (ScheduledDay, AppointmentDay) to the correct datetime format.

Column Renaming: Renames the No-show column to No_show for easier access.

Data Validation: Removes physically impossible data entries, such as negative age values.
