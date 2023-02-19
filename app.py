import tkinter as tk
from tkinter import *

root = tk.Tk()

root.geometry("1000x1000")


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








root.mainloop()