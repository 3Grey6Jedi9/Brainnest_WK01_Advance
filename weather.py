import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import requests
import json
from datetime import datetime
from key import my_weather_key

class Weather():

    def __init__(self, master):
        self.master = master
        self.mainframe = tk.Frame(self.master, bg='white')
        self.mainframe.pack(fill=tk.BOTH, expand=True)
        self.master.title('Weather App')

        self.build_grid()
        self.build_buttons()
        self.build_labels()
        self.request_info()


    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.columnconfigure(1, weight=1)
        self.mainframe.columnconfigure(2, weight=1)
        self.mainframe.columnconfigure(3, weight=1)
        # Adding the rows
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=1)
        self.mainframe.rowconfigure(3, weight=1)
        self.mainframe.rowconfigure(4, weight=1)
        self.mainframe.rowconfigure(5, weight=1)
        self.mainframe.rowconfigure(6, weight=1)
        self.mainframe.rowconfigure(7, weight=1)
        self.mainframe.rowconfigure(8, weight=1)
        self.mainframe.rowconfigure(9, weight=0)


    def build_buttons(self):
        buttons_frame = tk.Frame(self.mainframe)
        buttons_frame.grid(row=9, column=1, sticky='nsew', pady=10, padx=10)
        buttons_frame.columnconfigure(1, weight=1)

        self.weather_info_button = tk.Button(buttons_frame, text='Weather Info', command=self.request_info)

        self.weather_info_button.grid(row=9, column=1, sticky='ew')

    def build_labels(self):
        city_label = Label(self.mainframe, text='City:', font=('Arial', 21), bg='blue', fg='white')
        city_label.grid(row=0, column=1, sticky='ew')
        country_label = Label(self.mainframe, text='Country:', font=('Arial', 21), bg='green', fg='white')
        country_label.grid(row=1, column=1, sticky='ew')
        location_label = Label(self.mainframe, text='Location:', font=('Arial', 21), bg='blue', fg='white')
        location_label.grid(row=3, column=1, sticky='ew')
        temperature_label = Label(self.mainframe, text='Temperature:', font=('Arial', 21), bg='blue', fg='white')
        temperature_label.grid(row=4, column=1, sticky='ew')
        wind_label = Label(self.mainframe, text='Wind Speed:', font=('Arial', 21), bg='blue', fg='white')
        wind_label.grid(row=5, column=1, sticky='ew')
        humidity_label = Label(self.mainframe, text='Humidity:', font=('Arial', 21), bg='blue', fg='white')
        humidity_label.grid(row=6, column=1, sticky='ew')
        date_label = Label(self.mainframe, text='Date:', font=('Arial', 21), bg='blue', fg='white')
        date_label.grid(row=8, column=1, sticky='ew')


    def request_info(self):
        pass







if __name__=='__main__':
    root = tk.Tk()
    Weather(root)
    root.mainloop()

