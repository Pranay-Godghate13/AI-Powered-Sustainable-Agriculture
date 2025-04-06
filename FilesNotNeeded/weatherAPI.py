import datetime as dt
import requests

#BASE_URL="http://api.openweathermap.org/data/2.5/weather?q="
#API_KEY=open('API_KEYS.txt','r').read()

API_KEY="073be33fabb2df527e16f3fa35b9e6b8"
# FUNCTION TO GET POLYGON ID
###############################################################################
# Define new data to create
new_data = {
   "name":"Polygon1",
   "geo_json":{
      "type":"Feature",
      "properties":{

      },
      "geometry":{
         "type":"Polygon",
         "coordinates":[
            [
               [12.9655,77.5854],  
               [12.9745,77.5854],  
               [12.9745,77.5946],  
               [12.9655,77.5946],  
               [12.9655,77.5854]  
            ]
         ]
      }
   }
}
post_response_json =""
count=1
def createPolygon():
    # The API endpoint to communicate with
    url_post = "http://api.agromonitoring.com/agro/1.0/polygons?appid="+API_KEY
    # A POST request to tthe API
    
    post_response = requests.post(url_post, json=new_data)
    # Print the response
    return post_response.json()

post_response_json=createPolygon()
print(post_response_json)

#######################################################################################

BASE_URL="http://api.agromonitoring.com/agro/1.0/soil?polyid="

CITY='Bengaluru'
COUNTRY='india'
POLYID='67f05ce7e21a808a41a46699'
CENTRE=[12.97, 77.59]
#POST coordinates to get POLYID and coordinates



#http://api.agromonitoring.com/agro/1.0/soil?polyid=67f03fcbc46b9f5e57dfbf0e&appid=073be33fabb2df527e16f3fa35b9e6b8&units=metric
#http://api.agromonitoring.com/agro/1.0/soil?polyid=5aaa8052cbbbb5000b73ff66&appid=bb0664ed43c153aa072c760594d775a7


####################################################################################################
#SOIL URL
soil=BASE_URL+POLYID+'&appid='+API_KEY
#RAINFALL PREDICTION BASED ON LAST YEAR DATA

#url=BASE_URL+CITY+','+COUNTRY+'&APPID='+API_KEY+'&units=metric'



response=requests.get(soil).json()
print(response)
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

#######################################################
#CONVERT TO UNIX DATE & TIME
from datetime import datetime, timezone

# Input: Date string in local time
date_str = '2024-04-01 05:00:00'
date_end='2024-07-30 05:00:00'
# Parse and set it as UTC time
dt1 = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
dt2 = datetime.strptime(date_end, '%Y-%m-%d %H:%M:%S')
dt_utc1 = dt1.replace(tzinfo=timezone.utc)
dt_utc2 = dt2.replace(tzinfo=timezone.utc)

# Convert to Unix timestamp
timestamp1 = int(dt_utc1.timestamp())
timestamp2 = int(dt_utc2.timestamp())

print("Unix Timestamp (UTC):", timestamp1)
print("Unix Timestamp (UTC):", timestamp2)


##################################################################################################
#PRECIPITATION ACCUMULATOR INDICATOR

# rain_url="https://api.agromonitoring.com/agro/1.0/weather/history/accumulated_precipitation?lat=12&lon=77&start=1517502031&end=1519834831&appid=9d82f7c9ddf58e156f11c9cc2d1bb350"
# rain=requests.get(rain_url).json()
# print(rain)

# API="073be33fabb2df527e16f3fa35b9e6b8"

# temp_url="https://api.agromonitoring.com/agro/1.0/weather/history/accumulated_temperature?lat=35&lon=139&threshold=284&start=1517502031&end=1519834831&appid="+API
# temp=requests.get(temp_url).json()
# print(temp)
# KEY="FURGQ7QSA4UGU8KEWP3AB6MJ5"
# url="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Bengaluru,India/last30days?key="+KEY

# rain_x=requests.get(url).json()
# #print(rain_x['currentConditions']['precip'])
# print(rain_x)

KEY="2aeeab3a732349ce888235518250404"
url="https://api.weatherapi.com/v1/forecast.json?q=12.97%2C%2077.59&days=14&key="+KEY
forecasted_rain=requests.get(url).json()
print(f"Temperature in  C: {forecasted_rain["forecast"]["forecastday"][0]["day"]["avgtemp_c"]}")
print(forecasted_rain["forecast"]["forecastday"][0]["day"]["totalprecip_mm"])

sum=0
for x in forecasted_rain["forecast"]["forecastday"][0]["hour"]:
    sum+=x['precip_mm']
print(sum*2)
