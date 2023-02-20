import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import requests
import json
from datetime import datetime
from key import my_weather_key
from tkinter import messagebox

DEFAULT_GAP = 60 * 25
DEFAULT_GAP = 5


class Weather():
    def __init__(self, master): #When I call the class the constructor gets executed
        self.master = master
        self.mainframe = tk.Frame(self.master, bg='white' )#It belongs to self.master (which is our root)
        self.mainframe.pack(fill=tk.BOTH, expand=True)

        self.timer_text = tk.StringVar()
        self.timer_text.trace('w',self.build_timer)
        self.timer_text.trace('w', self.alert)
        self.timer_left = tk.IntVar()
        self.timer_left.set(DEFAULT_GAP)
        self.running = False

        self.build_grid()
        self.build_banner()
        self.build_buttons()
        self.build_timer()

        self.update()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1) #We have one column (0) that has a weight of 1 resize proportinally to everything else
        self.mainframe.rowconfigure(0, weight=0) #weight 0 it won't resize
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)


    def build_banner(self):
        banner = tk.Label(self.mainframe, bg='blue', text='Current Weather', fg='white', font=('Arial', 21))
        banner.grid(row=0, column=0, sticky='ew',
                    padx=10, pady=10)


    def build_buttons(self):
        buttons_frame = tk.Frame(self.mainframe)
        buttons_frame.grid(row=2, column=0, sticky='nsew', pady=10, padx=10)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        self.start_button = tk.Button(buttons_frame, text='Start', command=self.start_timer)#I do not need the () because the function will run when I press the button
        self.stop_button = tk.Button(buttons_frame, text='Stop', command=self.stop_timer)

        self.start_button.grid(row=0, column=0, sticky='ew')
        self.stop_button.grid(row=0, column=1, sticky='ew')
        self.stop_button.config(state=tk.DISABLED)


    def build_timer(self, *args):
        timer = tk.Label(self.mainframe, text=self.timer_text.get(), font=('Arial', 36))
        timer.grid(row=1, column=0, sticky='nsew')


    def start_timer(self):
        self.timer_left.set(DEFAULT_GAP)
        self.running = True
        self.stop_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)


    def stop_timer(self):
        self.running = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

    def minutes_seconds(self, seconds):
        return  int(seconds/60), int(seconds%60)

    def alert(self, *args):
        if not self.timer_left.get():
            messagebox.showinfo('Timer done!', 'Your timer is done!')


    def update(self):
        time_left = self.timer_left.get()
        if self.running and time_left:
            minutes, seconds = self.minutes_seconds(time_left)
            self.timer_text.set('{:0>2}:{:0>2}'.format(minutes, seconds))
            self.timer_left.set(time_left-1)
        else:
            minutes, seconds = self.minutes_seconds(DEFAULT_GAP)
            self.timer_text.set('{:0>2}:{:0>2}'.format(minutes, seconds))
            self.stop_timer()

        self.master.after(1000, self.update)





if __name__ == '__main__':
    root = tk.Tk()
    Weather(root)
    root.mainloop()