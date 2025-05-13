# This is me learning new skills of list/dictionary comprehension

# LIST COMPREHENSION

# new_list = [new_item for item in list if test]

name = "Angela"

new_list = [letter for letter in name]
print(new_list)

new_nums = [num*2 for num in range(1,5)]
print(new_nums)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
print(names)

short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)

# DICTIONARY COMPREHENSION

# new_dict = {nem_key:new_value for item in list if test}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

import random
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

student_scores = {
    'Alex': 76,
    'Beth': 32,
    'Caroline': 38,
    'Dave': 66,
    'Eleanor': 86,
    'Freddie': 86
}

passed_students = {student:score for (student, score) in  student_scores.items() if score >= 70}
print(passed_students)

passed_students = {
    'Alex': 76,
    'Eleanor': 86,
    'Freddie': 86
}

import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pd.DataFrame(student_dict)

print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    # print(row["student"])
    # print(row["score"])
    if row.student == "Angela":
        print(row.score)