import pandas as pd  # Import the pandas library and give it the alias 'pd'

df = pd.read_csv('WorldCupMatches.csv')  # Load the WorldCupMatches CSV file into a DataFrame

df.head(7)  # Display the first 7 rows of the DataFrame

df.tail(3)  # Display the last 3 rows of the DataFrame

df.info()  # Display summary info about the DataFrame, including column data types and non-null counts

df.shape  # Show the number of rows and columns in the DataFrame as a tuple (rows, columns)

df.iloc[3:6]  # Select rows by index position from 3 up to (but not including) 6 using integer-location based indexing

df.loc[5:9, ['Home Team Name', 'Away Team Name']]  
# Select rows 5 to 9 (inclusive) and only the columns 'Home Team Name' and 'Away Team Name'

df.loc[(df['Year'] == 1950) & (df['Stage'] == 'Group 3'), 'Attendance']  
# Get the 'Attendance' values for matches in 1950 that were in 'Group 3'

neth_home = len(df[df['Home Team Name'] == ('Netherlands')])  
# Count how many times the Netherlands played as the home team

neth_home  # Output the number of times Netherlands was the home team

len(df[df['Away Team Name']==('Netherlands')]) + neth_home  
# Count away matches for Netherlands and add to home match count for total appearances

usa_2014_mask = (
    # Create a boolean mask for matches where the USA was either home or away AND the year was 2014
    (
        (df['Home Team Name'] == 'USA') |
        (df['Away Team Name'] == 'USA')
    ) &
    (df['Year'] == 2014)
)

len(df[usa_2014_mask])  
# Apply the mask to the DataFrame and count how many matches fit that criteria

df.set_index('MatchID', inplace = True)  
# Set the 'MatchID' column as the index of the DataFrame (modifies df in place)

df.head()  # Show the first 5 rows of the updated DataFrame

df.loc[1085, 'Home Team Name': 'Half-time Away Goals']  
# Access a specific row by MatchID (1085) and slice columns from 'Home Team Name' to 'Half-time Away Goals'

df.reset_index(inplace = True)  
# Reset the index to default integer index and move 'MatchID' back to a regular column

df.drop(columns = ['Assistant 1', 'Assistant 2', 'Win conditions'], inplace=True)  
# Drop the specified columns from the DataFrame

print(df.columns)  # Print the list of column names in the DataFrame

df['Datetime'].dtype  # Check the data type of the 'Datetime' column

df['Datetime'] = pd.to_datetime(df['Datetime'], format= 'mixed')  
# Convert the 'Datetime' column to pandas datetime objects, automatically handling mixed formats

df['Datetime'].head()  # Show the first 5 entries in the converted 'Datetime' column

df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']  
# Create a new column for the total number of goals in each match

high_score_df = df[df['Total Goals']>=5]  
# Filter matches where 5 or more total goals were scored

len(high_score_df)  # Count how many high-scoring matches there were

df['High_Total_Score'] = (df['Total Goals'] >= 5).astype('int')  
# Create a binary (0 or 1) column indicating if the match had 5 or more total goals

print(df['High_Total_Score'].head())  
# Print the first 5 values in the 'High_Total_Score' column

df['Half-time Goals'] = df['Half-time Home Goals'] + df['Half-time Away Goals']  
# Create a new column summing half-time goals from both teams

df.columns  # List all column names in the DataFrame

df.loc[df['Home Team Name'].str.contains('Korea') | df['Away Team Name'].str.contains('Korea')].head()  
# Filter and display matches where either team name contains 'Korea'

mean_home_SK = df.loc[df['Home Team Name'] == 'Korea Republic',  'Home Team Goals'].mean()  
# Calculate the average number of goals Korea Republic scored when they played as the home team

mean_home_SK  # Output the mean value

std_home_SK = df.loc[df['Home Team Name'] == 'Korea Republic',  'Home Team Goals'].std(ddof=1)  
# Calculate the standard deviation of home goals scored by Korea Republic

std_home_SK  # Output the standard deviation

max_away_NK = df.loc[df['Away Team Name'] == 'Korea DPR',  'Away Team Goals'].max()  
# Find the maximum number of goals scored by Korea DPR when playing as the away team

max_away_NK  # Output the max goals scored away by Korea DPR

df.loc[df['Home Team Name'] == 'Korea Republic',  ['Attendance', 'Home Team Goals', 'Away Team Goals', 'Total Goals']].mean()  
# Calculate the mean of several stats for matches where Korea Republic was the home team

df.loc[df['Away Team Name'] == 'Korea Republic',  'Home Team Name'].unique()  
# List the unique home teams that played against Korea Republic when they were the away team

away_match_teamcount = df.loc[df['Away Team Name'] == 'Korea Republic',  'Home Team Name'].value_counts()  
# Count how many times each team hosted Korea Republic (when they were the away team)

away_match_teamcount  # Output the result
