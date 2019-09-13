import json, requests
import pprintpp as pprint
url_WOEID = 'https://www.metaweather.com/api/location/search/?query=bangalore'
response = requests.get(url_WOEID)
response.raise_for_status() 
woeid_data = json.loads(response.text)
pprint.pprint(woeid_data)
woeid = woeid_data[0]['woeid']
print(woeid)

url = ('https://www.metaweather.com/api/location/%s/' % (woeid))
request = requests.get(url)
request.raise_for_status()
    
weatherData = json.loads(request.text)

w = weatherData['consolidated_weather']

for i in range(len(w)):
    
    print("weather in Bangalore is: as on {} \n " .format(w[i]['applicable_date'])+ w[i]['weather_state_name'])

#Manual entry due to 