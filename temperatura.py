from urllib import response
import requests 
response = requests.get("http://www.7timer.info/bin/civillight.php?lon=-58.37723&lat=-34.61315&ac=0&unit=metric&output=json")
temp=response.json()
print(temp['dataseries'][6]['date'])
print(temp['dataseries'][6]['temp2m']['max'])
print(temp['dataseries'][6]['temp2m']['min'])
