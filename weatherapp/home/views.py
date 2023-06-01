from django.shortcuts import render
import requests
import json
# Create your views here.

def index(request):
    if request.method=='POST':
        city = request.POST['city']
      
    else:
        city = 'khandwa'
    url = f"https://api.weatherapi.com/v1/current.json?key=fae1515cb3c84e3dbf860745232505&q={city}"
    r = requests.get(url=url)
    res = r.json()
    print(city)
   
   
    location = res['location']['name']
    icon = res['current']['condition']['icon']
    temp = res['current']['temp_c']
    humidity = res['current']['humidity']
    time = res['location']['localtime']
    cloud = res['current']['cloud']

    return render(request, "index.html",{'temp':temp,'location':location,'time':time,'icon':icon
    ,'humidity':humidity,'cloud':cloud,})