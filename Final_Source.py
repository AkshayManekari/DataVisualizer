

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 20:34:50 2020

"""

import requests
import json
import pygal
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import webbrowser


win=tk.Tk()
win.title("Data visualizer")

win.resizable(False,False)

#Creation of tab control
tabControl=ttk.Notebook(win)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1,text="Visualizer")
tab2=ttk.Frame(tabControl)
tabControl.add(tab2,text="About")
tabControl.pack(expand=1,fill="both")

'''
#creating a labelframe for city1
mighty=ttk.LabelFrame(tab1,text="City1")
mighty.grid(column=0,row=0,padx=8,pady=4,sticky=tk.W)
'''
#creating a labelframe 
mighty=ttk.LabelFrame(tab1,text="Enter details below")
mighty.grid(column=0,row=0,padx=8,pady=4,sticky=tk.W)

#creating a label
u_label=ttk.Label(mighty,text="city1")
u_label.grid(column=0,sticky=tk.W,row=0)

#adding a text widget dor username
city1=tk.StringVar()
name_entered=ttk.Entry(mighty,width=12,textvariable=city1)
name_entered.grid(column=1,sticky=tk.W,row=0)

#creating a label
p_label=ttk.Label(mighty,text="city2")
p_label.grid(column=0,sticky=tk.W,row=1)

#adding a text widget for pass
city2=tk.StringVar()
number_entered=ttk.Entry(mighty,width=12,textvariable=city2)
number_entered.grid(column=1,sticky=tk.W,row=1)


def click_me():
    cityname1=city1.get()
    cityname2=city2.get()
	#Request for getting city searchkey
    req_searchkey=requests.get("http://dataservice.accuweather.com/locations/v1/cities/search",params={"apikey":"hu3frtlZoFypjjNAwDasnaprTUGBS3qT","q":"{}".format(cityname1)})
	#print(req_searchkey.text)


    data=json.loads(req_searchkey.text)
    a=list()
    for d in data:
        val=d['Key']
        a.append(val)
	 



    x=a[0]
    print(x) #city number
    #Request for 5 day forecast using city search key through
    req_forecast=requests.get("http://dataservice.accuweather.com/forecasts/v1/daily/5day/{}".format(x),params={"apikey":"7urUOlFBlJSNypCBljK5WbSDcYS0bxYW"})
    read_content=json.loads(req_forecast.text)
    #print(read_content)

    mini=list()
    maxi=list()
    date=list()

    def get_min():
        temp_access=read_content["DailyForecasts"]
        for data in temp_access:
            temp_data=data['Temperature']
            val=temp_data['Minimum']['Value']
            mini.append(val)
    def get_max():
        temp_access=read_content["DailyForecasts"]
        for data in temp_access:
            temp_data=data['Temperature']
            val=temp_data['Maximum']['Value']
            maxi.append(val)

    def get_date():
        temp_access=read_content["DailyForecasts"]
        for data in temp_access:
            val=data['Date']
            #mini=temp_data['Maximum']['Value']
            date.append(val)
	
    get_min()
    print("___________---------________")
    get_max()
    print("___________---------________")
    get_date()

    #min,max temperatures along with date is available in the lists
    #start plotting
    line_chart=pygal.Bar()
    line_chart.title="Weather Forecast of : {} in Fahrenheit".format(cityname1)
    line_chart.x_labels=map(str,date)
    line_chart.add('Minimum',mini)
    line_chart.add('Maximum',maxi)
    line_chart.render_to_file('Forecast1.svg')
    #action.configure(text="DOne")
    #Request for getting city searchkey
    req_searchkey=requests.get("http://dataservice.accuweather.com/locations/v1/cities/search",params={"apikey":"hu3frtlZoFypjjNAwDasnaprTUGBS3qT","q":"{}".format(cityname2)})
	#print(req_searchkey.text)


    data=json.loads(req_searchkey.text)
    a=list()
    for d in data:
        val=d['Key']
        a.append(val)
	 



    x=a[0]
    print(x) #city number
    #Request for 5 day forecast using city search key through
    req_forecast=requests.get("http://dataservice.accuweather.com/forecasts/v1/daily/5day/{}".format(x),params={"apikey":"7urUOlFBlJSNypCBljK5WbSDcYS0bxYW"})
    read_content=json.loads(req_forecast.text)
    #print(read_content)

    mini=list()
    maxi=list()
    date=list()

    get_min()
    print("___________---------________")
    get_max()
    print("___________---------________")
    get_date()

    #min,max temperatures along with date is available in the lists
    #start plotting
    line_chart=pygal.Bar()
    line_chart.title="Weather Forecast of : {} in Fahrenheit".format(cityname2)
    line_chart.x_labels=map(str,date)
    line_chart.add('Minimum',mini)
    line_chart.add('Maximum',maxi)
    line_chart.render_to_file('Forecast2.svg')
    action.configure(text="hello Plotting done")
    webbrowser.open("Forecast1.svg")
    webbrowser.open("Forecast2.svg")
    
    
    
	

#Generate button
#adding a button
action=ttk.Button(mighty,text='Forecast',command=click_me)
action.grid(column=0,row=3,padx=10)


#creating a label
#creating a label
p_label=ttk.Label(tab2,text="This is a weather forecaster;it produces beautiful SVG graphs.\n\n\n------------------------Created by ASM.-----------------------\n                                       For Convenience :)")
p_label.grid(column=0,sticky=tk.W,row=1)

win.mainloop()
