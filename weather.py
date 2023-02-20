import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import requests
import json
from datetime import datetime, timedelta
from key import my_weather_key
import webbrowser

class Weather():

    def __init__(self, master):
        self.master = master
        self.mainframe = tk.Frame(self.master, bg='white')
        self.mainframe.pack(fill=tk.BOTH, expand=True)
        self.master.title('Weather App')

        self.build_grid()
        self.build_buttons()
        self.build_labels()

        self.input_city = Entry(self.mainframe)
        self.input_city.grid(row=0, column=2)
        self.input_country = Entry(self.mainframe)
        self.input_country.grid(row=1, column=2)
        self.input_forecast = Entry(self.mainframe)
        self.input_forecast.grid(row=10, column=3)


    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.columnconfigure(1, weight=1)
        self.mainframe.columnconfigure(2, weight=1)
        self.mainframe.columnconfigure(3, weight=1)
        # Adding the rows
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=1)
        self.mainframe.rowconfigure(3, weight=1)
        self.mainframe.rowconfigure(4, weight=1)
        self.mainframe.rowconfigure(5, weight=1)
        self.mainframe.rowconfigure(6, weight=1)
        self.mainframe.rowconfigure(7, weight=1)
        self.mainframe.rowconfigure(8, weight=1)
        self.mainframe.rowconfigure(9, weight=1)
        self.mainframe.rowconfigure(10, weight=1)


    def build_buttons(self):

        self.weather_info_button = tk.Button(self.mainframe, text='Current Weather Info', command=self.request_info)
        self.weather_info_button.grid(row=10, column=1, sticky='nsew', pady=10, padx=10)

        self.country_codes_info_button = tk.Button(self.mainframe, text='Country Codes Info', command=self.info)
        self.country_codes_info_button.grid(row=1, column=3, sticky='nsew', pady=10, padx=10)

        self.weather_forecast_button = tk.Button(self.mainframe, text='Forecast', command=self.forecast)
        self.weather_forecast_button.grid(row=10, column=2, sticky='nsew', pady=10, padx=10)


    def build_labels(self):
        city_label = Label(self.mainframe, text='City:', font=('Arial', 21), bg='blue', fg='white')
        city_label.grid(row=0, column=1, sticky='ew')
        country_label = Label(self.mainframe, text='Country:', font=('Arial', 21), bg='green', fg='white')
        country_label.grid(row=1, column=1, sticky='ew')
        location_label = Label(self.mainframe, text='Location:', font=('Arial', 21), bg='blue', fg='white')
        location_label.grid(row=3, column=1, sticky='ew')
        weather_label = Label(self.mainframe, text='Weather:', font=('Arial', 21), bg='blue', fg='white')
        weather_label.grid(row=4, column=1, sticky='ew')
        temperature_label = Label(self.mainframe, text='Temperature:', font=('Arial', 21), bg='blue', fg='white')
        temperature_label.grid(row=5, column=1, sticky='ew')
        wind_label = Label(self.mainframe, text='Wind Speed:', font=('Arial', 21), bg='blue', fg='white')
        wind_label.grid(row=6, column=1, sticky='ew')
        humidity_label = Label(self.mainframe, text='Humidity:', font=('Arial', 21), bg='blue', fg='white')
        humidity_label.grid(row=7, column=1, sticky='ew')
        date_label = Label(self.mainframe, text='Local Time:', font=('Arial', 21), bg='blue', fg='white')
        date_label.grid(row=9, column=1, sticky='ew')
        forecast_label = Label(self.mainframe, text='''Forecast
    (3 - 120 hours)''', font=('Arial', 21), bg='blue', fg='white')
        forecast_label.grid(row=9, column=3, sticky='ew')





    def request_info(self):
        #Making the API request

        api_key = my_weather_key
        city_name = self.input_city.get()
        country_code = self.input_country.get()
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}'
        res = requests.get(url)
        data = res.json()
        print(data)

        #Displaying the data

        location_text = Text(self.mainframe, height=2, width=20)
        location = 'Longitude: ' + str(data['coord']['lon']) + '  Latitude: ' + str(data['coord']['lat'])
        location_text.insert(END, location)
        location_text.grid(row=3, column=2, sticky='ew')

        weather_text = Text(self.mainframe, height=2, width=20)
        weather = str(data['weather'][0]['main']) + ' ' + '(' + data['weather'][0]['description'] + ')'
        weather_text.insert(END, weather)
        weather_text.grid(row=4, column=2, sticky='ew')

        temperature_text = Text(self.mainframe, height=2, width=20)
        temperature = str(round(data['main']['temp'] - 273.15,2)) + 'ºC'
        temperature_text.insert(END, temperature)
        temperature_text.grid(row=5, column=2, sticky='ew')

        wind_text = Text(self.mainframe, height=2, width=20)
        wind_speed = str(data['wind']['speed']) + ' meters per second'
        wind_text.insert(END, wind_speed)
        wind_text.grid(row=6, column=2, sticky='ew')

        humidity_text = Text(self.mainframe, height=2, width=20)
        humidity = str(data['main']['humidity']) + ' grams of water vapor per cubic meter of air'
        humidity_text.insert(END, humidity)
        humidity_text.grid(row=7, column=2, sticky='ew')

        date_text = Text(self.mainframe, height=2, width=20)
        tz_offset = timedelta(seconds=data['timezone'])
        utc_time = datetime.utcnow()
        local_time = utc_time + tz_offset
        date = local_time.strftime("%d/%m/%Y %H:%M:%S")
        date_text.insert(END, date)
        date_text.grid(row=9, column=2, sticky='ew')


    def info(self):
        url = "https://www.iso.org/obp/ui/#search"
        webbrowser.open_new_tab(url)


    def forecast(self):
        #Making the API request

        api_key = my_weather_key
        city_name = self.input_city.get()
        country_code = self.input_country.get()
        forecast_hours = int(self.input_forecast.get())
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}'
        f_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name},{country_code}&appid={api_key}'
        res = requests.get(url)
        f_res = requests.get(f_url)
        data = res.json()
        f_data_gross = f_res.json()
        index = forecast_hours // 3
        f_data = f_data_gross['list'][index]



        # Displaying the data

        location_text = Text(self.mainframe, height=2, width=20)
        location = 'Longitude: ' + str(data['coord']['lon']) + '  Latitude: ' + str(data['coord']['lat'])
        location_text.insert(END, location)
        location_text.grid(row=3, column=2, sticky='ew')

        weather_text = Text(self.mainframe, height=2, width=20)
        weather = str(f_data['weather'][0]['main']) + ' ' + '(' + f_data['weather'][0]['description'] + ')'
        weather_text.insert(END, weather)
        weather_text.grid(row=4, column=2, sticky='ew')

        temperature_text = Text(self.mainframe, height=2, width=20)
        temperature = str(round(f_data['main']['temp'] - 273.15, 2)) + 'ºC'
        temperature_text.insert(END, temperature)
        temperature_text.grid(row=5, column=2, sticky='ew')

        wind_text = Text(self.mainframe, height=2, width=20)
        wind_speed = str(f_data['wind']['speed']) + ' meters per second'
        wind_text.insert(END, wind_speed)
        wind_text.grid(row=6, column=2, sticky='ew')

        humidity_text = Text(self.mainframe, height=2, width=20)
        humidity = str(f_data['main']['humidity']) + ' grams of water vapor per cubic meter of air'
        humidity_text.insert(END, humidity)
        humidity_text.grid(row=7, column=2, sticky='ew')

        date_text = Text(self.mainframe, height=2, width=20)
        tz_offset = timedelta(seconds=data['timezone'])
        utc_time = datetime.utcnow()
        local_time = utc_time + tz_offset
        date = local_time.strftime("%d/%m/%Y %H:%M:%S")
        date_text.insert(END, date)
        date_text.grid(row=9, column=2, sticky='ew')


if __name__=='__main__':
    root = tk.Tk()
    Weather(root)
    root.mainloop()
