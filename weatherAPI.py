import datetime as dt
import requests

#BASE_URL="http://api.openweathermap.org/data/2.5/weather?q="
#API_KEY=open('API_KEYS.txt','r').read()
BASE_URL="http://api.agromonitoring.com/agro/1.0/soil?polyid="
API_KEY="073be33fabb2df527e16f3fa35b9e6b8"
CITY='Bengaluru'
COUNTRY='india'
POLYID='67f03fcbc46b9f5e57dfbf0e'

#http://api.agromonitoring.com/agro/1.0/soil?polyid=67f03fcbc46b9f5e57dfbf0e&appid=073be33fabb2df527e16f3fa35b9e6b8&units=metric
#http://api.agromonitoring.com/agro/1.0/soil?polyid=5aaa8052cbbbb5000b73ff66&appid=bb0664ed43c153aa072c760594d775a7
soil=BASE_URL+POLYID+'&appid='+API_KEY
#url=BASE_URL+CITY+','+COUNTRY+'&APPID='+API_KEY+'&units=metric'

response=requests.get(soil).json()

tempK=response['t0']
moisture=response['moisture']
def inToCelcius(temp):
    ans=temp-273.15
    return ans
def moisturePercent(moisture):
    return moisture*100
print(f"{inToCelcius(tempK):.8f}")
print(f"{moisturePercent(moisture):.8f}")
#temp=response['main']['temp']
#print(temp)

