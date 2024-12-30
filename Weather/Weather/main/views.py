from django.shortcuts import render
import requests
from django.contrib import messages
# Create your views here.


def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else: 
        city="katmandu"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=32d819fcad1d78fe0fa1c5d0fb78c7b0"
    param={'units':'metric'}
    

    try:
        data=requests.get(url,param).json() #it convert into python dictionary

        temp=data['main']['temp']
        desc=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        humidity=data['main']['humidity']
        wind=data['wind']['speed']
        deg=data['wind']['deg']


        return render(request, 'index.html',{'temp':temp,'desc':desc,'icon':icon,'city':city,'humidity':humidity,'wind':wind,'deg':deg})
    except:
        data=requests.get(url,param).json() #it convert into python dictionary
        temp=0
        desc="there is no data"
        messages.error(request,"there is no such city name")
        

        return render(request, 'index.html',{'temp':temp,'desc':desc,'city':city})