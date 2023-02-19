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
print(res.json())


image = Image.open('rain.jpeg')

photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.pack()








root.mainloop()