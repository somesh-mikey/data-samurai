import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path, low_memory=False)

def clean_data(df):
    df.drop(columns=['Data Quality'], inplace=True, errors='ignore')
    df[['Total Rain (mm)', 'Total Snow (cm)', 'Total Precip (mm)']] = df[['Total Rain (mm)', 'Total Snow (cm)', 'Total Precip (mm)']].fillna(0)
    df['Max Temp (°C)'].fillna(df['Max Temp (°C)'].mean(), inplace=True)
    df['Min Temp (°C)'].fillna(df['Min Temp (°C)'].mean(), inplace=True)
    df['Mean Temp (°C)'].fillna(df['Mean Temp (°C)'].mean(), inplace=True)
    df['Date/Time'] = pd.to_datetime(df['Date/Time'], errors='coerce')
    df['Spd of Max Gust (km/h)'] = pd.to_numeric(df['Spd of Max Gust (km/h)'], errors='coerce')
    df['Spd of Max Gust (km/h)'].fillna(df['Spd of Max Gust (km/h)'].median(), inplace=True)
    
    def remove_outliers(df, column):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    
    for col in ['Max Temp (°C)', 'Min Temp (°C)', 'Mean Temp (°C)', 'Spd of Max Gust (km/h)']:
        df = remove_outliers(df, col)
    
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace(r'[^a-zA-Z0-9_]', '', regex=True)
    df.drop_duplicates(inplace=True)
    return df

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

def compare_datasets(original_path, cleaned_path):
    original_df = load_data(original_path)
    cleaned_df = load_data(cleaned_path)
    accuracy_percentage = (cleaned_df.shape[0] / original_df.shape[0]) * 100
    return original_df.shape[0], cleaned_df.shape[0], accuracy_percentage

original_file = "/mnt/data/crum_weather_data_curr.csv"
cleaned_file = "/mnt/data/crum_weather_data_cleaned.csv"

df = load_data(original_file)
df_cleaned = clean_data(df)
save_data(df_cleaned, cleaned_file)
original_rows, cleaned_rows, accuracy = compare_datasets(original_file, cleaned_file)

print(f"Original Rows: {original_rows}")
print(f"Cleaned Rows: {cleaned_rows}")
print(f"Accuracy: {accuracy:.2f}%")
