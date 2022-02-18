# it is used for storing a collection of data
# Syntax {key: value}
# Get item by key
# Duplicate keys will be override


student = {
    "name": "jamal",
    "lastname": "kamal",
    "grade": 12,
}

#  update the item

# student.update({
#     "name" : "Kamal",
#     "lastname": "omid",
#     "dob": "2020-10-10"
# })

# Add a new item
#  Adding via the key
# student['dob'] = "2020-10-10"

#  Adding via the update function

# remove item
# student.popitem()
# student.pop("name") # you need to provide the key


# deleting the item
# del student['name']
# delete all the dictionary
# del student

#  clear the dictionary
# student.clear()

#  Loop the dictionary

# loop the key
# for key in student.keys():
#     print(key)

#  Loop the values
# for value in student.values():
#     print(value)

# loop the key and value
# for x,y in student.items():
#     print(x,y)

# copy the dictionary

# new_student = student.copy()

# student.update({
#     "ip": "10.10.10.1"
# })

# print(new_student)

# students = {
#     "child1" : {
#         'name': "Hamid",
#         "lastname": "Afghan"
#     },
#     "child2" : {
#         "name": "ali",
#         "lastname": "omid"
#     }
# }

# for student in students.items():
#     print(student)
