# Pandas Data Aggregation
#!/bin/python3

import matplotlib.pyplot as plt
import pandas as pd

print()

auto = pd.read_csv('E:\_Python_Projects_Data\Data_Visualization\Autos_Data_Set\Autos_Import_1985.csv' ,
                        usecols = [ 'Symboling' ,
                                    'Make' ,
                                    'Body Style' , 
                                    'City mpg' ,
                                    'Highway mpg',  
                                    'Price']
                        )
# print the first 5 rows of the file
print(auto.head())
print()
print(auto.tail(10))