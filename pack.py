import requests
#import os
from datetime import datetime

api_key = '12f3fe0150a34c3e74ba3e458f6e0b7d'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
file = open("output.txt", "w")
l=str("\n-------------------------------------------------------------\n")
print(l)
file.write(str(l))
s="Weather Stats for - {}  || {}".format(location.upper(), date_time)
print(s)
file.write(str((s)))
file.write(l)
print (l)
m ="Current temperature is: {:.2f} deg C\n".format(temp_city)
print(m)
file.write(m)
o = ("Current Weather desc  :"+weather_desc+"\n")
print(o)
file.write(o)
p = ("Current Humidity      :"+str(hmdt)+'%\n')
print(p)
file.write(p)
q = ("Current Wind Speed    :"+str(wind_spd)+'kmph\n')
print(q)
file.write(q)
file.close()