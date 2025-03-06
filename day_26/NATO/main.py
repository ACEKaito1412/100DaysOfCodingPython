student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
NATO_NAMES = pandas.read_csv('nato_alphabet.csv')

nato_dic = {row.letter:row.code for (index, row) in NATO_NAMES.iterrows()}
# print(nato_dic)
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_name = input("Whats your name: ").upper()

nato_translate = [value for (key, value) in nato_dic.items() if key in input_name]
print(nato_translate)