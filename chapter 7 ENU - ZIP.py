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