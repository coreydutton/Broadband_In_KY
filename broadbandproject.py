# Import requirements
import numpy as np
import pandas as pd
import math 
import matplotlib.pyplot as plt
import seaborn as sns

# Read in broadband data
broadband = pd.read_csv('broadbandbyco.csv')

# View data
print(broadband)

# Remove unwanted characters from 'Population' column
broadband['Coverage'] =broadband['Coverage'].str.replace('%', '')

# Convert 'Coverage' to floats
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

# Determine smallest 5 counties
smallest_counties = broadband.head()
print(smallest_counties)

# Determine largest 5 counties
largest_counties = broadband.tail()
print(largest_counties)

# Determine lowest broadband access
my_min = broadband['Coverage'].loc[broadband['Coverage'].idxmin()]      # Minimum in column
print(my_min)

# Find matching county
lowest_coverage = broadband[broadband['Coverage'] == 18] 
print(lowest_coverage)

# Determine counties with coverage under fifty percent
coverage_under_50 = broadband[broadband['Coverage'] < 50] 
print(coverage_under_50)

# Create a line plot of broadband coverage by ascending population
sns.set_theme(style="whitegrid")
broadband.plot(kind= "line", x= "Population", y= "Coverage", color= "green", fontsize= 12)
plt.title('Broadband Coverage by Population Size', fontsize= 16)
plt.margins(0.2)
plt.xlim([0, 120])
plt.ylim([0, 100])
plt.show

# Create a scatterplot of broadband coverage by population
broadband_by_pop = sns.regplot(x=broadband['Population'], y=broadband['Coverage'])
plt.xlim([0, 780000])
plt.ylim([0, 100])
print(broadband_by_pop)

# Create a scatterplot of broadband coverage in counties with population up to 500k
broadband_by_pop = sns.regplot(x=broadband['Population'], y=broadband['Coverage'])
plt.xlim([0, 50000])
plt.ylim([0, 100])
print(broadband_by_pop)

# Create a line plot of broadband coverage for smallest counties
smallest_counties.plot( x= "County", y= "Coverage", color= "violet", marker= ('o'))
plt.title('Broadband Coverage in Smallest Kentucky Counties')
plt.ylim(0, 100)
plt.margins(0)

# Create a line plot of broadband coverage for largest counties
largest_counties.plot( x= "County", y= "Coverage", color= "blue", marker= ('o'))
plt.title('Broadband Coverage in Largest Kentucky Counties')
plt.ylim([90, 100])
plt.ylabel('Broadband Coverage in %', size =12)
plt.xlabel('County', size =12)
plt.margins(0)