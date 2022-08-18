#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 12:17:35 2022

@author: samanthasheely
"""

import pandas as pd

# file_name=pd.read_csv('file.csv')
data=pd.read_csv('transaction.csv')
data=pd.read_csv('transaction.csv',sep=';')

# summary of data
data.info()

#playing around with variables

#var=range(10) range
#var=range() range
#var={'name':'Dee','location':'South Africa'}  dictionary
#var={'apple','pear','banana'} set
#var=True

#working with calculations

#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem
CostPerTransaction = CostPerItem * NumberofItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberofItemsPurchased

#CostPerTransaction Column Calculation
#CostPerTransaction = CostPerItem * NumberofItemsPurchased
# variabe = datframe['column_name']

CostPeritem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPeritem * NumberofItemsPurchased

#Adding new column to dataframe

data['CostPerTransaction'] = CostPerTransaction

#sales per transaction

data['SalesPerTransaction'] = data['SellingPricePerItem']* data['NumberOfItemsPurchased']

#profit calculation= sales-cost

data['ProfitPertransaction']= data['SalesPerTransaction'] - data['CostPerTransaction']

#markup = (Sales - Cost)/Cost

data['Markup'] = data['ProfitPertransaction']/data['CostPerTransaction']

#Rounding Markup

Roundmarkup = round(data['Markup'],2)
data['Markup'] = round(data['Markup'],2)

#combining dat fields

my_name = 'Jamin' +'Jama'
my_date = 'Day' + '-' + 'Month' + '-' + 'Year'
#my-date = data['Day'] + '-'

#checking columns data type
print(data['Day'].dtype)

#change columns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date= day+'-'+data['Month']+'-'+year
data['my_date']=my_date

#using ilot to view specific clolumns
data.iloc[0] #views the row with index=0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] # brings in all rows on the second colum

data.iloc[4,2] #brings in 4th row, 2nd column

#Using split to split the client keywords field
#new_var = column.str.split('sep', expand=True)

split_col=data['ClientKeywords'].str.split(',',expand=True)

#Creating new columns for the split columns in client keywords

data['ClientAge']= split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#Using the replace function
data['ClientAge']=data['ClientAge'].str.replace('[','')
data['LengthofContract']=data['LengthofContract'].str.replace(']','')

#using the lower function to change item to lowercase

data['ItemDescription']=data['ItemDescription'].str.lower()

#how to merge files
#Bringing in a new data set

seasons=pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df= pd.merge(df_old,df_new,on='key')

data=pd.merge(data,seasons,on='Month')

#dropping columns

# df= df.drop('columnname',axis=1)

data=data.drop('ClientKeywords',axis=1)
data=data.drop('Day', axis=1)
data=data.drop(['Year','Month'],axis=1)

#Export into CSV

data.to_csv('ValueInc_Cleaned.csv',index=False)