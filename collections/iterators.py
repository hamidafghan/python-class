# An iterator is an object

# iter -> convert itrator
# next -> next item

# students = ("jamal", "Kamal", "Ali", "Parwin") # iterable

# students = iter(students) # itrator

# next(students)
# next(students)
# next(students)

# print(next(students))

# name = "Jamal"

# name = iter(name)

# next(name)
# next(name)
# print(next(name))

# class Counter:

#     def __init__(self) -> None:
#         # any code
#         pass

#     def __iter__(self):
#         self.count = 1
#         return self

#     def __next__(self):
#         if self.count < 40:
#             count = self.count
#             self.count += 1
#             return count
#         else:
#             raise StopIteration


# counter = Counter()
# counter = iter(counter)

# for count in counter:
#     print(count)
