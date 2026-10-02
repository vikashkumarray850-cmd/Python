#===============================
# >>>>>>>> ENUMERATE <<<<<<<<<<<
#===============================

# enumerate() kya karta hai?

# enumerate() kisi iterable ki value ke saath uska index bhi deta hai.

# Normal for loop:

# students = ["Vikash", "Ravi", "Mohit"]

# for student in students:
#     print(student)

# Output:

# Vikash
# Ravi
# Mohit

# Lekin agar hume index + value dono chahiye:

# students = ["Vikash", "Ravi", "Mohit"]

# for index, student in enumerate(students):
#     print(index, student)

# Output:

# 0 Vikash
# 1 Ravi
# 2 Mohit

# Yahan:

# index → 0, 1, 2
# student → Vikash, Ravi, Mohit
# Simple structure
# for index, value in enumerate(iterable):
#     print(index, value)
# Index 1 se start karna ho

# Normally index 0 se start hota hai.

# Lekin hum starting number change kar sakte hain:

# students = ["Vikash", "Ravi", "Mohit"]

# for index, student in enumerate(students, start=1):
#     print(index, student)

# Output:

# 1 Vikash
# 2 Ravi
# 3 Mohit

# Data Analyst work mein enumerate() useful hai jab data ke 
# saath row position/index bhi track karna ho.

# Ab basic practice:

# ==========================================
# Advanced Python — enumerate()
# ==========================================

# Q1. Create a list of 4 student names.
# Use enumerate() to print the index and student name.

# students = ["Vikash", "Ravi", "Mohit", "Raj"]

# for index, student in enumerate(students):
#     print(index,student)
#__________________________________________________________--


# Q2. Create a list of 5 product names.
# Use enumerate() to print the product number starting from 1
# and the product name.

# products = [ "Rice", "Dal", "Oil", "Masala", "Biscuit"]

# for index,product in enumerate(products, start=1):
#     print(index,product)
#_________________________________________________________

# Q3. Create a list of 4 employee names.
# Use enumerate() to print the index and employee name.
# Start the index from 1.

# employees = ["vikash", "ravi", "mohit", "Rohit"]

# for index , employee in enumerate(employees, start=1):
#     print(index,employee)
