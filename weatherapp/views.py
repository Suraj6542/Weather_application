from django.shortcuts import render
import requests

def home(request):
    city = request.GET.get('city')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=917ffedbd49db304875ac0d243550ecd'
    data = requests.get(url).json()
    print(data)
    payload = {
        'city': data['name'],
        'weather': data['weather'][0]['main'],
        'icon': data['weather'][0]['icon'],
        'Kelvin_temperature': int(data['main']['temp']),
        'Celcius_temperature': int(data['main']['temp'] - 273),
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description']
    }
    context = {'data' : payload}
    return render(request, 'home.html', context)

