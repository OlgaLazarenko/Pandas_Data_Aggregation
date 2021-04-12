# Pandas Data Aggregation
#!/bin/python3

import matplotlib.pyplot as plt
import pandas as pd

print()
# *** 1)
# read the file into the dataframe <auto_df>
auto_df = pd.read_csv('E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Autos_Import_1985.csv' ,
                        usecols = [ 'Symboling' ,
                                    'Make' ,
                                    'Body Style' , 
                                    'City mpg' ,
                                    'Highway mpg',  
                                    'Price']
                        )
# print the first 5 rows of the file
print('Auto dataframe:')
print(auto_df.head())
print()


# read the file <Briges_1818_1986.csv> info <brige> dataframe
brige_df = pd.read_csv('E:\_Python_Projects_Data\Data_Visualization\Briges_Data_Set\Briges_1818_1986.csv' , 
                        usecols = ['River' ,
                                    'Erected' ,
                                    'Purpose' ,
                                    'Length' ,
                                    'Material' ,
                                    'Type'])

# print the first 5 rows of the file
print('Briges dataframe:')
print(brige_df.head())
print()

#--------------------------------------------------------------------

# *** 2) 
# check the basic information of the dataframes
print('--- auto_df  dataframe basic information:')
print(auto_df.info())
print()
print('--- brige_df  dataframe basic information:')
print(brige_df.info())
print()

# unique values of the dataframes
print('auto_df unique values:')
print('Symboling:')
print(auto_df['Symboling'].unique())
print()
print('Make:')
print(auto_df['Make'].unique())
print()
print('Body Style:')
print(auto_df['Body Style'].unique())
print()
print('* * * * * *')
print('brige_df unique values:')
print('River:')
print(brige_df['River'].unique())
print()
print('Erected:')
print(brige_df['Erected'].unique())
print()
print('Purpose:')
print(brige_df['Purpose'].unique())
print()
print('Length:')
print(brige_df['Length'].unique())
print()
print('Material:')
print(brige_df['Material'].unique())
print()
print('Type:')
print(brige_df['Type'].unique())
print()
#--------------------------------------------------------------------

# *** 3)
# *** Summarizing the DataFrames





# How many cars were imported at 1985? The DataFrame <auto_df>
print(str(auto_df['Make'].count()) + '  cars were imported at 1985')
print()
# How many briges were build? The DataFrame <brige_df>
print( str(brige_df['Material'].count()) + '  briges were built')
# What is the max price of an imported car?
print(str(auto_df['Price'].max()) + ' is the max price of an imported car')
# What is the min price of an imported car?