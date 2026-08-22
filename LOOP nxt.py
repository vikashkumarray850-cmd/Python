# ==========================================
# ENUMERATE() - PRACTICE QUESTIONS
# ==========================================


# Q1. Easy
# Create a list of 5 student names.
# Use enumerate() to print the index and name.
#
# Expected Output:
# 0 Amit
# 1 Rahul
# 2 Priya
# 3 Sneha
# 4 Arjun

# names = ["Amit", "Rahul", "Priya", "Sneha", "Arjun"]

# for index, name in enumerate(names):
#     print(index, name)

# Q2. Medium
# Create a list of 5 cities.
# Use enumerate() with start=1.
# Print the city number and city name.
#
# Expected Output:
# 1 Kolkata
# 2 Delhi
# 3 Mumbai
# 4 Pune
# 5 Chennai

# cities = ["Kolkata", "Delhi", "Mumbai", "Pune", "Chennai"]

# for index, city in enumerate(cities, start = 1):
#     print(index, city)

# Q3.
# Create a list of 5 products.
# Use enumerate() to display each product
# with its serial number starting from 1.

# products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphone"]

# for index, product in enumerate(products, start=1):
#     print(index, product)

# ==========================================
# ZIP() - PRACTICE QUESTIONS
# ==========================================


# Q1. Easy
# Create two lists:
# 1. Student names
# 2. Student marks
#
# Use zip() to print each student's
# name and marks.
#
# Example:
# Names = ["Amit", "Rahul", "Priya"]
# Marks = [85, 90, 78]
#
# Expected Output:
# Amit 85
# Rahul 90
# Priya 78

# Names = ["Amit", "Rahul"]
# Marks = [85, 90]

# for name, mark in zip(Names, Marks):
#     print(name, mark)
#--------------------------------------------------------
# Create two lists:
# 1. Employee names
# 2. Employee salaries
#
# Use zip() to print each employee's
# name and salary.
#
# Example:
# Names = ["Amit", "Rahul", "Sneha"]
# Salaries = [50000, 60000, 55000]
#
# Expected Output:
# Amit 50000
# Rahul 60000
# Sneha 55000

# Names = ["Amit", "Rahul", "Sneha"]
# Salaries = [50000, 60000, 55000]

# for name , salary in zip(Names, Salaries):
#     print(name, salary)

# Create three lists:
# 1. Product names
# 2. Product prices
# 3. Product quantities
#
# Use zip() to print the product name,
# price and quantity together.
#
# Example:
# Products = ["Laptop", "Mouse", "Keyboard"]
# Prices = [50000, 1000, 1500]
# Quantities = [2, 5, 3]
#
# Expected Output:
# Laptop 50000 2
# Mouse 1000 5
# Keyboard 1500 3

# Products = ["Laptop", "Mouse", "Keyboard"]
# Prices = [50000, 1000, 1500]
# Quantities = [2, 5, 3]

# for product,price, quality in zip(Products,Prices,Quantities):
#     print(product,price, quality)

# ==========================================
# NESTED LOOPS - PRACTICE QUESTIONS
# ==========================================


# Q1. Easy
# Use nested loops to print the following:
#
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

# for i in range(1, 4):
#     for j in range(1,4):
#         print(i , j)
#------------------------------------------------------------------------------
# Q2. Easy
# Use nested loops to print a 3 × 4 rectangle
# of stars.
#
# Expected Output:
# * * * *
# * * * *
# * * * *

# for i in range(3):
#     for j in range(4):
#         print("*", end=" ")
#     print()
#-----------------------------------------------------------------

# Q3. Medium
# Use nested loops to print the multiplication
# tables from 2 to 5.
#
# Example:
# 2 * 1 = 2
# 2 * 2 = 4
# ...
# 2 * 10 = 20
#
# Then print the table of 3, 4 and 5.

# for i in range(2, 6):          # Outer loop → 2, 3, 4, 5
#     for j in range(1, 11):     # Inner loop → 1 to 10
#         print(i, "*", j, "=", i * j)
#---------------------------------------------------------------------------

# Q4. Medium
# Use nested loops to print this pattern:
#
# 1
# 12
# 123
# 1234
# 12345

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()

# Q5. Practical
# There are 3 departments.
# Each department has 3 employees.
#
# Use nested loops to print:
#
# Department 1 - Employee 1
# Department 1 - Employee 2
# Department 1 - Employee 3
# Department 2 - Employee 1
# Department 2 - Employee 2
# Department 2 - Employee 3
# Department 3 - Employee 1
# Department 3 - Employee 2
# Department 3 - Employee 3

