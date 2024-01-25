# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 23:26:01 2021

@author: md894973
"""

import pandas as pd
df=pd.read_csv(r'C:\Users\md894973\2021_charging_infrastructure_ridesourcing_VOT\2021_charging_infrastructure_ridesourcing_VOT\src\gitRepository\final_output.csv')

# Split by space in location column and expand to two new columns with column labels
df[['latitude','longitude']] = df['Location'].str.split(' ',expand=True)

df.to_csv(r'C:\Users\md894973\2021_charging_infrastructure_ridesourcing_VOT\2021_charging_infrastructure_ridesourcing_VOT\src\gitRepository\feasibleLocationGIS.csv')