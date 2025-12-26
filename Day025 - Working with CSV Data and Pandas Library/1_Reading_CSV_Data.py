# with open("weather_data.csv") as weather:
#     data = weather.readlines()
#     print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for weather in data:
        if weather[1] != "temp":
            temperatures.append(int(weather[1]))
    print(temperatures)

import pandas