# for i in range (1,4):
#     for j in range(1,4):
#         print(f"Department {i} - Employee {j}" )

# ==========================================
# STAR PATTERNS - PRACTICE QUESTIONS
# ==========================================


# Q1. Basic Triangle
# Print the following pattern:
#
# *
# **
# ***
# ****
# *****
#
# Use nested loops.

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end = "")
#     print()
#----------------------------------------------------------
# Q2. Inverted Triangle
# Print the following pattern:
#
# *****
# ****
# ***
# **
# *
#
# Use nested loops.

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()
#--------------------------------------------------------
# Q3. Square Pattern
# Print a 5 × 5 square:
#
# *****
# *****
# *****
# *****
# *****
#
# Use nested loops

# for i in range (5):
#     for j in range(5):
#         print("*", end="")
#     print()
#-----------------------------------------------------------------------
# Q4.
# Print the following pattern:
#
# 1
# 12
# 123
# 1234
# 12345
#
# Use nested loops.

# for i in range (1, 6):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
#----------------------------------------------------------------------
# Q5. Increasing Star Pattern
# Take the number of rows from the user.
# Print a star triangle based on that number.
#
# Example:
# Input: 4
#
# Output:
# *
# **
# ***
# ****
#
# Input: 6
#
# Output:
# *
# **
# ***
# ****
# *****

# rows = int(input("Enter number of rows: "))

# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()

# ==========================================
# STAR PATTERNS - PRACTICE SET 2
# ==========================================


# Q6. Right-Aligned Triangle
# Take the number of rows from the user.
# Print a right-aligned star triangle.
#
# Example:
# Input: 5
#
# Output:
#     *
#    **
#   ***
#  ****
# *****

# rows = int(input("Enter number of rows: "))

# for i in range(1, rows + 1):
#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")
#     # Print stars
#     for j in range(i):
#         print("*", end="")
#-------------------------------------------------------------------------
# Q7.
# Take the number of rows from the user.
# Print an inverted right-aligned triangle.
#
# Example:
# Input: 5
#
# Output:
# *****
#  ****
#   ***
#    **
#     *

# rows = int(input("Enter number of rows: "))

# for i in range(rows, 0, -1):

#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")

#     # Print stars
#     for j in range(i):
#         print("*", end="")

#     print()
#--------------------------------------------------------------------

# Q8. Pyramid Pattern
# Take the number of rows from the user.
# Print a centered pyramid.
#
# Example:
# Input: 5
#
# Output:
#     *
#    ***
#   *****
#  *******
# *********
# rows = int(input("Enter number of rows: "))

# for i in range(1, rows + 1):

#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")

#     # Print stars
#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()

# Q9.
# Take the number of rows from the user.
# Print an inverted centered pyramid.
#
# Example:
# Input: 5
#
# Output:
# *********
#  *******
#   *****
#    ***
#     *

# rows = int(input("Enter number of rows: "))

# for i in range(rows, 0, -1):

#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")

#     # Print stars
#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()


# Q10.
# Take the number of rows from the user.
# Print a diamond pattern.
#
# Example:
# Input: 5
#
# Output:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# rows = int(input("Enter number of rows: "))

# # Upper half
# for i in range(1, rows + 1):

#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")

#     # Print stars
#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()

# # Lower half
# for i in range(rows - 1, 0, -1):

#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")

#     # Print stars
#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()



#----------------------------------------------------------------------------

#🐍 Strings — Practice Questions

# Q1. Create a string "Vikash" and print its first character.

# name = "Vikash"
# print(name[0])

# Q2. Create a string "Vikash" and print its last character using negative indexing.

# name = "Vikash"
# print(name[-1])

# Q3. Create a string "Kolkata" and print its third character.
# city = "Kolkata"
# print(city[2])

# Q4. Create a string "Python" and print "Pyt" using slicing.
# name = "Python"
# print(name[0:3])

# Q5. Create a string "Python" and print "hon" using slicing.
# name = "Python"
# print(name[3:6])

# Q6. Create a string "Programming" and print "Program" using slicing.
# name = "Programming"
# print(name[0:7])

# Q7. Create a string "Programming" and print the last 3 characters using negative slicing.
# name = "Programming"
# print(name[-3:])

# Q8. Create a string "Vikash Kumar" and print only "Vikash" using slicing.
# name ="Vikash kumar"
# print(name[0:6])

# Q9. Create a string "Vikash Kumar" and print only "Kumar" using slicing.
# name ="Vikash kumar"
# print(name[7:])

