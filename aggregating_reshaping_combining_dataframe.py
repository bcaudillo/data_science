# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('Austin_Animal_Center_Outcomes_022822.csv')

# Preview the first few rows of the DataFrame
df.head()

# Display summary information about the DataFrame (column names, data types, null values)
df.info()

# Convert 'DateTime' and 'Date of Birth' from object to datetime type for easier manipulation
df['DateTime'] = pd.to_datetime(df['DateTime'])
df['Date of Birth'] = pd.to_datetime(df['Date of Birth'])

# Drop the 'Outcome Subtype' column due to high number of missing values
df = df.drop(columns=['Outcome Subtype'])
print(df.columns)

# Show duplicated rows (but does not assign or print them)
df[df.duplicated()]

# Drop duplicated rows from the DataFrame
df = df.drop_duplicates()

# Check how many missing values are in 'Age upon Outcome'
print(df['Age upon Outcome'].isna().sum())  # there are 5 NaNs

# Check the data type of 'Age upon Outcome'
print(df['Age upon Outcome'].dtype)

# Display the first few entries of 'Age upon Outcome'
print(df['Age upon Outcome'].head())

# Remove any rows with missing data (including NaNs in 'Age upon Outcome')
df = df.dropna()

# Split the string in 'Age upon Outcome' into numeric and unit components
df['Age Number'] = df['Age upon Outcome'].str.split(" ").str[0]
df['Age Unit'] = df['Age upon Outcome'].str.split(" ").str[1]

print(df.columns)

# Create a dictionary to map age units to number of days
age_vals = {
    'years': 365,
    'year': 365,
    'months': 30,
    'month': 30,
    'weeks': 7,
    'week': 7,
    'days': 1,
    'day': 1
}

# Map the string age units to numeric day equivalents
df['Age Unit'] = df['Age Unit'].map(age_vals)

# Display the mapped values (in days) of age units
print(df['Age Unit'].head())

# Convert 'Age Number' column to integer (nullable integer type)
df['Age Number'] = df['Age Number'].astype('Int16')

# Calculate age in days by multiplying number and unit
df['Age upon Outcome'] = df['Age Number'] * df['Age Unit']

# Display the calculated age in days
print(df['Age upon Outcome'].head())

# Plot histogram of age upon outcome
fig, ax = plt.subplots()
ax.hist(df['Age upon Outcome'], bins=30)
ax.axvline(df['Age upon Outcome'].median(), c='r', linestyle='--')  # Add median line
plt.show()

# Fill any remaining missing age values with the median (though we dropped NaNs earlier)
df['Age upon Outcome'] = df['Age upon Outcome'].fillna(df['Age upon Outcome'].median())

# Confirm that there are no more missing values
df['Age upon Outcome'].isna().sum()

# Recalculate age based on the actual difference between intake and date of birth
df['Age upon Outcome'] = (df['DateTime'] - df['Date of Birth']).dt.days

# Print out the number of missing values in the updated age calculation
print("There are " + str(df['Age upon Outcome'].isna().sum()) + " missing values.")
print(df['Age upon Outcome'].head())

# Display the unique values in the 'Sex upon Outcome' column
print(df['Sex upon Outcome'].unique())

# Define a function to group animals by whether they are fixed (neutered/spayed) or intact
def fixed_mapper(status):
    '''
    Takes in the current status of animals and outputs whether they have been fixed
    '''
    if status in ['Neutered Male', 'Spayed Female']:
        return 'Fixed'
    elif status in ['Intact Male', 'Intact Female']:
        return 'Intact'
    else:
        return 'Unknown'

# Apply the grouping function to create a new column
df['Grouped Sex upon Outcome'] = df['Sex upon Outcome'].map(fixed_mapper)

# Preview the new column
df[['Grouped Sex upon Outcome']].head()

# Display a bar plot of the value counts for the grouped sex outcome
df['Grouped Sex upon Outcome'].value_counts().plot(kind='bar')

# Check how many missing values are in the 'Outcome Type' column
df['Outcome Type'].isna().sum()

# Create a new boolean column indicating whether the animal has a name
df['Name Missing'] = df['Name'].isna()

# Preview the DataFrame with the new column
df.head()

# Drop all columns that contain any missing values
df_clean = df.dropna(axis=1)

# Print summary info for the cleaned DataFrame
print(df_clean.info())

# Save the cleaned DataFrame to a new CSV file
df_clean.to_csv('cleaned_animal_data.csv')
