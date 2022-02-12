#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 10:38:48 2022

@author: saathvikdirisala
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

continent_df = pd.read_csv("Downloads/GlobalHealth/countryContinent.csv", encoding="latin-1")
female_ed_df = pd.read_csv("Downloads/GlobalHealth/literacy_rate_adult_female_percent_of_females_ages_15_above.csv")
male_ed_df = pd.read_csv("Downloads/GlobalHealth/literacy_rate_adult_male_percent_of_males_ages_15_above.csv")

female_ed_df = female_ed_df.set_index("country")
male_ed_df = male_ed_df.set_index("country")

def non_nan(df):
    return [(df.index[row], df.columns[col]) for row in range(df.shape[0]) for col in range(df.iloc[row,:].shape[0]) if not np.isnan(df.iloc[row, col])]

female = non_nan(female_ed_df)
male = non_nan(male_ed_df)

female.remove(("Afghanistan", "2010"))

female_ed_df = female_ed_df.merge(continent_df, left_index = True, right_on = "country", how = "left")
male_ed_df = male_ed_df.merge(continent_df, left_index = True, right_on = "country", how = "left")
female_ed_df = female_ed_df.set_index("country")
male_ed_df = male_ed_df.set_index("country")
female_ed_df = female_ed_df.drop(['code_2', 'code_3', 'country_code', 'iso_3166_2', 'sub_region_code', 'region_code'], axis = 1)
male_ed_df = male_ed_df.drop(['code_2', 'code_3', 'country_code', 'iso_3166_2', 'sub_region_code', 'region_code'], axis = 1)

for i in range(len(female_ed_df)):
    if not isinstance(female_ed_df.iloc[i,37], str):
        female_ed_df.iloc[i,37] = "Other"
    if not isinstance(male_ed_df.iloc[i,37], str):
        male_ed_df.iloc[i,37] = "Other"

female_df_sub = female_ed_df.groupby("sub_region").mean()
male_df_sub = male_ed_df.groupby("sub_region").mean()

# =============================================================================
# for j in range(len(female_ed_df)):
#     
#     new_df0 = female_ed_df.iloc[j,:37]
#     new_df0 = new_df0[new_df0.isnull()==False]
#     new_df1 = male_ed_df.iloc[j,:37]
#     new_df1 = new_df1[new_df1.isnull()==False]
#     
#     years_female = list(pd.Series(new_df0.index).apply(int))
#     literacy_female = list(new_df0)
#     years_male = list(pd.Series(new_df1.index).apply(int))
#     literacy_male = list(new_df1)
#     plt.figure(j)
#     
#     plt.plot(years_female, literacy_female, c="red", label = "Female")
#     plt.plot(years_male, literacy_male, c="blue", label = "Male")
#     plt.legend()
#     plt.title(female_ed_df.index[j])
# =============================================================================

for j in range(len(female_df_sub)):
    
    new_df0 = female_df_sub.iloc[j,:]
    new_df0 = new_df0[new_df0.isnull()==False]
    new_df1 = male_df_sub.iloc[j,:]
    new_df1 = new_df1[new_df1.isnull()==False]
    
    years_female = list(pd.Series(new_df0.index).apply(int))
    literacy_female = list(new_df0)
    years_male = list(pd.Series(new_df1.index).apply(int))
    literacy_male = list(new_df1)
    plt.figure(j)
    
    plt.plot(years_female, literacy_female, c="red", label = "Female")
    plt.plot(years_male, literacy_male, c="blue", label = "Male")
    #plt.xticks(rotation=-90)
    plt.legend()
    plt.title(female_df_sub.index[j])