# Q10. Create a string "Data Analyst" and print "Data" and "Analyst" separately using slicing.
# text = "Data Analyst"
# print(text[0:4], text[5:])

# Q11. Create a string "Computer" and print its first 5 characters using slicing.
# name = "Computer" 
# print(name[0:5])

# Q12. Create a string "Computer" and print its last 4 characters using negative slicing.
# name = "Computer"
# print(name[-4:])

# Q13. Create a string "Python" and print "thon" using slicing.
# name = "Python"
# print(name[2:])

# Q14. Create a string "Programming" and print "gram" using slicing.
# name = "Programming"
# print(name[3:7])
#-----------------------------------------------------------------------------------------

#🐍 Strings — Part 2: String Operations


# Q1. Create two strings "Vikash" and "Kumar" and join them with a space using +.
# first_name = "Vikash"
# last_name = "Kumar"

# Full_name = first_name + " " + last_name
# print(Full_name)

# Q2. Create two strings "Data" and "Analyst" and join them using +.
# first_text = "Data"
# last_text = "Analyst"

# full_text = first_text + " " + last_text
# print(full_text)

# Q3. Create a string "Python" and print it 3 times using *.
# word = "Python"
# print(word * 3)

# Q4. Create a string "Hi " and print it 5 times using *.
# name = "Hi "
# print(name * 5)

# Q5. Create a string "Vikash" and find its length using len().
# Name = "Vikash"
# print(len(Name))

# Q6. Create a string "Data Analyst" and find its total length using len().
# text = "Data Analyst"
# print(len(text))

# Q7. Create a string "Python Programming" and check whether "Python" is present using in.
# name = "Python Programming" 
# print("Python" in name)

# Q8. Create a string "Python Programming" and check whether "Java" is not present using not in.
# name = "Python Programming" 
# print("Java" not in name)

#--------------------------------------------------------------------------------------------------------
#🐍 String Methods — Practice

# Q1. Create a string "python" and convert it into uppercase using upper().
# name = "python"
# print(name.upper())

# Q2. Create a string "PYTHON" and convert it into lowercase using lower().
# name = "PYTHON"
# print(name.lower())

# Q3. Create a string "python programming" and convert the first character to uppercase using capitalize().
# name = "python programming"
# print(name.capitalize())

# Q4. Create a string "python programming language" and convert every word's first character to uppercase using title().
# name = "python programming"
# print(name.title())

# Q5. Create a string with extra spaces around "Vikash" and remove the extra spaces using strip().
# name = "    Vikash     "
# print(name.strip())

# Q6. Create a string "I like Python" and replace "Python" with "SQL" using replace().
# name = "I like Python"
# print(name.replace("Python", "SQL"))

# Q7. Create a string "banana" and count how many times "a" appears using count().
# NAME = "banana"
# print(NAME. count("a"))

# Q8. Create a string "Python" and find the index of "t" using find().
# name = "Python"
# print(name.find("t"))

# Q9. Create a string "Python Programming" and check whether it starts with "Python" using startswith().
# name = "python programming"
# print(name.startswith("Python"))

# Q10. Create a string "Python Programming" and check whether it ends with "Programming" using endswith().
# name = "python programming"
# print(name.endswith("programming"))

#-----------------------------------------------------------------------------------------------------

# Q1. Create a string "I love Python" and split it into separate words using split().
# text = "I love Python" 
# print(text.split())


# Q2. Create a list ["Data", "Analyst"] and join the words with a space using join().
# word = ["Data", "Analyst"]
# print(" ".join(word))

# Q3. Create a string "Python" and check whether it contains only alphabets using isalpha().
# text = "Python"
# print(text. isalpha())

# Q4. Create a string "Python123" and check whether it contains only alphabets using isalpha().
# text= "Python123"
# print(text.isalpha())

# Q5. Create a string "12345" and check whether it contains only digits using isdigit().
# number="12345"
# print(number. isdigit())

# Q6. Create a string "Python123" and check whether it contains only alphabets and numbers using isalnum().
# number="Python123"
# print(number. isalnum())

# Q7. Create a string "Python 123" and check whether it contains only alphabets and numbers using isalnum().
# number="Python 123"
# print(number. isalnum())

# Q8. Create a string containing only spaces and check it using isspace().
# text = "   "

# print(text.isspace())

# Q9. Create a list ["Python", "SQL", "Excel"] and join all elements using " - " as the separator.
# languages = ["Python", "SQL", "Excel"]

# print(" - ".join(languages))

# Q10. Create a string "Data Analyst Python" and split it into separate words using split().
# text = "Data Analyst Python"

# print(text.split())