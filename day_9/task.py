"""
    - dictionary
    - key value pair
    - wiping a dictionary
    - editing the data
    - nesting list and dictionary
    - accessing item inside a nested dictionary
"""

programming_dictionary =  {
    "Bug" : "An error on the program",
    "Function" : "A piece of code that you can call",
    "Loop" : "Doing something over and over again"
}

# print(programming_dictionary["Bug"])

# for key in programming_dictionary:
#     print(programming_dictionary[key])

# nested_list = ["a", "b", ["c", "d"]]

# accessing data in a 2d list
# print(nested_list[2][0])

travel_log = {
    "france" : {
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits" : 12
    },
    "germany" : {
        "cities_visited" : ["berlin", "hamburg", "stuttgart"],
        "total_visits" : 24
    }
}

print(travel_log["germany"]["cities_visited"][0])