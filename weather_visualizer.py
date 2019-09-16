import json, requests, re
#import pprintpp as pprint
import matplotlib.pyplot as plt 
url_WOEID = 'https://www.metaweather.com/api/location/search/?query=bangalore'
response = requests.get(url_WOEID)
response.raise_for_status() 
woeid_data = json.loads(response.text)
woeid = woeid_data[0]['woeid']

url = ('https://www.metaweather.com/api/location/%s/' % (woeid))
request = requests.get(url)
request.raise_for_status()
    
weatherData = json.loads(request.text)

w = weatherData['consolidated_weather']

#Lists to hold Speed vs dates & temprature data vs dates.
temprature = []
speed      = []
date       = []
for i in range(len(w)):
    
    print("weather in Bangalore is: as on {} \n " .format(w[i]['applicable_date'])+
     w[i]['weather_state_name'])

    temprature.append(w[i]['the_temp'])
    speed.append(w[i]['wind_speed'])
    
    #Regex to edit the date in 'month-day' format.
    DateRegex = re.compile(r'(\d\d\d\d)-(\d\d-\d\d)')
    day = DateRegex.search(w[i]['applicable_date'])
    
    date.append(day.group(2))


#Plotting the data 

#Temprature data plot
plt.scatter(date,temprature, s=200, label='x-axis = month-date\ny-axis = degree celsius')
plt.title("Days vs Temprature graph", c='indigo',fontsize=16)
plt.xlabel("dates",c='orange', fontsize=14)
plt.ylabel("temptarture",c='orange', fontsize=14)
plt.tick_params('both', which='major',labelsize=14)
plt.legend()

plt.show()

#Speed data plot
plt.scatter(date,speed,c='indigo', s=200)
plt.title("Days vs Wind Speed graph", c='blue',fontsize=16)
plt.xlabel("dates",c='orange', fontsize=14)
plt.ylabel("Wind Speed (km\hr)",c='orange', fontsize=14)
plt.tick_params('both', which='major',labelsize=14)

plt.show()





