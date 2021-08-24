# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 12:59:02 2021

@author: Ragnar Dzosua Builong Jónsson
"""

import pandas as pd

df = pd.read_csv('Fasteign_housing_list.csv')

# Fix address
Address_name = df['Address'].apply(lambda x: (x.split(' ')[0]))
Address_number = df['Address'].apply(lambda x: (x.split(' ')[1]))
df['Address'] = (Address_name + ' ' + Address_number).apply(lambda x: x.replace(',',''))

# If sold already
df['Sold'] = df['Address'].apply(lambda x: 1 if 'seld' in x.lower() else 0)
df['Address'] = df['Address'].apply(lambda x: x.replace('SELD',''))


# Address to Area Code and City
df['City'] = df['Postal Code'].apply(lambda x: x.split(' ')[1])
df['Postal Code'] = df['Postal Code'].apply(lambda x: x.split(' ')[0])

# Price number only / Tilboð -> Offer

df['Offer'] = df['Price'].apply(lambda x: 1 if 'tilboð' in x.lower() else 0)
df['Price'] = df['Price'].apply(lambda x: -1 if 'tilboð' in x.lower() else int((x.replace('kr','')).replace('.','')))

# size to float
df['Size m^2'] = df['Size m^2'].apply(lambda x: float(x.replace(',','.')))

# Kind to english
df['Kind'] = df['Kind'].apply(lambda x: x.replace('einbýlishús,','Single Family House'))
df['Kind'] = df['Kind'].apply(lambda x: x.replace('hæð,','Duplex'))
df['Kind'] = df['Kind'].apply(lambda x: x.replace('parhús,','Semi-Detached House'))
df['Kind'] = df['Kind'].apply(lambda x: x.replace('raðhús,','Terrace House'))
df['Kind'] = df['Kind'].apply(lambda x: x.replace('fjölbýlishús,','Flat'))


# Date of construction, get rid of unusable data
df['Date'] = df['Date'].apply(lambda x: -1 if 'herbergi' in x.lower() else int(x))

# Rooms, get rid of unusable data
df['Rooms'] = df['Rooms'].apply(lambda x: int(x) if (x.isnumeric() == True) else -1)

# Clean Description

df_out = df.drop(['Description'], axis = 1)
df_out.to_csv('Fasteign_Housing_list_Cleaned.csv', index = False)
#pd.read_csv('Fasteign_Housing_list_Cleaned.csv')
