
# This is me trying to open and printing a csv file with just python:

# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# Now I tried a native library for csv manipulation
# to get all the temperatures in the csv file
# Still using: with open() as file  -_-

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperature = int(row[1])
#             temperatures.append (temperature)
#     print(f"\n{temperatures}")


# Discovering that with pandas, this is so much easier!
# We only need 3 lines:

import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])


# Understanding the types used in panda's library:

print(type(data))                # DataFrame - the whole table
print(type(data["temp"]))        # Series - single column - "list"


# Converting a DataSet(table) to a dictionary:
data_dict = data.to_dict() # Here I'm using the .to_dict() panda's function
print(data_dict)


# Converting a column(Series) to a list:
temp_list = data["temp"].tolist() # Here I'm using the .tolist() panda's function
print(len(temp_list))

# Now calculating the average of the temperatures in the table:
avg = data["temp"].mean() # Here I'm using the .mean() panda's function
print(avg)

# Now calculating the max temperature in the table:
max_temp = data["temp"].max()
print(max_temp)

# IMPORTANT!
# data.temp is the same as data["temp"]

# Getting data in a row:
print(data[data.temp == max_temp])
print(data[data.day == "Monday"])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(f"Temperature in Celsius: {monday_temp}°C")
print(f"Temperature in Fahrenheit: {monday_temp_F}°F")


# Creating a dataframe from scratch:

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")