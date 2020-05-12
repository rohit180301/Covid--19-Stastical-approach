import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

Age_group = pd.read_csv("Age Groups.csv")
Countries =  Age_group['Country'].values.tolist()
print("These are the countries where you can do your interships : ")
print(Countries)
print("The number of people died in the 20-29 age group in above countries are as follows : ")
age_grp_1 = Age_group['20-29'].values.tolist()
  
Countries_and_deaths_of_20_to_29 = {} 
for key in Countries: 
    for value in age_grp_1: 
        Countries_and_deaths_of_20_to_29[key] = value 
        age_grp_1.remove(value) 
        break  
print(Countries_and_deaths_of_20_to_29)

from heapq import nlargest   
N = int(input("Enter the number to get Top Countries in which people in the age group 20_29 have died : "))
Top_N_Countries = nlargest(N, Countries_and_deaths_of_20_to_29, key = Countries_and_deaths_of_20_to_29.get)  
print(f'Top {N} Countries in which people in the age group 20_29 have died are as follows :') 
print(str(Top_N_Countries))

countries_list = []
n = int(input("Enter the number of countries for which you have to see Age gaps of selected country vs No.of Deaths Graph : "))
print("Enter the name of countries for which you have to see Age gaps of country vs No.Deaths Graph :\n")
for i in range(1,n+1):
    country_names = str(input())
    countries_list.append(country_names)
print("Entered countries list by user : ")    
print(countries_list)

a1 = ['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80 and above']
for item in  countries_list:
     b=[]
     for i in range(0,len(Age_group)):          
        if Age_group.iloc[i][0]==item:
            b.extend(list(Age_group.iloc[i]))
            b.remove(item)
            plt.xlabel('Age gaps') 
            plt.ylabel('No. of Deaths')
            plt.plot(a1,b,color = 'green')
            plt.bar(a1,b, color ='Blue',width = 0.4) 
            plt.title(f"Age gaps of {Age_group.iloc[i][0]} vs No. of deaths",color = 'Red') 
            plt.show()
          
            
