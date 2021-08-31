#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open research Central (ORC) helper script
Get gender probabilities for the article reviewers
@authors: Antonija Mijatovic (antonija.mijatovic@mefst.hr)
"""
import os
import io
import csv
import re
import string
import pandas as pd
import numpy as np
from genderize import Genderize

# ORC data
file_name = r'C:\Users\Korisnik\Desktop\ORC_script\all_info.xlsx'

df_all = pd.read_excel(io=file_name)
df = df_all.replace(np.nan, 'No data', regex=True)

print(df.head(5)) 

names = df["name"]

print(names.head())

names_list = names.tolist()
names_reg = []
names_clean = []
for val in names_list:
    names_reg.append(re.findall(r"^[a-zA-z]+", val))    
for value in names_reg:
    for val in value:
        names_clean.append(val)    
    
genders = []
genders.append(Genderize().get(names_clean)) 


# Save the results manually into genderizeReviewers_results.txt

with open(r'C:\Users\Korisnik\Desktop\ORC_script\ORC_results\genderizeReviewers_results.txt', "r") as file_object:
    content = file_object.read()
    file_object.close()
    
print(content.replace("{'name':", "\n"))  