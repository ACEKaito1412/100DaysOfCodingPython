
# list comprehension

# numbers = [1,2,3]
# new_list = [n + 1 for n in numbers]


# n_doubled = [n * 2 for n in range(1,5)]
# print(n_doubled)

# names = ["james", "alphas", "remu", "angela"]

# new_names = [name.upper() for name in names if len(name) > 4]
# print(new_names)
# import random

# names = ["james", "alphas", "remu", "angela"]

# student_score  = {student:random.randint(50, 100) for student in names}

# pass_stud = {key:value for (key, value) in student_score.items() if value >= 60}

# print(pass_stud)

import pandas

student_dic = {
    "student" : ["james", "alphas", "remu", "angela"],
    "score": [78, 98, 45, 100]
}

student_df = pandas.DataFrame(student_dic)
print(student_df)

for (index, row) in student_df.iterrows():
    print(row.score)

