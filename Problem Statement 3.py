
#Please first install pip-packages

from win32com.client import Dispatch
import pandas as pd
import csv
lst=[]
lst1=[]
def speak(str):
    speak=Dispatch("SAPI.SPVoice")
    speak.Speak(str)


class change_country_state(object):
    def __init__(self,country_name,state):
        self.country_name=country_name
        self.state=state
    def finding_avg_no_of_days_for_country_to_change(self):
        df=pd.read_csv(open("C:\\Users\\Rohit Sagar Shinde\\Desktop\\time_series_covid19_deaths_global.csv",'r'))
        i=4
        i1=0
        while(self.country_name!=df.iloc[i1,1]):
            i1+=1
        # print(df.iloc[i1+1,1])
        while(df.iloc[i1,i]<1):
            i+=1
        speak(f"{i-4} number of average days are taken by {self.country_name} come to {self.state} state.")
        print(f"{i-4} number of average days are taken by {self.country_name} come to {self.state} state.")  
 

def country_took_the_maximum_number_of_days_to_death(state1):
        df=pd.read_csv(open(f"C:\\Users\\Rohit Sagar Shinde\\Desktop\\covid_19_{state1}.csv",'r'))
        lst=df['Country/Region']
        #j=1
        a=[]
        for item in range(0,262):
            a.append(change_country_state(lst[item],f"{state1}"))
            # print()
        for item in range(0,262):
            a[item].finding_avg_no_of_days_for_country_to_change()
        maxpos = lst1.index(max(lst1))
        print(lst(maxpos))  

speak("Hello everyone, this is COVID-19 visualisar. Please enter the country name that you want the information ")
c=1
while(c==1):
    country_name=(input("Please enter the country name that you want the information : ").capitalize())

    speak("Enter number of above states 1 or 2 to find out average number of days taken by country ")
    states=['death','recovered']

    p=0
    while(p==0):
        st=int(input("1.death\n2.recovered\nEnter number of above states 1 or 2 to find out average number of days taken by country : "))
    # print(country_name)
        if (st==1):
            # import time_series_covid_19_deaths
            df=pd.read_csv(open("C:\\Users\\Rohit Sagar Shinde\\Desktop\\time_series_covid19_deaths_global.csv",'r'))
            death=change_country_state(country_name,states[0])
            death.finding_avg_no_of_days_for_country_to_change()
        elif (st==2):
            # import time_series_covid_19_recovered
            df=pd.read_csv(open("C:\\Users\\Rohit Sagar Shinde\\Desktop\\time_series_covid19_deaths_global.csv",'r'))
            recover=change_country_state(country_name,states[1])
            recover.finding_avg_no_of_days_for_country_to_change()
        speak("press 0 to again loop into same country else press any number key to terminate the program : ")
        p=int(input("press 0 to again loop into same country else press any number key to terminate the program : "))
    
    speak("press 1 to loop into other country else press any key to terminate the program : ")
    c=int(input("press 1 to again loop into other country else press any number key to terminate the program : "))
 
# country_took_the_maximum_number_of_days_to_recover(can be given state[0]or state[1]as arguement)

           
   