# Import requirements
import numpy as np
import pandas as pd
import math 
import matplotlib.pyplot as plt
import seaborn as sns

# Read in broadband data
broadband = pd.read_csv('broadbandbyco.csv')

# Convert Coverage column to floats
broadband['Coverage'] =broadband['Coverage'].astype(float)

# Remove unwanted characters from 'Population' column
broadband['Population'] =broadband['Population'].str.replace(',', '')

# Convert 'Population' to floats
broadband['Population'] =broadband['Population'].astype(float)

# Round up values in 'Coverage' column
broadband['Coverage'] = broadband['Coverage'].round(0)
print(broadband)

# Sort dataframe by ascending population values 
broadband = broadband.sort_values('Population')
print(broadband)

# Determine median broadband coverage
broadband['Coverage'].median()

# Determine median population size
broadband['Population'].median()

# Determine smallest 10% of counties
smallest_counties = broadband.head(13)
print(smallest_counties)

# Determine largest 10% of counties
largest_counties = broadband.tail(13)
print(largest_counties)

# Set plot style
sns.set_theme(style="whitegrid")

# Line plot of broadband coverage by ascending population
sns.set_theme(style="whitegrid")
broadband.plot(kind= "line", x= "Population", y= "Coverage", color= "green", fontsize= 12)
plt.title('Broadband Coverage by Population Size', fontsize= 16)
plt.margins(0.2)
plt.xlim([0, 120])
plt.ylim([0, 100])
plt.show