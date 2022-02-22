# Functions in python

# How to define a fucntion
# def get_fullname():
#     # function logic
#     print("Jamal Kamal")

# get_fullname()

# Function arguments
# def full_name(name, lastname):
#     print(name + str(lastname))

# full_name("Kamal", "Jamal")

# Default value in argument

# Arbitary argument -> tuple
# def user_address(*address):
#     print(type(address))
#     print(address)


# user_address("Kabul", 3, 30)

# Keyword arugment

# def user_address(city, street, house):
#     print (city, street, house)

# user_address(house=10, street =20, city="kabul")

# Arbitary keyword arguments -> dictionary

# def user_address(**address):
#     print(type(address))
#     print(address['city'])

# user_address(street=3, house=3, city="Kabul")

# Iterable as an argument
# student = {
#     "name": "Jamal",
#     "last_name": "Kamal",
#     "year": 2020
# }

# def get_students(student):
#     for item in student.items():
#         print(item)


# get_students(student)


# recursion of function
# 6! => 1*2*3*4*5*6 = 720

# 6
# step 1 => 6*5 => 30
# step 2 => 30 * 4 => 120
# ...
# step 6 => xxx *1 => xxx

# def factorial(number):

#     if number == 0:
#         return "No valid number"

#     if number == 1:
#         return number
#     else:
#         return (number * factorial(number - 1))

# restult = factorial(0)

# print(type(restult))

# Lamba function -> lamba arguments: expresion

# sum = lambda x,y: x+y

# print(sum(10,20))
