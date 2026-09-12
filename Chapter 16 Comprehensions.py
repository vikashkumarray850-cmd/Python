# List Comprehension kya hota hai?

# List comprehension ka simple meaning:

# for loop se list banane ka short way.

# Maan lo hume 1 se 5 tak list banani hai.

# Normal for loop:

# numbers = []

# for i in range(1, 6):
#     numbers.append(i)

# print(numbers)

# Output:

# [1, 2, 3, 4, 5]

# Ab isi ka short version:

# numbers = [i for i in range(1, 6)]

# print(numbers)

# Output same:

# [1, 2, 3, 4, 5]
# Is syntax ko todte hain
# [i for i in range(1, 6)]

# Isko left se right padho:

# [i]          → list mein kya rakhna hai
#    [for i]   → kis variable par loop chalega
#         [range(1, 6)] → values kahan se aayengi

# Matlab:

# i = 1 → list mein 1
# i = 2 → list mein 2
# i = 3 → list mein 3
# i = 4 → list mein 4
# i = 5 → list mein 5

# Result:

# [1, 2, 3, 4, 5]





# ==========================================
# Python Comprehensions — Basic List Comprehension Practice
# ==========================================


# Q1.
# Create a list containing numbers from 1 to 5.
# Use list comprehension.
# Print the list.

# numbers = [1,2,3,4,5]

# numbers = [i for i in range(1, 6)]

# print(numbers)

# Q2.
# Create a list containing the squares of numbers from 1 to 5.
# Use list comprehension.
# Print the list.

# squares = [i * i for i in range(1, 6)]

# print(squares)

# Q3.
# Create a list containing the cubes of numbers from 1 to 5.
# Use list comprehension.
# Print the list.

# cubes = [i ** 3 for i in range(1,6)]

# print(cubes)

#------------------------------------------------------------------------------------------


# ==========================================
# Python Comprehensions — List Comprehension + if
# ==========================================

# Q1.
# Create a list containing only even numbers
# from 1 to 10.
# Use list comprehension with if.
# Print the list.

# numbers =[i for i in range(1,11) if i % 2== 0]

# print(numbers)

# Q2.
# Create a list containing only numbers greater than 5
# from 1 to 10.
# Use list comprehension with if.
# Print the list.

# numbers = [i for i in range (1,11) if i > 5]

# print(numbers)


# Q3.
# Create a list containing the squares of only even numbers
# from 1 to 10.
# Use list comprehension with if.
# Print the list.

# squares =[i ** 2 for i in range(1, 11) if i % 2 == 0]

# print(squares)
#-----------------------------------------------------------------------------------------------------

# ==========================================
# Python Comprehensions — List Comprehension + if-else
# ==========================================

# Syntax yaad rakho

# if-only mein:

# [expression for i in iterable if condition]
#-------------------
# Lekin if-else mein order change hota hai:

# [expression_if_true if condition else expression_if_false for i in iterable]

# Q1.
# Create a list from 1 to 10.
# Store "Even" for even numbers and "Odd" for odd numbers.
# Use list comprehension with if-else.
# Print the list.

# numbers = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 11)]

# print(numbers)

# Q2.
# Create a list from 1 to 10.
# Store the number itself if it is even.
# Store 0 if it is odd.
# Use list comprehension with if-else.
# Print the list.

# numbers = [i if i % 2 == 0 else 0 for i in range(1, 11)]

# print(numbers)


# Q3.
# Create a list from 1 to 10.
# Store the square of the number if it is even.
# Store the cube of the number if it is odd.
# Use list comprehension with if-else.
# Print the list.

# squares = [i ** 2 if i % 2 == 0 else i ** 3 for i in range(1,11)]

# print(squares)

#--------------------------------------------------------------------------------

# ==========================================
# Python Comprehensions — Nested List Comprehension Practice
# ==========================================

# Nested List Comprehension kya hota hai?

# Simple comprehension mein ek loop hota hai:

# numbers = [i for i in range(1, 4)]

# Nested comprehension mein ek comprehension ke andar doosra loop hota hai.

# Pehle normal nested for loop dekho:

# numbers = []

# for i in range(1, 4):
#     for j in range(1, 4):
#         numbers.append(j)

# print(numbers)

# Output:

# [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Isi ko nested list comprehension mein:

# numbers = [j for i in range(1, 4) for j in range(1, 4)]

# print(numbers)
# Syntax
# [expression for outer_loop for inner_loop]

# Important: Isko padhne ka simple tarika:

# [j for i in range(1, 4) for j in range(1, 4)]

# Pehle i wala loop chalega, aur har i ke liye j wala loop chalega.

# Ek aur useful example

# Normal nested loop:

# result = []

# for i in range(1, 4):
#     for j in range(1, 4):
#         result.append(i * j)

# print(result)

# Comprehension:

# result = [i * j for i in range(1, 4) for j in range(1, 4)]

# print(result)

#=======================================
# QUESTION STARTED NOW
#=======================================

# Q1.
# Create a list containing all combinations of numbers
# from 1 to 3 with numbers from 1 to 3.
# Use nested list comprehension.
# Print the list.

# numbers = [j for i in range(1,3) for j in range(1,3)]

# print(numbers)

# Q2.
# Create a list containing the multiplication results
# of numbers from 1 to 3 with numbers from 1 to 3.
# Use nested list comprehension.
# Print the list.

# numbers = [i * j for i in range(1,4) for j in range(1,4)]

# print(numbers)

# Q3.
# Create a list containing pairs [i, j]
# for every value of i from 1 to 3
# and every value of j from 1 to 2.
# Use nested list comprehension.
# Print the list.

# numbers = [[i, j] for i in range(1, 4) for j in range(1, 3)]

# print(numbers)
#--------------------------------------------------------------------------------

# ==========================================
# Python Comprehensions — Dictionary Comprehension Practice
# ==========================================

# Dictionary Comprehension kya hota hai?

# Normal dictionary banane ke liye hum loop use kar sakte hain:

# numbers = {}

# for i in range(1, 6):
#     numbers[i] = i * i

# print(numbers)

# Output:

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Yahan:

# i → key
# i * i → value

# Dictionary comprehension se same kaam short mein:

# numbers = {i: i * i for i in range(1, 6)}

# print(numbers)

# Output:

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Syntax
# {key: value for variable in iterable}

# List comprehension mein:

# [i * i for i in range(1, 6)]

# Dictionary comprehension mein:

# {i: i * i for i in range(1, 6)}

# Main difference:
# [] → List
# {key: value} → Dictionary

#=======================================
# QUESTION STARTED NOW
#=======================================

# Q1.
# Create a dictionary where numbers from 1 to 5
# are the keys and their squares are the values.
# Use dictionary comprehension.
# Print the dictionary.

# numbers = {i: i * i for  i in range(1, 6)}

# print(numbers)

# Q2.
# Create a dictionary where numbers from 1 to 5
# are the keys and their cubes are the values.
# Use dictionary comprehension.
# Print the dictionary.

# cubes = {i : i ** 3 for i in range(1, 6)}

# print(cubes)

# Q3.
# Create a dictionary where numbers from 1 to 5
# are the keys and each value is double the key.
# Use dictionary comprehension.
# Print the dictionary.

# numbers = {i: i * 2 for i in range(1, 6)}

# print(numbers)