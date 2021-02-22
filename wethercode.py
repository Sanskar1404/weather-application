import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q="+ city +"{Your API Key}" 
    # for api, go to - https://openweathermap.org/api  and subscribe on current weather, there you will get your api key
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] -273.15)
    min_temp = int(json_data['main']['temp_min'] -273.15)
    max_temp = int(json_data['main']['temp_max'] -273.15)
    feels_like = int(json_data['main']['feels_like'] -273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 19800))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] + 19800))
    visibility = json_data['visibility']
     


    final_info = condition + "\n" + str(temp) + "°C"
    final_dt =  "Feels Like: " + str(feels_like)+" °C"
    final_data = "\n" + "Max Temp: " + str(max_temp)+" °C" + "\n" + "Min Temp: " + str(min_temp)+" °C" + "\n"+ "Visibility: " + str(visibility/1000) + " km" "\n" + "Pressure: " + str(pressure) +" hpa"+ "\n" + "Humidity: " + str(humidity)+ " %" + "\n" + "Wind Speed: " + str(wind )+" km/h"  + "\n" + "Sunrise: " + sunrise+" am" + "\n" + "Sunset: " + sunset+" pm"
    label1.config(text = final_info)
    label2.config(text = final_dt)
    label3.config(text = final_data)



canvas = tk.Tk()
canvas.geometry("700x600")
canvas.title("Weather App")
canvas.configure(bg="sea green")

f = ("Times New Roman", 23, "bold")
t = ("Times New Roman", 27, "bold")
z = ("Times New Roman", 20, "bold")

textfield = tk.Entry(canvas,justify="center", bg="lime green", font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)


label1 = tk.Label(canvas,justify="center", bg="sea green" ,font = t)
label1.pack()
label2 = tk.Label(canvas,justify="center", bg="sea green",font = f)
label2.pack()
label3 = tk.Label(canvas ,justify="center", bg="sea green",font = z)
label3.pack()


canvas.mainloop()
