import json

# json string
# student = '{ "name": "Ahmad","last_name": "Kamal"}'


# # parse -> dict
# json_studnet = json.loads(student)

# # Dict
# print(json_studnet["last_name"])

# ----- Convert the dict to json string

# student = {
#     "name": "Jamal",
#     "last_name": "kamal"
# }

# # converts to json string
# student = json.dumps(student)

# Json object
# {
#     key: value
# }

# Json array
# {
#     [
#         {key:value},
#         {key:value},
#         ...
#     ]
# }

# dict	Object
# list	Array
# tuple	Array
# str	String
# int	Number
# float	Number
# True	true
# False	false
# None	null

# print(json.dumps({"name": "Jamal", "last_name": "Kamal"}))
# print(json.dumps([["Jamal","Jamal 2"], "Kamal", "Ali", "Parwin"]))
# print(json.dumps(("Jama", "Kamal", "Ali", "Parwin")))
# print(json.dumps("Jamal"))
# print(json.dumps(12))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# Json -> javascript Object notation {key:value}

student = {
    "name": "Jamal",
    "last_name": "kamal",
    "age": 25
}


print(json.dumps(student, indent=2, sort_keys=True))
