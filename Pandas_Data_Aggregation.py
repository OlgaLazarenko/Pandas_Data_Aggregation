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
print(str(f"{auto_df['Make'].count():,d}") + '  cars were imported')
# What is the max price of an imported car?
print('$' + str(f"{auto_df['Price'].max():,d}") + ' . . .  max price of an imported car')
# What is the min price of an imported car?
print('$' + str(f"{auto_df['Price'].min():,d}") + ' . . . min price of an imported car')
# What is the average price of an imported car?
print('$' + str(f"{round(auto_df['Price'].mean()):,d}") + '. . . average price of an imported car')
# What is the total sale of the imported cars?
print('$' + str(f"{auto_df['Price'].sum():,d}") +  '  the total sale of the imported cars')
# show the number with commas as thousands separators f"{auto_df['Price'].sum():,d}"
print()

# show the summary of sales by the car make
print("Sales of the imported cars by the car make:")
print(auto_df.groupby('Make')['Price'].sum())
# OR 
auto_sales_make = auto_df.groupby('Make').agg(Sales = pd.NamedAgg(column = 'Price' , aggfunc = 'sum'))  # rename the summary column 
print(auto_sales_make) # display the new dataframe with summary on sales
# sort the sales summary dataframe by the column <Sales> at the descending order
auto_sales_make_sorted = auto_sales_make.sort_values( by = 'Sales' , ascending = False , inplace = False)
print()
print()
print("Sorted summary sales:")
print(auto_sales_make_sorted)
print()
print()



# Summaries with multiple columns <auto_df>
# calculate the sales by the car make and car body type
print("Imported cars, 1985")
auto_sales_make_style = auto_df.groupby(['Make','Body Style']).agg(Sales = pd.NamedAgg(column = 'Price' , aggfunc = 'sum'))
print(auto_sales_make_style)
print()
# calculate the sales by the car body type and the car make
auto_sales_style_make = auto_df.groupby(['Body Style','Make']).agg(Sales = pd.NamedAgg(column = 'Price' , aggfunc = 'sum'))
print(auto_sales_style_make)
# calculate the min, max miliage
print()
print()
print("Miliage:")
print(auto_df.groupby('Body Style').agg( city_min_mpg = ('City mpg', 'min') ,
                                        higway_min_mpg = ('Highway mpg' , 'min') , 
                                        city_max_mpg = ('City mpg' , 'max') ,
                                        higway_max_mpg = ('Highway mpg' , 'max') ,
                                        city_avg_mpg = ('City mpg' , 'mean') , 
                                        higway_avg_mpg = ('Highway mpg' , 'mean')
                                        
                                        )
    )   
print()
print("Mileage by style and make")
print(auto_df.groupby(['Body Style','Make']).agg( city_min_mpg = ('City mpg', 'min') ,
                                        higway_min_mpg = ('Highway mpg' , 'min') , 
                                        city_max_mpg = ('City mpg' , 'max') ,
                                        higway_max_mpg = ('Highway mpg' , 'max') ,
                                        city_avg_mpg = ('City mpg' , 'mean') , 
                                        higway_avg_mpg = ('Highway mpg' , 'mean')
                                                )
   )

print()
print('-------------------------------------------------------------------------')
print()
print('Briges data set:')
# how many briges were build?
print(str(brige_df['River'].count()) + '  briges were buidt')

print()
print('Types of erected briges:')
print(str(brige_df['Erected'].unique()))

print()
print('Purpose of the briges:')
print(str(brige_df['Purpose'].unique()))

print()
print('Lenght of the briges:')
print(brige_df['Length'].unique())

print()
print('Material of the briges:')
print(brige_df['Material'].unique())

print()
print('Type of the briges:')
print()


# *** Aggregations of brige_df dataframe with multiple columns
print('Aggregations of brige_df dataframe ')
print('-- Number of briges by the river:')
print(brige_df.groupby(['River','Erected']).Erected.count())

print()
print('-- Number of the erected briges by the purpose:')
print(brige_df.groupby(['Erected','Purpose']).Purpose.count())

print()
print('-- Number of briges by the purpose, the type and the material:')
print(brige_df.groupby(['Purpose','Type','Material']).Material.count())

print()
print('-- Number of briges by their purpose and material:')
print(brige_df.groupby(['Purpose','Material']).Material.count())
'''
['River' ,
                                    'Erected' ,
                                    'Purpose' ,
                                    'Length' ,
                                    'Material' ,
                                    'Type'])
'''