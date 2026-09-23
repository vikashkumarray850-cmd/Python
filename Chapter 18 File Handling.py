# ==========================================
# File Handling — Read
# ==========================================

# open() — Short Summary

# Python mein file ke saath kaam karne ke liye open() use hota hai.

# open("file_name", "mode")

# Common modes:

# Mode	Meaning
# "r"	Read — file se data padhna
# "w"	Write — file mein data likhna
# "a"	Append — existing data ke end mein data add karna

# Example:

# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)

# Isme:

# data.txt → file ka naam
# "r" → read mode
# as file → opened file ko file variable se access karenge
# file.read() → content read
# with → kaam khatam hone par file automatically close



# ==========================================
# File Handling — Read
# ==========================================

# Q1. Create a file named "data.txt" and put some text inside it.
# Open the file in read mode.
# Read the complete content.
# Print the content.

# file = open("data.txt", "r")

# content = file.read()

# print(content)

# file.close()


# Q2. Open "data.txt" using with open().
# Read the complete content.
# Print the content.

# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)

# Q3. Create a file named "students.txt" with 3 student names.
# Open the file using with open().
# Read and print the complete content.

# file = open("data.txt", "r")

# content = file.read()

# print(content)

# file.close()
#----------------------

#  PREFER THIS ONE👇

#===============================================
# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)
#================================================
#--------------------------------------------------------------------------------------------------

# ==========================================
# File Handling — Write
# ==========================================

# "w" mode
# with open("data.txt", "w") as file:
#     file.write("Hello Vikash")

# Is code mein:

# with open("data.txt", "w")
# → data.txt ko write mode mein open karta hai.

# file.write("Hello Vikash")
# → file ke andar "Hello Vikash" likhta hai.

# Agar data.txt pehle se exist karti hai aur usme kuch likha hua hai, toh "w" mode purana content hata kar naya content likh sakta hai.

# 2. Multiple lines kaise likhen?
# with open("data.txt", "w") as file:
#     file.write("Vikash\n")
#     file.write("Rahul\n")
#     file.write("Amit\n")

# \n ka matlab new line.


# ==========================================
# File Handling — Write
# ==========================================

# Q1. Open "data.txt" in write mode.
# Write your name into the file.
# Close the file automatically.

# with open("data.txt", "w") as file:
#     file.write("My name is Vikash")

# Q2. Open "data.txt" in write mode.
# Write three student names into the file.
# Each name should appear on a separate line.
# Close the file automatically.

# with open("data.txt", "w") as file:
#     file.write("Vikash\n")
#     file.write("Mohit\n")
#     file.write("Ravan\n")
#     file.write("My Name Is Vikash\n")

#-----------------------------------------------------------------------------------

# ==========================================
# File Handling — Append
# ==========================================

# "a" ka matlab — Append

# Append ka matlab hota hai existing file ke end mein naya data add karna.

# Example:

# Abhi data.txt mein hai:

# Vikash
# Mohit
# Ravan

# Agar hum likhen:

# with open("data.txt", "a") as file:
#     file.write("Amit\n")

# Toh purana data delete nahi hoga.

# File ban jayegi:

# Vikash
# Mohit
# Ravan
# Amit
# "w" vs "a"
# "w" → purana content overwrite kar sakta hai
# "a" → purane content ke end mein add karta hai

# ==========================================
# File Handling — Append
# ==========================================

# Q1. Open "data.txt" in append mode.
# Add one new student name to the existing file.
# Close the file automatically.

# with open("data.txt", "a") as file:
#     file.write("SAVAN")

# Q2. Open "data.txt" in append mode.
# Add two more student names to the existing file.
# Put each name on a separate line.
# Close the file automatically.

# with open("data.txt", "a") as file:
#     file.write("jaanu\n")
#     file.write("parmeshwar\n")

#------------------------------------------------------------------------------

# ==========================================
# File Handling — CSV Read
# ==========================================

# CSV kya hoti hai?

# CSV ka full form hai Comma-Separated Values.

# Ye ek file format hai jisme data rows aur columns ke form mein store hota hai.

# Example students.csv:

# name,age,city
# Vikash,25,Kolkata
# Mohit,24,Delhi
# Ravi,26,Mumbai

# Yahan:

# name, age, city → column names
# Har line → ek row
# , → columns ko separate karta hai
# Python mein CSV kyun useful hai?

# Data Analyst ke liye CSV bahut important hai, kyunki Excel/table jaisa data CSV file mein mil sakta hai.

# Python mein CSV ko handle karne ke liye built-in csv module use kar sakte hain:

# import csv

# CSV read karne ka basic structure:

# import csv

# with open("students.csv", "r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)

# Agar CSV mein:

# name,age,city
# Vikash,25,Kolkata
# Mohit,24,Delhi

# toh row ek-ek row ko read karega.

# Sabse important difference:

# .txt  → normal text
# .csv  → table-like data (rows + columns)

