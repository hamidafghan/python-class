# 1. Write a program that accepts a string from the user.
#  Your program should count and display a number of vowels in that string.

# input = input('Please enter a word: ').lower() # Afghanistan

# vowels = 0

# for letter in input:
#     if letter in "aoieu":
#         vowels += 1

# print(vowels)


#  -----------------

# 2. Write a program that reads a string from keyboard and display:

# * The number of uppercase letters in the string
# * The number of lowercase letters in the string
# * The number of digits in the string
# * The number of whitespace characters in the string 

# input = input('Please enter a sentence:')

# upper = lower = digits = space = 0

# for letter in input: 
#     if letter.isupper():
#         upper += 1
#     elif letter.islower():
#         lower += 1
#     elif letter.isdigit():
#         digits += 1
#     elif letter.isspace():
#         space += 1

# print(upper, lower, digits, space)

# --------------------

# 3.Write a Python program that accepts a string from user. Your program should create and display a new string 
# where the first and last characters have been exchanged.For example if the user enters the
#  string 'HELLO' then new string would be 'OELLH'

# input = input('Please enter a text:')

# print(input[-1] + input[1:-1] + input[0])

# # -----------------------------------------
# 5. Write a Python program that accepts a string from user. Your program should create 
# a new string by shifting one position to left.
# For example if the user enters the string 'examination 2021' then new string would be 'xamination 2021e' 

# input = input('Please enter a text: $') # Afghanistan

# print(input[1:] + input[0])




