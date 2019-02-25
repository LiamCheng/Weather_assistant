import tkinter as tk
from tkinter import ttk
from function import gettime
from getweather import all_location,weatherinfo
import time

window = tk.Tk()
window.title('Your google assistant')
window.geometry('420x200')

#==========================================
def clock():
    timer= time.strftime("%b %d, %Y \n %H:%M:%S")
    time_label.configure(text=timer)
    window.after(1000, clock)

time_label = tk.Label(window, text="", font=("Arial", 14))
time_label.place(x='35',y='20')
clock()

btn_time = tk.Button(window, text='告訴我時間?', command=gettime, font=('Arial', 14))
btn_time.place(x='30',y='70')

#===============================================
label_weather = tk.Label(window,text = "選擇你的所在地")
label_weather.place(x='230',y='20')
all_location=all_location()
weather = ttk.Combobox(window,values=list(all_location.values()))
weather.place(x='230',y='40')
weather.current(17)
btn_weather = tk.Button(window, text='告訴我天氣?', command= lambda:weatherinfo(weather.get(),all_location), font=('Arial', 14))
btn_weather.place(x='230',y='70')
#=================================================

window.mainloop()