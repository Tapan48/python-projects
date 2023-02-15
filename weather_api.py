import datetime

import requests



base_url = "https://api.openweathermap.org/data/2.5/weather?"
apikey="f94a9153399480ab3247e00aee61cb19"
city="Hubli"


url = base_url +"appid=" + apikey +"&q="+city


response = requests.get(url).json()

print(response)



def tempconverter(kelvintemp):
    
    celsius=kelvintemp-273.15
    
    fahren=(kelvintemp-273.15)*(9/5) +32
    
    
    return celsius,fahren
    
    


temp_celsius,temp_fahrenheit=tempconverter(response['main']['temp'])
mintempc,mintempf=tempconverter(response['main']['temp_min'])
maxtempc,maxtempf=tempconverter(response['main']['temp_max'])
windspeed=response['wind']['speed']

humidity=response['main']['humidity']
pressure=response['main']['pressure']


cloud_descrptn=response['weather'][0]['description']




print(f"the temperature in {city} is {temp_celsius} degree or {temp_fahrenheit} fahrenheit")

print(f"the minimum temperature in {city} is {mintempc} degree or {mintempf} fahrenheit")

print(f"the maximum temperature in {city} is {maxtempc} degree or {maxtempf} fahrenheit")
print(f"the windspeed in {city}is {windspeed}")


print(f"the humidity in {city}is {humidity}%")

print(f"the pressure in {city}is {pressure}")

print(f"the cloud  description in {city}is {cloud_descrptn}")













