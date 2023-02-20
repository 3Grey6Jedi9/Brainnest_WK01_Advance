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

        self.weather_info_button = tk.Button(buttons_frame, text='Weather Info')

        self.weather_info_button.grid(row=9, column=1, sticky='ew')

    def build_labels(self):
        pass






if __name__=='__main__':
    root = tk.Tk()
    Weather(root)
    root.mainloop()

