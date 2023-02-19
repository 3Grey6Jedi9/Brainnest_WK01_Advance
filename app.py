import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import requests
import json
from datetime import datetime
from key import my_weather_key


#Creating the GUI window
root = tk.Tk()
root.title("Weather App")
root.geometry("1000x1000")



# Creating the labels for the weather data and forecast

location_label = Label(root, text="Location")
location_label.pack()
weather_label = Label(root, text="Weather")
weather_label.pack()
temperature_label = Label(root, text="Temperature")
temperature_label.pack()
humidity_label = Label(root, text="Humidity")
humidity_label.pack()
wind_label = Label(root, text="Wind Speed")
wind_label.pack()
forecast_label = Label(root, text="Forecast")
forecast_label.pack()


#Making the API call to OpenWeatherMap

api_key = my_weather_key
city_name = input('Please enter the city name: ')
#city_name = 'Rome'
country_code = input('Please enter the country code: ')
#country_code = 'IT'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}'
res = requests.get(url)
data = res.json()
print(data)


# Parse the JSON data and update the labels with the weather data


location = data['coord']
weather = data['weather'][0]['main'] + ' ' + data['weather'][0]['description']
temperature = data['main']







root.mainloop()