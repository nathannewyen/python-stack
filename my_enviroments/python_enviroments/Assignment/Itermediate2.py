# 1 Update Values in Dictionaries and Lists

# x = [[5, 2, 3], [10, 8, 9]]


# def update_x(x):
#     for num in x:
#         for i in range(len(num)):
#             if num[i] == 10:
#                 num[i] = 15
#     return x


# print(update_x(x))

# ######################

# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]


# def update_student():
#     for i in range(len(students)):
#         students[0]['last_name'] = 'Bryant'
#         return students


# print(update_student())

# ######################

# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }


# def change(key_soccer, sport_directory):
#     for i in range(len(sports_directory[key_soccer])):
#         if sport_directory[key_soccer][i] == "Messi":
#             sport_directory[key_soccer][i] = "Andres"
#         return sports_directory


# print(change('soccer', sports_directory))

# ######################

# z = [{'x': 10, 'y': 20}]


# def update_z(z):
#     for i in z:
#         for j in i:
#             if i[j] == 20:
#                 i[j] = 30
#     return z


# print(update_z(z))

# # 2 Iterate Through a List of Dictionaries

# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]


# def iterateDictionary(students):
#     for student in range(len(students)):
#         print('first_name ' '-',
#               students[student]['first_name'] + ',',
#               'last_name ' '-',
#               students[student]['last_name'])


# iterateDictionary(students)


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# 3  Get Values From a List of Dictionaries

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary2(students):
    for key in students:
        print(students[1]["first_name"])


iterateDictionary2(students)

#     for student in students:
#         print(student[key])


# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)


# 4 Iterate Through a Dictionary with List Values

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }


# def printInfo(dojo):
#     count = 0
#     for key, val in dojo.items():
#         print(len(val), key.upper(), val)


# print(printInfo(dojo))


# def printInfo(key, dojo):
#     count = 0
#     for ninja in dojo[key]:
#         count += 1
#         print(ninja)
#     return count, key.upper()

# print(printInfo('locations', dojo))
# print(printInfo('instructors', dojo))


# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
