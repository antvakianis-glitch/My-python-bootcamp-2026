def cels_to_fahrenheit(temp):
    temp_fahrenheit = temp * 9 / 5 + 32
    return temp_fahrenheit

#with open("./weather_data.csv", "r") as data_file:
#        data = data_file.readlines()
#print(data)

#import csv
#from shlex import split
#
#from PIL.ImagePalette import raw
#
#with open("weather_data.csv", "r") as data_file:
#        data = csv.reader(data_file)
#        temperatures = []
#        for row in data:
#            if row[1] != 'temp':
#                temp = row[1]
#                temperatures.append(int(temp))
#        print(temperatures)

#import pandas
#data = pandas.read_csv("weather_data.csv")
#data_dict = data.to_dict()
#temp_list = data["temp"]
#print(temp_list.max())
#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
#monday_temp = monday.temp[0]
#print(cels_to_fahrenheit(monday_temp))
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

counts = data["Primary Fur Color"].value_counts()

new_data = pandas.DataFrame(counts)
new_data.to_csv("squirrel_count.csv")







