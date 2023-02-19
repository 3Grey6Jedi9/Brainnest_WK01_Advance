d = {'coord': {'lon': 12.4839, 'lat': 41.8947}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds',
                                                             'icon': '04d'}],
     'base': 'stations',
     'main': {'temp': 288.47, 'feels_like': 287.91, 'temp_min': 286.66, 'temp_max': 289.48, 'pressure': 1025, 'humidity': 71},
     'visibility': 10000, 'wind': {'speed': 3.09, 'deg': 250}, 'clouds': {'all': 75}, 'dt': 1676809166,
     'sys': {'type': 2, 'id': 2037790, 'country': 'IT', 'sunrise': 1676786469, 'sunset': 1676825223},
     'timezone': 3600, 'id': 3169070, 'name': 'Rome', 'cod': 200}


location = d['coord']
weather = d['weather'][0]['main'] + '. ' + 'The have ' + d['weather'][0]['description']
temperature = str(round(d['main']['temp'] - 273.15, 2)) + 'ºC'
humidity = ''
wind_speed = ''

print(location, weather, temperature, humidity, wind_speed)

