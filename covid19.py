'''
Description: This python code uses API to extracts realtime covid19 data of IND & ITY and then plots it using matplotlib library 

'''
import json
import urllib
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time


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
		days_in_month=[31,29,31,30,31,30,31,31,30,31,30,31]
		total_month=-30    #Because first case was reported on jan 31st 
		for thismonth in range(month-2):
			total_month+= days_in_month[thismonth]
		total_days_in.append(day+total_month)
	return total_days_in

response_in =requests.get(url = URLIN)
data_in = response_in.json()
response_it =requests.get(url = URLIT)
data_it = response_it.json()

#For printing data in terminal
india131= data_in['location']['latest']
italy137= data_it['location']['latest']

print("data of india-->",india131)
print("data of italy-->",italy137)

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
ax1 = plt.subplot2grid((1,1),(0,0))
ax2 = plt.subplot2grid((1,1),(0,0))
plt.plot(total_days_in,case_in,'-',label='INDIA',color='g')
plt.plot(total_days_it,case_it,'-',label='ITALY',color='r')
fig.suptitle('Corona India vs Italy',fontsize=20)
'''
for label in plt.xaxis.get_ticklabels():
	label.set_rotation(45)
'''
#common for all plots so kept at bottom
plt.xlabel('Days',fontsize=18,color='b')
plt.ylabel('Confirmed cases',fontsize=18,color='b')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.legend()
plt.subplots_adjust(left=0.15,bottom=0.13,right=0.99,top=0.90,wspace=0.2,hspace=0)
plt.show()
