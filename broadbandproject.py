# Import requirements
import numpy as np
import pandas as pd
import math 

# Read in broadband data
broadband = pd.read_csv('broadbandbyco.csv')

# Remove unwanted characters in 'Coverage' column
broadband['Coverage'] = broadband['Coverage'].str.replace('%', '')
print(broadband)

# Convert Coverage column to floats
broadband['Coverage'] =broadband['Coverage'].astype(float)

# Round up values in 'Coverage' column
broadband['Coverage'] = broadband['Coverage'].round(0)
print(broadband)

# Sort dataframe by ascending population values 
broadband = broadband.sort_values('Population')
print(broadband)

# Import requirements
import matplotlib.pyplot as plt
import seaborn as sns

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