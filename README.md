# data-samurai
Overview

This script processes a weather dataset by performing data cleaning steps and comparing the cleaned dataset with the original. The accuracy percentage of retained data is also calculated.

Features

Loads the dataset from a CSV file.

Cleans missing values by filling or removing them appropriately.

Converts data types for consistency.

Removes outliers using the Interquartile Range (IQR) method.

Standardizes column names.

Removes duplicate records.

Saves the cleaned dataset to a new CSV file.

Compares the number of rows in the original and cleaned datasets to calculate accuracy.

Dependencies

Python 3.x

Pandas

Usage

Place the dataset in the specified path.

Run the script to clean and save the processed data.

The script will print the number of original and cleaned rows along with the accuracy percentage.

File Paths

Original dataset: /mnt/data/crum_weather_data_curr.csv

Cleaned dataset: /mnt/data/crum_weather_data_cleaned.csv

Output

The script prints:

Original row count

Cleaned row count

Accuracy percentage

Author

This script is intended for data preprocessing before analytics and machine learning tasks.
