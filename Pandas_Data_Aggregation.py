# Pandas Data Aggregation
#!/bin/python3

import matplotlib.pyplot as plt
import pandas as pd

print()

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
print(auto_df.tail(10))
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
print(brige_df.tail(10))