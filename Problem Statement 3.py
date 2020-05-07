#Please first install pip-packages

from win32com.client import Dispatch
import pandas as pd
import csv
lst=[]
lst1=[]
def speak(str):
    speak=Dispatch("SAPI.SPVoice")
    speak.Speak(str)
    
class change_country_death_state(object):
    def __init__(self,country_name,death_state):
        self.country_name=country_name
        self.death_state=death_state

    def finding_avg_no_of_days_for_country_to_change(self):
        confirmed = pd.read_csv("C:\\Users\\Rohit Sagar Shinde\\Desktop\\time_series_covid19_confirmed_global.csv")
        deaths = pd.read_csv("C:\\Users\\Rohit Sagar Shinde\\Desktop\\time_series_covid19_deaths_global.csv")
        i=4
        k=4
        i1=0
        i3=0
        D=0
        while(self.country_name!=confirmed.iloc[i1,1]):
            i1+=1
        while(self.country_name!=deaths.iloc[i3,1]):
            i3+=1    
        while(confirmed.iloc[i1,i]<1):
            i+=1
        while(deaths.iloc[i3,k]<1):
            k+=1  
        D = k-i  
        speak(f"{D} number of average days are taken by {self.country_name} come to {self.death_state} state.")
        print(f"{D} number of average days are taken by {self.country_name} come to {self.death_state} state.") 

class change_country_recovered_state(object):
    def __init__(self,country_name,recovered_state):
        self.country_name=country_name
        self.recovered_state=recovered_state
    def finding_avg_no_of_days_for_country_to_change(self):
        confirmed = pd.read_csv("C:\\Users\\Rohit Sagar Shinde\\Desktop\\time_series_covid19_confirmed_global.csv")
        recovered = pd.read_csv("C:\\Users\\Rohit Sagar Shinde\\Desktop\\time_series_covid19_recovered_global.csv")
        i=4
        j=4
        i1=0
        i2=0
        R=0
        while(self.country_name!=confirmed.iloc[i1,1]):
            i1+=1
        while(self.country_name!=recovered.iloc[i2,1]):
            i2+=1
        while(confirmed.iloc[i1,i]<1):
            i+=1
        while(recovered.iloc[i2,j]<1):
            j+=1    
        R = j-i   
        speak(f"{R} number of average days are taken by {self.country_name} come to {self.recovered_state} state.")
        print(f"{R} number of average days are taken by {self.country_name} come to {self.recovered_state} state.")   
 
speak("Hello everyone, this is COVID-19 visualisar. Please enter the country name that you want the information ")
c=1
while(c==1):
    country_name=(input("Please enter the country name that you want the information : ").capitalize())
    speak("Enter number of above states 1 or 2 to find out average number of days taken by country ")
    states=['death','recovered']
    p=0
    while(p==0):
        st=int(input("1.death\n2.recovered\nEnter number of above states 1 or 2 to find out average number of days taken by country : "))
        if (st==1):
            death=change_country_death_state(country_name,states[0])
            death.finding_avg_no_of_days_for_country_to_change()
        elif (st==2):
            recover=change_country_recovered_state(country_name,states[1])
            recover.finding_avg_no_of_days_for_country_to_change()
        speak("Press 0 to again loop into same country else press any number key to terminate the program : ")
        p=int(input("Press 0 to again loop into same country else press any number key to terminate the program : "))
    speak("Press 1 to loop into other country else press any key to terminate the program : ")
    c=int(input("Press 1 to again loop into other country else press any number key to terminate the program : "))
 


           
   