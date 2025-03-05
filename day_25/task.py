import csv

data = []

# with open('weather_data.csv', mode='r') as f:
#     content = csv.reader(f)
#     temperature = []
#     for weather in content:
#         if weather[1] != "temp":
#             temperature.append(int(weather[1]))
        
#     print(temperature)

import pandas

data = pandas.read_csv('weather_data.csv')


# data_dic = data.to_dict()
# print(data_dic)

temp_list = data['temp'].to_list()

print((temp_list))

# print(sum(temp_list) / len(temp_list))
# alternative
# getting the average
# print(data['temp'].mean())
# print(data.temp.mean())

#  getting the max
# print(data['temp'].max())
# print(data.temp.mean())

#  get the data in row
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]

# far = monday.temp * 1.8 + 32

# data_dict = {
#     "students" : ['arry','james', 'angela'],
#     "scores" : [76, 89, 70]
# }

# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_data.csv")
