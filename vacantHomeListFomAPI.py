# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:01:39 2020

@author: Scott
"""

#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
import os
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.baltimorecity.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.baltimorecity.gov,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("qqcv-ihn5", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

print(results_df)

dirName = 'currentVacantFile'
 
try:
    # Create target Directory
    os.mkdir(dirName)
    #print("Directory " , dirName ,  " Created ") 
except FileExistsError:
    #print("Directory " , dirName ,  " already exists")
    
    
#copy contents of directory into other directory

#delete contents of directory 

# replace with new file