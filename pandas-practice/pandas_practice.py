import pandas as pd
import dateutil


# -- LOADING THE DATA

# Load data from csv file
data = pd.read_csv('~/environment/python-practice/pandas-practice/phone_data.csv')

# Convert date from string to date times
data['date'] = data['date'].apply(dateutil.parser.parse, dayfirst=True)

print(data)


# -- SUMMARIZING THE DATA

# How many rows the dataset
print(data['item'].count())

# What was the longest phone call / data entry?
print(data['duration'].max())

# How many seconds of phone calls are recorded in total?
print(data['duration'][data['item'] == 'call'].sum())

# How many entries are there for each month?
print(data['month'].value_counts())

# Number of non-null unique network entries
print(data['network'].nunique())