#===============================
# SORTED() WITH KEY
#===============================

# sorted() kya karta hai?

# sorted() kisi iterable ke elements ko sort karke ek new list return karta hai.

# Example:

# numbers = [50, 10, 40, 20, 30]
# result = sorted(numbers)
# print(result)

# Output:

# [10, 20, 30, 40, 50]

# Original list change nahi hoti:

# print(numbers)

# Output:

# [50, 10, 40, 20, 30]

# Yani:

# sorted() → new sorted list
# 2. Reverse sorting

# Agar descending order chahiye:

# numbers = [50, 10, 40, 20, 30]

# result = sorted(numbers, reverse=True)

# print(result)

# Output:

# [50, 40, 30, 20, 10]
# 3. key kya karta hai?

# Ab main important part.

# key Python ko batata hai:

# "Sorting kis basis par karni hai?"

# Example:

# students = [
#     ("Vikash", 70),
#     ("Ravi", 90),
#     ("Mohit", 60)
# ]

# result = sorted(students, key=lambda student: student[1])

# print(result)

# Output:

# [('Mohit', 60), ('Vikash', 70), ('Ravi', 90)]

# Yahan:

# key=lambda student: student[1]

# ka matlab:

# marks ke basis par sort karo.

# student[1] → marks.

# Simple visual
# ("Vikash", 70)  → 70
# ("Ravi", 90)    → 90
# ("Mohit", 60)   → 60
#                        ↓
#                   sorted by marks
#                        ↓
# Mohit → 60
# Vikash → 70
# Ravi → 90

# Data Analyst ke liye ye concept important hai, kyunki kabhi data ko name, 
# salary, marks, price, age etc. ke basis par sort karna hota hai.

# Abhi lambda + sorting ko alag se detail mein nahi karenge.
#  Pehle sorted() + key ka basic concept strong karenge.

# Practice
# ==========================================
# Advanced Python — sorted() with key
# ==========================================

# Q1. Create a list of numbers.
# Use sorted() to sort the numbers in ascending order.

# numbers = [30, 10, 20, 40]

# result = sorted(numbers)
# print(result)
#________________________________________________________


# Q2. Create a list of tuples containing student names and marks.
# Use sorted() with key to sort the students by their marks.

# students = [
#     ("Vikash", 70),
#     ("Ravi", 90),
#     ("Mohit", 60)
# ]

# result = sorted(students, key=lambda student: student[1])
# print(result)
#________________________________________________________


# Q3. Create a list of tuples containing product names and prices.
# Use sorted() with key to sort the products by their prices.

products = [
    ("Rice", 50),
    ("Oil", 120),
    ("Biscuit", 30),
    ("Dal", 80)
]

result = sorted(products, key=lambda product: product[1])
print(result)

#________________________________________________________


# Q4. Create a list of employee names and salaries.
# Use sorted() to sort the employees by salary
# from highest salary to lowest salary.

employees = {
    ("vikash" , 30000),
    ("ravi", 49999)
}

result = sorted(
    employees,key=lambda employee: employee[1],
    reverse = True
)

print(result)

