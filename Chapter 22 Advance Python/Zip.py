#===============================
# >>>>>>>> ZIP 
#===============================

# zip() kya karta hai?

# zip() do ya do se zyada iterables ki values ko position 
# ke according pair/group karta hai.

# Example:

# names = ["Vikash", "Ravi", "Mohit"]
# ages = [25, 24, 26]

# result = zip(names, ages)

# for item in result:
#     print(item)

# Output:

# ('Vikash', 25)
# ('Ravi', 24)
# ('Mohit', 26)

# Yani:

# names       ages
#   ↓           ↓
# Vikash      25
# Ravi        24
# Mohit       26

# zip() ne same position ki values ko saath mein combine kar diya.

# Data Analyst mein iska use

# Maan lo tumhare paas:

# employees = ["Vikash", "Ravi", "Mohit"]
# salaries = [40000, 50000, 45000]

# Aur tum employee + salary ko saath process karna chahte ho:

# for employee, salary in zip(employees, salaries):
#     print(employee, salary)

# Output:

# Vikash 40000
# Ravi 50000
# Mohit 45000

# Yeh practical data-processing situation mein useful hai.

# Ek important rule

# Agar lengths different hain:

# names = ["Vikash", "Ravi", "Mohit"]
# ages = [25, 24]
# for name, age in zip(names, ages):
#     print(name, age)

# Output:

# Vikash 25
# Ravi 24

# Mohit ka pair nahi bana, kyunki corresponding age available nahi thi.

# So basic rule:

# zip() shortest iterable ke according pairs banata hai.

# Ab practice:

#==========================================
# Advanced Python — zip()
#==========================================

# Q1. Create two lists:
# One list should contain 3 student names.
# The second list should contain their marks.
# Use zip() and a for loop to print each student with their marks.

# students = ["Vikash", "Ravi", "Mohit"]
# marks = [50, 87, 78]

# for student , mark in zip(students, marks):
#     print(student, mark)
#_______________________________________________________

# Q2. Create two lists:
# One list should contain 4 product names.
# The second list should contain their prices.
# Use zip() to print each product with its price.

# products = [ "Rice", "Dal", "Oil", "Masala"]
# prices = [ 50, 30, 100, 200, 5]

# for product , price in zip(products, prices):
#     print(product, price)
#_________________________________________________


# Q3. Create three lists:
# One list should contain 3 employee names.
# One list should contain their departments.
# One list should contain their salaries.
# Use zip() to print the employee name, department, and salary together.

# employees = ["vikash", "ravi", "mohit"]
# departments = ["HR", "Sales", "IT"]
# salaries = [25000, 50000, 70000]

# for employee , department, salary in zip(employees,departments,salaries):
#     print(employee,department,salary)