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
# auto_df['Price'] = auto_df['Price'].astype(str).astype(int) # convert the values of the column <Price> to  the integer data type
print(auto_df.info())
# auto_df.dtypes()
print()
print('--- brige_df  dataframe basic information:')
print(brige_df.info())
print()

# remove nonvalid values <?>
auto_df = auto_df[auto_df['Price']  != '?'] # remove rows with <?> at the column <Price> from the data frame
brige_df = brige_df[brige_df['Length']  != '?'] # remove rows with <?> at the column <Price> from the data frame
brige_df = brige_df[brige_df['Material']  != '?']
brige_df = brige_df[brige_df['Type']  != '?']

# convert <Price> column of <auto_df> dataframe not integer data type
print()
print(auto_df.dtypes)
auto_df['Price'] = auto_df['Price'].astype(str).astype(int)
print(auto_df.dtypes)
print()
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
print('* * * * * *')
print()

#--------------------------------------------------------------------

# *** 3)
# *** Summarizing the DataFrames



# How many cars were imported at 1985? The DataFrame <auto_df>
print('Summarizing the DataFrames:')
print()
print(str(auto_df['Make'].count()) + '  cars were imported at 1985')
# What is the max price of an imported car?
print('$' + str(auto_df['Price'].max()) + ' . . .  max price of an imported car')
# What is the min price of an imported car?
print('$' + str(auto_df['Price'].min()) + ' . . . min price of an imported car')
# What is the average price of an imported car?
print('$' + str(round(auto_df['Price'].mean())) + '. . . average price of an imported car')
# What is the total sale of the imported cars?
print('$' + str(f"{auto_df['Price'].sum():,d}") +  '  the total sale of the imported cars')
# show the number with commas as thousands separators f"{auto_df['Price'].sum():,d}"
print()
# How many briges were build? The DataFrame <brige_df>

