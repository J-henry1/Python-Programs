# -*- coding: utf-8 -*-
"""Lab_5_N01484167

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l-0p0hbbgO_rWYtxZjShEi7fV0_VBSt7
"""

#Jared Henry
#N01484167
#Version 3/16/2023

import pandas as pd
import numpy as np


df = pd.read_table('items.csv', sep = ',') #reads in csv as Data Frame

df.iloc[:7] #prints out first 7 items of Data Frame

df.iloc[4152:4159] #prints out last 7 items of Data Frame

print("Properties of Data Frame:")
df.info() #prints out info of Data Frame

print("Columns and Rows Count of Data Frame:")
df.shape

print("Properties of 'Bottle_Cost' Attribute':")
df['Bottle_Cost'].describe()

#calulates bottle profit margin then insert's column into Data Frame
for index in df:
  diff = df['Bottle_Retail_Price']-(df['Bottle_Cost'])#gets differece
  Bottle_Profit_Margin = diff/df['Bottle_Retail_Price']#diff is then divided by Bottle Retail Price to equal Bottle Profit Margin
  
df['Bottle_Profit_Margin'] = Bottle_Profit_Margin

df

#drops numbered rows 5 upto 15
df.drop(df.index[5:15], inplace = True)

df[:15]

#displays table where ml is greater than 750 and pack is greater than 12 and profit margin is greater than .3
df[(df['Bottle_Volume_ml'] > 750) & (df['Pack'] > 12) & (df['Bottle_Profit_Margin'] > .3)]

#prints the total number of rows where "Energy Drink" is the category of the tuple
print("The number of energy drinks: ")
len(df[df['Category'] == 'Energy Drink'])

#creating new Data Frame with 4 columns specified in project requirements

for index in df:
  items2 = df[['Item_id','Item_Description', 'Bottle_Retail_Price', 'Bottle_Profit_Margin']].copy()

items2

items2['QTY'] = np.random.randint(100, size = len(items2.index))

items2