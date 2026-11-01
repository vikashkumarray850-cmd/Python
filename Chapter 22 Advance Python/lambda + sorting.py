#===================================
# ADVANCED PYTHON — LAMBDA + SORTING
#===================================

# Pichhle topic mein humne ye kiya tha:

# employees = {
#     ("vikash", 30000),
#     ("ravi", 49999)
# }
# result = sorted(
#     employees,
#     key=lambda employee: employee[1],
#     reverse=True
# )
# print(result)

# Ab samajhte hain ki lambda sorting ke andar exactly kya kar raha hai.

# 1. Lambda ka basic idea

# Lambda ek small anonymous function hota hai.

# Normal function:

# def square(x):
#     return x * x

# Same kaam lambda se:

# square = lambda x: x * x
# print(square(5))

# Output:
# 25

# 2. Sorting mein lambda ka use

# Maan lo:

# students = [
#     ("Vikash", 70),
#     ("Ravi", 90),
#     ("Mohit", 60)
# ]

# Hume marks ke according sort karna hai.

# result = sorted(
#     students,
#     key=lambda student: student[1]
# )
# print(result)

# Yahan:
# lambda student: student[1]

# ka matlab hai:
# Har tuple mein se second value lekar sorting karo.

# Example:

# ("Vikash", 70) → 70
# ("Ravi", 90)   → 90
# ("Mohit", 60)  → 60

# Isliye result:

# [('Mohit', 60), ('Vikash', 70), ('Ravi', 90)]
# 3. Descending sorting

# Agar highest marks pehle chahiye:

# result = sorted(
#     students,
#     key=lambda student: student[1],
#     reverse=True
# )
# Result:

# [('Ravi', 90), ('Vikash', 70), ('Mohit', 60)]
# Data Analyst ke liye important pattern

# Is pattern ko yaad rakho:

# sorted(data, key=lambda x: x[index])

# Aur descending:

# sorted(data, key=lambda x: x[index], reverse=True)

# Ye salary, marks, price, sales, rating jaise data ko sort 
# karne mein kaafi useful hai.


# ==========================================
# Advanced Python — Lambda + Sorting
# ==========================================

# Q1. Create a list of tuples containing employee names and salaries.
# Use sorted() with lambda to sort the employees by salary
# from lowest salary to highest salary.

# employees = [
#     ("Vikash", 30000),
#     ("Ravi", 50000),
#     ("Aman", 25000),
#     ("Mohit", 40000)
# ]

# result = sorted(
#     employees,
#     key=lambda employee: employee[0]
# )
# print(result)

# Q2. Create a list of tuples containing product names and prices.
# Use sorted() with lambda and reverse=True to sort the products
# from highest price to lowest price.

# products = [
#     ("Clothes", 266),
#     ("Jeans", 599),
#     ("Trouser", 798)
# ]

# result = sorted(
#     products, key=lambda product: product[1],
#     reverse=True
# )
# print(result)

# Q3. Create a list of tuples containing student names and marks.
# Use sorted() with lambda to sort the students by marks
# from highest marks to lowest marks.

# Students = [
#     ("Vikash", 57),
#     ("Ravi", 67),
#     ("Aman", 98),
#     ("Mohit", 56)
# ]

# result = sorted(
#     Students, 
#     key=lambda Student:Student[1],
#     reverse=True
# )
# print(result)


# Q4. Create a list of tuples containing employee names and salaries.
# Use sorted() with lambda to sort the employees by their names
# in alphabetical order.

# employees = [
#     ("Vikash", 30000),
#     ("Ravi", 50000),
#     ("Aman", 25000),
#     ("Mohit", 40000)
# ]

# result = sorted(
#     employees, key=lambda employee: employee[0],
# )
# print(result)


# Q5. Create a list of tuples containing products and their prices.
# Use sorted() with lambda to sort the products by price
# from lowest price to highest price.

products = [
    ("Rice", 50),
    ("Oil", 120),
    ("Biscuit", 30),
    ("Dal", 80)
]

result = sorted(
    products, key=lambda product:product[1]
)
print(result)