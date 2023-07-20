from django.shortcuts import render
import requests
from decouple import config

# Create your views here.
def main(request):
    context = {}
    city = request.GET.get('user-input')
    try:
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={config('API_ID')}"
        json_data = requests.get(api).json()
        context['condition'] = json_data['weather'][0]['main']
    except KeyError:
        context['error'] = 'Please enter a valid city name!'
    else:
        context['detailed_condition'] = json_data['weather'][0]['description']
        context['temperature'] = int(json_data['main']['temp'] - 273.15)
        context['min_temp'] = int(json_data['main']['temp_min'] - 273.15)
        context['max_temp'] = int(json_data['main']['temp_max'] - 273.15)
        context['pressure'] = json_data['main']['pressure']
        context['humidity'] = json_data['main']['humidity']
        context['wind'] = json_data['wind']['speed']
        if context['condition'] == 'Clear':
            context['icon'] = 'my_weather_app/figs/clear.png'
        elif context['condition'] == 'Clouds':
            context['icon'] = 'my_weather_app/figs/clouds.png'
        elif context['condition'] == 'Snow':
            context['icon'] = 'my_weather_app/figs/snow.png'
        elif context['condition'] == 'Thunderstorm':
            context['icon'] = 'my_weather_app/figs/thunderstorm.png'
        elif context['condition'] == 'Rain':
            context['icon'] = 'my_weather_app/figs/rain.png'
        elif context['condition'] == 'Drizzle':
            context['icon'] = 'my_weather_app/figs/drizzle.png'
        else:
            context['icon'] = 'my_weather_app/figs/mist.png'
    return render(request, 'my_weather_app/home.html', context)
