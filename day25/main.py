# with open('weather_data.csv') as f:
#     data = f.readlines()

# import csv

# with open('weather_data.csv') as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
    
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

# print(data["temp"].mean())
# print(data["temp"].max())

# # get data in columns
# print(data["condition"])
# print(data.condition)

# get data in row
# print(data[data.day == "Monday"])

# challenge
# print the row of data which had the highest temperature
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)


# Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 54, 56]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')







# SQUIRREL CENSUS CHALLENGE
# create new csv called "squirrel_count.csv" with the amount of squirrels in each color
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])


new_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

dataframe = pandas.DataFrame(new_data)
print(dataframe)

dataframe.to_csv('squirrel_count.csv')

