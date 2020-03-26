import COVID19Py #This module is not used actually
import json
import urllib
import requests
import matplotlib.pyplot as plt

#Defining the api's for the nations required
URLIN="https://coronavirus-tracker-api.herokuapp.com/v2/locations/131"
URLIT="https://coronavirus-tracker-api.herokuapp.com/v2/locations/137"

def dilist(dates,cases):   #To convert date from recieved format to no. of days
	newdate=[]
	newcase=[]
	for i in dates:
		newdate.append(i[:10])
	for i in cases:
		newcase.append(i)
	return newdate,newcase

def date_convert(datelist,total_days_in):
	for x in datelist:
		month= int(x[5:7])
		day= int(x[8:10])
		if month==1:
			total_days_in.append(day)
		elif month==2:
			total_days_in.append(day+31)
		elif month==3:
			total_days_in.append(day+60)
		elif month==4:
			total_days_in.append(day+91)
	return total_days_in

response_in =requests.get(url = URLIN)
data_in = response_in.json()
response_it =requests.get(url = URLIT)
data_it = response_it.json()
#print(data['location']['timelines'].keys())
time_in = data_in['location']['timelines']['confirmed']['timeline']
time_it = data_it['location']['timelines']['confirmed']['timeline']
#print(times)
dates_in, cases_in=  time_in.keys(), time_in.values()
dates_it, cases_it=  time_it.keys(), time_it.values()

newdate_in,case_in= dilist(dates_in,cases_in)
newdate_it,case_it= dilist(dates_it,cases_it)

total_days_in=[]
total_days_it=[]

total_days_in=date_convert(newdate_in,total_days_in)
total_days_it=date_convert(newdate_it,total_days_it)
'''
print(total_days_in)
print(case_in)
print(total_days_it)
print(case_it)
'''
fig= plt.figure()
plt.plot(total_days_in,case_in,label='INDIA',color='g')
plt.plot(total_days_it,case_it,label='ITALY',color='r')
fig.suptitle('Corona Ind vs Ity',fontsize=20)
plt.xlabel('Days',fontsize=18)
plt.ylabel('Confirmed cases',fontsize=18)
plt.show()

