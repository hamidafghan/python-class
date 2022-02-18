# List is used for storing a collection of data
# Syntax []
# get item by index
# To update more
# accept duplicate values

students = [
    ["Jamal", 10],
    ["Kamal", 12],
    ["Baheer", 20],
    ["Asra", 5]
]

# Accessing the itmes
# print(students[2])

# Negative Indexing
# print(students[-2])

# Range of indexes
# print(students[1:])
# the last number is not includded

# Range of negative index
# print(students[-3:-1])

# Check if item exist
# print("Jamal" in students)

#  Add a new itme -> append
# students.append("Parwin")

# insert a new time
# students.insert(1, "Parwin")

# Extend the list
# newStudents = ["Alex", "Gareth"]
# newStudents.extend(students)

# Update the value
# students[0] = "Ahamd"

# Removing an item based on value -> remove
# students.remove("Jamal")

# Removing an item by index -> pop
# students.pop(1)

# Deleting the item by index -> support the range
# del students

# Clear all the list items
# students.clear()

# sort the list

# students.sort(key=lambda student: student[1], reverse=True)


print(students)

