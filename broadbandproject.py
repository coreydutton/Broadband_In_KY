import numpy as np
import pandas as pd
import math 

# Read in broadband data
broadband = pd.read_csv('broadbandbyco.csv')

# View data
print(broadband)

# Remove unwanted characters in 'Coverage' column
broadband['Coverage'] = broadband['Coverage'].str.replace('%', '')
print(broadband)

# Convert Coverage column to floats
broadband['Coverage'] =broadband['Coverage'].astype(float)