# Abhi csv.reader() ko bas samjho. Practice question dene se pehle 
# hum reader aur row ko thoda aur clearly samjhenge.

# Flow yaad rakho

# import csv
#      ↓
# open CSV file
#      ↓
# csv.reader(file)
#      ↓
# for row in reader
#      ↓
# har row ko read karo

# ==========================================
# File Handling — CSV Read
# ==========================================

# Q1. Create a CSV file named "students.csv".
# Add a header with name, age, and city.
# Add three student records.
# Read the CSV file using Python.
# Print each row.

# import csv

# with open("students.csv", "r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)

# Q2. Create a CSV file named "employees.csv".
# Add a header with name, department, and salary.
# Add three employee records.
# Read the CSV file.
# Print each row.

# import csv

# with open("employees.csv", "r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)



# Q3. Create a CSV file named "products.csv".
# Add a header with product, price, and quantity.
# Add three product records.
# Read the CSV file.
# Print each row.

# import csv
# with open("products.csv", "r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)
#----------------------------------------------------------------------------------------------------

# ==========================================
# File Handling — CSV Write
# ==========================================

# Ab Python se CSV file ke andar data likhna seekhenge.

# 1. csv.writer()

# Example:

# import csv

# with open("students.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerow(["Name", "Age", "City"])
#     writer.writerow(["Vikash", 25, "Kolkata"])
#     writer.writerow(["Mohit", 24, "Delhi"])

# Yahan:

# csv.writer(file) → CSV file mein data likhne ke liye writer banata hai.
# writer.writerow(...) → ek row likhta hai.
# ["Name", "Age", "City"] → ek row ke andar columns.
# newline="" → CSV mein unwanted blank lines se bachne ke liye commonly use hota hai.

# File mein result:

# Name,Age,City
# Vikash,25,Kolkata
# Mohit,24,Delhi
# reader vs writer
# csv.reader()  → CSV se data READ
# csv.writer()  → CSV mein data WRITE

# ==========================================
# File Handling — CSV Write
# ==========================================

# Q1. Create a CSV file named "students.csv".
# Write a header with name, age, and city.
# Write three student records into the file.

# import csv

# with open("students.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerows([
#     ["Vikash", 25, "Kolkata"],
#     ["Mohit", 24, "Delhi"],
#     ["Ravi", 26, "Mumbai"]
# ])

# Q2. Create a CSV file named "employees.csv".
# Write a header with name, department, and salary.
# Write three employee records into the file.

# import csv

# with open("employees.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name", "department", "salary"])
#     writer.writerow(["Vikash", "IT", "35000"])
#     writer.writerow(["Mohit", "Sales" "50000"])
#     writer.writerow(["Ravi", "HR", "60000"])


# Q3. Create a CSV file named "products.csv".
# Write a header with product, price, and quantity.
# Write three product records into the file.

# import csv

# with open("products.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerow(["Product", "Price", "Quantity"])
#     writer.writerow(["Apple", "50", "3"])
#     writer.writerow(["Banana","20", "4"])
#     writer.writerow(["Mango", "40", "2"])

#-----------------------------------------------------------------------------------------------

# ==========================================
# File Handling — CSV Append
# ==========================================

# CSV Append ka next part.

# Ab ek important difference samjho:

# writer.writerow(...)

# → 1 row add

# writer.writerows([...])

# → multiple rows add

# Example:

# import csv

# with open("students.csv", "a", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerow(["Amit", 27, "Mumbai"])

# Isse sirf ek student add hoga.

# Multiple students:

# import csv

# with open("students.csv", "a", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerows([
#         ["Amit", 27, "Mumbai"],
#         ["Rahul", 23, "Pune"]
#     ])

# ==========================================
# File Handling — CSV Append
# ==========================================

# Q1. Open "students.csv" in append mode.
# Add one new student record to the existing CSV file.

# import csv

# with open("students.csv", "a", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerow(["Jigmesh", "30", "Mumbai"])


# Q2. Open "employees.csv" in append mode.
# Add two new employee records to the existing CSV file.

# import csv

# with open("employees.csv", "a", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerows([
#         ["Manu", "HR", "40000"],
#         ["Ranu", "IT", "25000"]
#     ])


# Q3. Open "products.csv" in append mode.
# Add two new product records to the existing CSV file.

# import csv

# with open("products.csv", "a", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerows([
#         ["Coconut", "50", "2"],
#         ["Orange", "10", "3"]
#     ])


# File Handling chapter complete ✅

# Ab tak kya seekha
# File Handling
# │
# ├── open() ✅
# ├── Read ("r") ✅
# ├── Write ("w") ✅
# ├── Append ("a") ✅
# │
# └── CSV Basics ✅
#     ├── csv.reader() ✅
#     ├── csv.writer() ✅
#     ├── writerow() ✅
#     └── writerows() ✅



with open("data.txt", "r") as file:
    content = file.read()
    print(content)