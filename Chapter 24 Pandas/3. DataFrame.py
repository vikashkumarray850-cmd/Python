# ========================================
# CODE NUMBERING BY:-

#  16 TO 153     DataFrame kya hota hai?
#  157 TO 286    pd.DataFrame()
#  290 TO 367    Dictionary se DataFrame
#  370 TO 533    List of Lists se DataFrame
#  537 TO 669    DataFrame Columns
#  673 TO 807    DataFrame Index
#  811 TO 927    DataFrame Shape
#  931 TO 1043   DataFrame Size
#  1047 TO 1176  DataFrame dtypes
# ========================================

#==============================
# 1: DataFrame kya hota hai?
#==============================

# Abhi tak humne Pandas Series padhi hai. 
# Series ko filhaal ek single column ki tarah samjho.

# Maan lo hamare paas 3 employees ka data hai:

# Name	Age	Salary
# Vikash	25	25000
# Mohit	24	35000
# Ravi	26	50000

# Is data mein 3 columns hain:

# Name
# Age
# Salary

# Aur 3 rows hain, har row ek employee ki information rakhti hai.

# DataFrame kya hai?

# Pandas DataFrame ek two-dimensional, tabular data structure hai. 
# rows aur columns hote hain.
#  Excel ki table ya SQL ki table ki tarah soch sakte ho.

# 1. DataFrame aur Series mein difference

# Series — ek column:

# import pandas as pd

# salary = pd.Series([25000, 35000, 50000])

# print(salary)

# Output:

# 0    25000
# 1    35000
# 2    50000
# dtype: int64

# DataFrame — multiple columns:

# import pandas as pd

# data = {
#     "Name": ["Vikash", "Mohit", "Ravi"],
#     "Age": [25, 24, 26],
#     "Salary": [25000, 35000, 50000]
# }

# df = pd.DataFrame(data)

# print(df)

# Output:

#      Name  Age  Salary
# 0  Vikash   25   25000
# 1   Mohit   24   35000
# 2    Ravi   26   50000

# Yahan df hamara DataFrame variable hai.

# Dhyan do:

# Har employee ki information ek row mein hai.
# Har type ki information ka apna column hai.
# 0, 1, 2 default row indexes hain.
# 2. Data Analyst ke liye DataFrame kyun important hai?

# Real-world data aksar tables mein milta hai, jaise:

# Sales reports
# Employee records
# Customer details
# Product prices
# Monthly expenses

# DataFrame ki madad se hum aise data ko select, filter, 
# sort aur analyse kar sakte hain.

# Practice — DataFrame Introduction
# ==========================================
# Pandas DataFrame — Introduction Practice
# ==========================================

# Q1. Create a DataFrame containing three columns:
# Name: ["Amit", "Neha", "Rahul"]
# Age: [22, 24, 23]
# City: ["Kolkata", "Delhi", "Mumbai"]
#
# Print the complete DataFrame.

# import pandas as pd
# data = {
#     "Name": ["Amit", "Neha", "Rahul" ],
#     "Age" : [22, 24, 23],
#     "City": ["Kolkata", "Mumbai", "Delhi"]
# }
# df = pd.DataFrame(data)
# print(df)
#-----------------------------------------

# Q2. Create a DataFrame containing:
# Product: ["Egg", "Maggi", "Milk"]
# Price: [7, 14, 30]
# Quantity: [12, 8, 5]
#
# Print the complete DataFrame.

# import pandas as pd

# data = {
#     "Product": ["Egg", "Maggi", "Milk"],
#     "Price": [7, 14, 30],
#     "Quantity": [12, 8, 5]
# }
# df = pd.DataFrame(data)
# print(df)
#----------------------------------------------

# Q3. Create a DataFrame containing:
# Student: ["Ravi", "Priya", "Aman"]
# Marks: [75, 92, 68]
#
# Print the complete DataFrame.

# import pandas as pd
# data = {
#     "Students": ["Ravi", "Priya", "Aman"],
#     "Marks": [75, 92, 68]
# }
# df = pd.DataFrame(data)
# print(df)
#_____________________________________________________________________________________________________

#==============================
# 2: pd.DataFrame()
#==============================

# pd.DataFrame() kya hai?

# pd.DataFrame() Pandas ka function hai jo data ko rows aur columns wali table mein convert karta hai.

# Example:

# import pandas as pd

# data = {
#     "Name": ["Vikash", "Mohit", "Ravi"],
#     "Age": [25, 24, 26]
# }

# df = pd.DataFrame(data)

# print(df)

# Output:

#      Name  Age
# 0  Vikash   25
# 1   Mohit   24
# 2    Ravi   26

# Ab code ko step by step samjho.

# Step 1: Dictionary banana

# data = {
#     "Name": ["Vikash", "Mohit", "Ravi"],
#     "Age": [25, 24, 26]
# }

# Yahan:

# "Name" aur "Age" column names hain.
# Unki lists mein column ki values hain.

# Step 2: DataFrame banana

# df = pd.DataFrame(data)

# Pandas dictionary ke data ko table mein convert karta hai aur result df variable mein store hota hai.

# Step 3: Table print karna

# print(df)

# Isse poora DataFrame display hota hai.

# 2. DataFrame mein rows kaise banti hain?

# Dictionary ki dono lists mein 3-3 values hain, isliye DataFrame mein 3 rows banti hain.

# Index	Name	Age
# 0	Vikash	25
# 1	Mohit	24
# 2	Ravi	26

# Dhyan rakho: har list ki pehli value pehli row mein, 
# doosri value doosri row mein aur teesri value teesri row mein jaati hai.

# Aam taur par, dictionary se DataFrame banate waqt sabhi 
# columns ki lists ki length barabar honi chahiye.

# ==========================================
# Pandas DataFrame — pd.DataFrame() Practice
# ==========================================

# Q1. Create a DataFrame using the following dictionary:
# data = {
#     "Product": ["Egg", "Maggi", "Milk"],
#     "Price": [7, 14, 30],
#     "Quantity": [10, 20, 15]
# }
#
# Store the DataFrame in a variable named df.
# Print the complete DataFrame.

# import pandas as pd
# data = {
#     "Product": ["Egg", "Maggi", "Milk"],
#     "Price": [7, 14, 30],
#     "Quantity": [10, 20, 15]
# }
# df = pd.DataFrame(data)
# print(df)
#--------------------------------------------------

# Q2. Create a DataFrame using the following dictionary:
# data = {
#     "Employee": ["Amit", "Ravi", "Neha"],
#     "Department": ["IT", "HR", "Sales"]
# }
#
# Convert the dictionary into a DataFrame.
# Store it in a variable named employees.
# Print the DataFrame.

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Ravi", "Neha"],
#     "Department": ["IT", "HR", "Sales"]
# }
# employees = pd.DataFrame(data)
# print(employees)
#--------------------------------------------------

# Q3. Create a DataFrame using the following dictionary:
# data = {
#     "Student": ["Aman", "Priya", "Rahul"],
#     "Marks": [78, 92, 85]
# }
#
# Create the DataFrame.
# Store it in a variable named students.
# Print the DataFrame.

# import pandas as pd

# data = {
#     "Student": ["Aman", "Priya", "Rahul"],
#     "Marks": [78, 92, 85]
# }
# students = pd.DataFrame(data)
# print(students)
#_______________________________________________________________________________________________

#==============================
# 3. Dictionary se DataFrame
#==============================
# 1. Dictionary se DataFrame kya hota hai?

# Python mein hum dictionary ke andar data store karte hain. 
# Jab hum us dictionary ko pd.DataFrame() mein dete hain, 
# toh Pandas us data ko table mein convert kar deta hai.

# DataFrame mein:

# Dictionary ki keys column names banti hain.
# Dictionary ki list values columns ke andar data banti hain.
# Har list ka pehla element pehli row mein, doosra element doosri
# row mein aata hai, aur isi tarah aage.

# 2. Example se samjho

# Maan lo, humein teen employees ka data store karna hai.

# import pandas as pd

# data = {
#     "Name": ["Vikash", "Mohit", "Ravi"],
#     "Department": ["IT", "HR", "Sales"],
#     "Salary": [25000, 35000, 50000]
# }

# df = pd.DataFrame(data)

# print(df)

# Output:

#      Name Department  Salary
# 0  Vikash         IT   25000
# 1   Mohit         HR   35000
# 2    Ravi      Sales   50000
# 3. Ab code ko step-by-step samjho

# Step 1: Dictionary banao

# data = {
#     "Name": ["Vikash", "Mohit", "Ravi"],
#     "Department": ["IT", "HR", "Sales"],
#     "Salary": [25000, 35000, 50000]
# }

# Yahan teen keys hain: Name, Department aur Salary.

# Yehi DataFrame ke column names banengi.

# Step 2: Dictionary ko DataFrame mein convert karo

# df = pd.DataFrame(data)

# Pandas dictionary ke data ko table mein convert kar deta hai.

# Step 3: DataFrame print karo

# print(df)

# Ab tumhe employees ka data rows aur columns mein dikhai dega.

# 4. Ek important concept

# Dhyan do ki har list ka data apni corresponding row mein aata hai.

# Name	Department	Salary
# Vikash	IT	25000
# Mohit	HR	35000
# Ravi	Sales	50000

# Vikash ka naam, department aur salary ek hi row mein hain. 
# Isi tarah Mohit aur Ravi ka data bhi apni-apni rows mein hai.

# Yaad rakho: Dictionary ki sabhi lists mein aam taur par barabar 
# elements hone chahiye, taaki unhe seedhe DataFrame mein convert kiya ja sake.
#______________________________________________________________________________________________

#==============================
# 4.List of Lists se DataFrame
#==============================

# 1. List of Lists kya hoti hai?

# Jab ek list ke andar multiple lists hoti hain, toh use List of Lists kehte hain.

# Example:

# data = [
#     ["Vikash", 25, "Kolkata"],
#     ["Mohit", 24, "Delhi"],
#     ["Ravi", 26, "Mumbai"]
# ]

# Yahan data ek list hai, jiske andar 3 alag lists hain.

# Har inner list ek employee ya person ka record represent karti hai.

# 2. List of Lists ko DataFrame mein kaise convert karein?

# Dictionary mein column names pehle se keys ke roop mein hote hain. 
# Lekin List of Lists mein column names alag se dene padte hain.

# Example:

# import pandas as pd

# data = [
#     ["Vikash", 25, "Kolkata"],
#     ["Mohit", 24, "Delhi"],
#     ["Ravi", 26, "Mumbai"]
# ]

# df = pd.DataFrame(
#     data,
#     columns=["Name", "Age", "City"]
# )

# print(df)

# Output:

#      Name  Age      City
# 0  Vikash   25   Kolkata
# 1   Mohit   24     Delhi
# 2    Ravi   26    Mumbai
# 3. Code ko step-by-step samjho

# Step 1: Data ko List of Lists mein store kiya.

# data = [
#     ["Vikash", 25, "Kolkata"],
#     ["Mohit", 24, "Delhi"],
#     ["Ravi", 26, "Mumbai"]
# ]

# Step 2: pd.DataFrame() se DataFrame banaya.

# df = pd.DataFrame(
#     data,
#     columns=["Name", "Age", "City"]
# )

# Yahan columns parameter se humne column names diye hain.

# Dhyan do:

# Pehli inner list → pehli row.
# Doosri inner list → doosri row.
# Teesri inner list → teesri row.

# Har inner list ka pehla element Name, 
# doosra Age aur teesra City column mein aata hai.

# Important: Column names ki sankhya har inner list mein 
# maujood elements ki sankhya ke barabar honi chahiye.

# Practice Questions — List of Lists

# Ab tumhari baari! Neeche 3 naye questions hain. Solutions nahi diye gaye hain.

# ==========================================
# Pandas DataFrame — List of Lists Practice
# ==========================================

# Q1. Create a DataFrame from the following list of lists:
# data = [
#     ["Amit", 25000],
#     ["Neha", 32000],
#     ["Ravi", 28000]
# ]

# Use "Employee" and "Salary" as column names.
# Store the DataFrame in a variable named df.
# Print the DataFrame.

# import pandas as pd

# data = [
#     ["Amit", 25000],
#     ["Neha", 32000],
#     ["Ravi", 28000]
# ]

# df = pd.DataFrame(
#     data,
#     columns= ["Employee","Salary" ]
# )
# print(df)
# ------------------------------------------------


# Q2. Create a DataFrame from the following list of lists:
# data = [
#     ["Laptop", 45000, 5],
#     ["Mouse", 500, 20],
#     ["Keyboard", 1200, 10]
# ]

# Use "Product", "Price" and "Stock" as column names.
# Store the DataFrame in a variable named inventory.
# Print the DataFrame.

# import pandas as pd

# data = [
#     ["Laptop", 45000, 5],
#     ["Mouse", 500, 20],
#     ["Keyboard", 1200, 10]
# ]

# inventory = pd.DataFrame(
#     data,
#     columns= ["Product", "Price", "stock"]
# )
# print(inventory)
# ------------------------------------------------------


# Q3. Create a DataFrame from the following list of lists:
# data = [
#     ["Kolkata", 32],
#     ["Delhi", 35],
#     ["Mumbai", 30]
# ]

# Use "City" and "Temperature" as column names.
# Store the DataFrame in a variable named weather.
# Print the DataFrame.

# import pandas as pd

# data = [
#     ["Kolkata", 32],
#     ["Delhi", 35],
#     ["Mumbai", 30]
# ]

# weather = pd.DataFrame(
#     data,
#     columns= ["City", "Temperature"]
# )
# print(weather)
#_________________________________________________________________________________________________________

#==============================
# 5. DataFrame Columns
#==============================

# 1. DataFrame Columns kya hote hain?

# DataFrame mein columns table ke vertical parts hote hain. 
# Har column kisi particular type ki information store karta hai, 
# jaise Name, Age, Salary.

# Example:

# import pandas as pd

# data = {
#     "Name": ["Vikash", "Mohit", "Ravi"],
#     "Age": [25, 24, 26],
#     "Salary": [25000, 35000, 50000]
# }

# df = pd.DataFrame(data)

# print(df)

# Output:

#      Name  Age  Salary
# 0  Vikash   25   25000
# 1   Mohit   24   35000
# 2    Ravi   26   50000

# Is table mein 3 columns hain:

# Name
# Age
# Salary
# 2. Column names kaise dekhein?

# Agar tumhe sirf DataFrame ke column names dekhne hain, toh df.columns use kar sakte ho.

# print(df.columns)

# Output:

# Index(['Name', 'Age', 'Salary'], dtype='object')

# Yahan df.columns DataFrame ke saare column names dikhata hai.

# Dhyan do: columns ek attribute hai, isliye df.columns likhte hain, df.columns() nahi.

# 3. Column names ko Python list mein kaise dekhein?

# Kabhi-kabhi column names ko normal Python list mein rakhna useful hota hai. 
# Iske liye list() use kar sakte hain.

# print(list(df.columns))

# Output:

# ['Name', 'Age', 'Salary']

# Ab column names ek normal Python list ke form mein milenge.

# Yaad rakho:

# df.columns → column names dikhata hai.
# list(df.columns) → column names ko Python list mein convert karta hai.
# Practice Questions — DataFrame Columns

# Ab tum khud solve karna. Solutions pehle se nahi diye gaye hain.

# ==========================================
# Pandas DataFrame — Columns Practice
# ==========================================

# Q1. Create a DataFrame using this dictionary:
# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard"],
#     "Price": [45000, 500, 1200],
#     "Stock": [5, 20, 10]
# }
#
# Print only the column names using the appropriate attribute.

# import pandas as pd
# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard"],
#     "Price": [45000, 500, 1200],
#     "Stock": [5, 20, 10]
# }
# df = pd.DataFrame(data)
# print(df.columns)
#--------------------------------------------------

# Q2. Create a DataFrame using this dictionary:
# data = {
#     "Student": ["Aman", "Priya", "Rahul"],
#     "Marks": [78, 92, 85],
#     "Grade": ["B", "A", "A"]
# }
#
# Convert the dictionary into a DataFrame.
# Print the column names as a normal Python list.

# import pandas as pd
# data = {
#     "Student": ["Aman", "Priya", "Rahul"],
#     "Marks": [78, 92, 85],
#     "Grade": ["B", "A", "A"]
# }

# df = pd.DataFrame(data)
# print(list(df.columns))
#--------------------------------------------------------

# Q3. Create a DataFrame using this dictionary:
# data = {
#     "City": ["Kolkata", "Delhi", "Mumbai"],
#     "Temperature": [32, 35, 30]
# }
#
# Convert the dictionary into a DataFrame.
# Print the column names using the appropriate attribute.
# Do not print the complete DataFrame.

# import pandas as pd

# data = {
#     "City": ["Kolkata", "Delhi", "Mumbai"],
#     "Temperature": [32, 35, 30]
# }

# dataframe = pd.DataFrame(data)
# print(dataframe.columns)
#______________________________________________________________________________________________________

#==============================
# 6. DataFrame Index
#==============================

# 1. DataFrame Index kya hota hai?

# Pandas DataFrame mein Index rows ko identify karne ke liye labels deta hai.

# Jab hum DataFrame banate hain aur khud se koi index nahi dete, 
# toh Pandas automatically 0, 1, 2, 3... index bana deta hai.

# Example:

# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard"],
#     "Price": [45000, 500, 1200]
# }

# df = pd.DataFrame(data)

# print(df)

# Output:

#     Product  Price
# 0    Laptop  45000
# 1     Mouse    500
# 2  Keyboard   1200

# Dhyan se dekho:

# Index	Product	Price
# 0	Laptop	45000
# 1	Mouse	500
# 2	Keyboard	1200

# Yahan 0, 1, 2 DataFrame ke row index hain.

# 0 → Laptop wali row
# 1 → Mouse wali row
# 2 → Keyboard wali row

# Index khud DataFrame ka normal column nahi hota. 
# Yeh rows ko identify karne ke liye hota hai.

# 2. df.index kya karta hai?

# DataFrame ke index labels dekhne ke liye hum df.index use karte hain.

# print(df.index)

# Output:

# RangeIndex(start=0, stop=3, step=1)

# Iska matlab:

# start=0 → Index 0 se shuru hai.
# stop=3 → Index 3 se pehle tak hai; yaani 0, 1, 2.
# step=1 → Har index mein 1 ka increment hai.

# Agar tumhe index ko Python list mein dekhna hai, toh:

# print(list(df.index))

# Output:

# [0, 1, 2]

# Yaad rakho:

# df.columns → Column names dikhata hai.
# df.index → Row index labels dikhata hai.

# Dono attributes hain, isliye inke saath parentheses () nahi lagate.

# Pandas DataFrame — Index Practice Questions

# Ab ye 3 questions khud solve karo. Abhi solutions nahi diye hain.

# ==========================================
# Pandas DataFrame — Index Practice
# ==========================================

# Q1. Create a DataFrame using a dictionary.
# Columns: Employee, Salary
# Employees: Amit, Neha, Rahul, Priya
# Salaries: 25000, 32000, 28000, 35000
# Print the DataFrame and observe its default index.

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Rahul", "Priya"],
#     "Salary": [25000, 32000, 28000, 35000]
# }

# df = pd.DataFrame(data)

# print(df)
#---------------------------------------------

# Q2. Create a DataFrame using a dictionary.
# Columns: City, Population
# Cities: Kolkata, Delhi, Mumbai
# Population: 45, 80, 60
# Print only the DataFrame index using df.index.

# import pandas as pd
# data = {
#     "Cities": ["Kolkata", "Delhi", "Mumbai"],
#     "Population": [ 45, 80, 60]
# }
# df = pd.DataFrame(data)
# print(df.index)
#-------------------------------------------------

# Q3. Create a DataFrame using a dictionary.
# Columns: Subject, Marks
# Subjects: Python, SQL, Excel, Power BI
# Marks: 85, 90, 78, 88
# Convert the DataFrame index into a Python list
# and print the list.

# import pandas as pd

# data = {
#     "Subjects": ["Python", "SQL", "Excel", "Power BI"],
#     "Marks": [85, 90, 78, 88]
# }

# df = pd.DataFrame(data)

# print(list(df.index))
#_______________________________________________________________________________________________________

#==============================
# 7. DataFrame Shape
#==============================

# DataFrame Shape kya hota hai?

# DataFrame ka shape batata hai ki usmein kitni rows aur kitne columns hain.

# Pandas mein iske liye hum .shape attribute use karte hain.

# Example:

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Rahul", "Priya"],
#     "Salary": [25000, 32000, 28000, 35000],
#     "City": ["Kolkata", "Delhi", "Mumbai", "Pune"]
# }

# df = pd.DataFrame(data)

# print(df)
# print(df.shape)

# Output:

#   Employee  Salary      City
# 0     Amit   25000   Kolkata
# 1     Neha   32000     Delhi
# 2    Rahul   28000    Mumbai
# 3    Priya   35000      Pune

# (4, 3)
# 2. (4, 3) ka kya matlab hai?

# Shape hamesha is order mein hota hai:

# (rows, columns)

# Is example mein:

# 4 → 4 rows hain.
# 3 → 3 columns hain.

# Yaad rakho: Pehle rows, phir columns.

# 3. Sirf rows ya columns ki sankhya kaise nikalein?
# print(df.shape[0])  # Rows ki sankhya
# print(df.shape[1])  # Columns ki sankhya

# Output:

# 4
# 3

# Samjho:

# df.shape[0] → Pehli value, yani rows.
# df.shape[1] → Doosri value, yani columns.

# Ek important baat: .shape ek attribute hai, method nahi. 
# Isliye df.shape likhenge, df.shape() nahi.

# Pandas DataFrame — Shape Practice Questions

# Ab ye 3 questions khud solve karo. Solutions abhi nahi diye hain.

# ==========================================
# Pandas DataFrame — Shape Practice
# ==========================================

# Q1. Create a DataFrame using a dictionary.
# Columns: Product, Price
# Products: Laptop, Mouse, Keyboard, Monitor, Printer
# Prices: 45000, 500, 1200, 12000, 8000
# Print the DataFrame shape.

# import pandas as pd
# data = {
#     "Products": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printe"],
#     "Prices": [45000, 500, 1200, 12000, 8000]
# }
# df = pd.DataFrame(data)

# print(df.shape)
#--------------------------------------------

# Q2. Create a DataFrame using a dictionary.
# Columns: Student, Marks, City
# Students: Amit, Neha, Rahul
# Marks: 85, 92, 78
# Cities: Kolkata, Delhi, Mumbai
# Print the number of rows using shape.

# import pandas as pd
# data = {
#     "Students": ["Amit", "Neha", "Rahul"],
#     "Marks": [85, 92, 78],
#     "Cities": [ "Kolkata", "Delhi", "Mumbai"]
# }
# df = pd.DataFrame(data)
# print(df.shape[0])
#-------------------------------------------

# Q3. Create a DataFrame using a dictionary.
# Columns: Department, Employees
# Departments: IT, HR, Sales, Finance
# Employees: 12, 8, 15, 6
# Print the number of columns using shape.

# import pandas as pd
# data = {
#     "Departments": ["IT", "HR", "Sales", "Finance"],
#     "Employees": [12, 8, 15, 6]
# }
# df = pd.DataFrame(data)
# print(df.shape[1])
#_________________________________________________________________________________________________

#==============================
# 8. DataFrame Size
#==============================

# 1. DataFrame Size kya hota hai?

# Pandas mein .size attribute batata hai ki DataFrame mein total kitne elements (cells) hain.

# Yaani rows aur columns ko mila kar jitne bhi individual values hain, unki total sankhya.

# Example:

# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard"],
#     "Price": [45000, 500, 1200]
# }

# df = pd.DataFrame(data)

# print(df)
# print(df.size)

# Output:

#     Product  Price
# 0    Laptop  45000
# 1     Mouse    500
# 2  Keyboard   1200

# 6
# 2. Output 6 kyun aaya?

# DataFrame mein:

# Rows = 3
# Columns = 2
# Har row mein 2 cells hain.

# Isliye total cells = 3 × 2 = 6.

# Yahi value df.size return karta hai.

# 3. shape aur size mein difference
# Attribute	Kya batata hai?	Example output
# df.shape	Rows aur columns ki sankhya	(3, 2)
# df.size	Total cells/elements	6

# Yaad rakhne ka easy tareeka:

# Shape → DataFrame ka structure: rows aur columns.
# Size → DataFrame mein total values.

# Ek aur baat: .size bhi ek attribute hai, isliye df.size likhenge, df.size() nahi.

# Pandas DataFrame — Size Practice Questions

# Ab ye 3 questions khud solve karo. Solutions abhi nahi diye hain.

# ==========================================
# Pandas DataFrame — Size Practice
# ==========================================

# Q1. Create a DataFrame using a dictionary.
# Columns: Product, Stock, Price
# Products: Laptop, Mouse, Keyboard
# Stock: 10, 25, 15
# Prices: 45000, 500, 1200
# Print the total number of elements.

# import pandas as pd
# data = {
#     "Products": ["Laptop", "Mouse", "Keyboard"],
#     "Stock": [10, 25, 15],
#     "Prices": [45000, 500, 1200]
# }
# df = pd.DataFrame(data)
# print(df.size)
#-------------------------------------------------

# Q2. Create a DataFrame using a dictionary.
# Columns: Name, Age
# Names: Amit, Neha, Rahul, Priya
# Ages: 25, 24, 26, 23
# Print both the DataFrame shape and size.

# import pandas as pd
# data ={
#     "Names": ["Amit", "Neha", "Rahul", "Priya"],
#     "Ages": [25, 24, 26, 23]
# }
# df = pd.DataFrame(data)
# print(df.shape)
# print(df.size)
#-----------------------------------------------------

# Q3. Create a DataFrame using a dictionary.
# Columns: City, Temperature, Humidity, Rainfall
# Cities: Kolkata, Delhi
# Temperature: 32, 35
# Humidity: 75, 60
# Rainfall: 12, 5
# Print the total number of elements using df.size.

# import pandas as pd
# data ={
#     "Cities": ["Kolkata", "Delhi"],
#     "Temperature": [32, 35],
#     "Humidity": [75, 60],
#     "Rainfall": [12, 5]
# }
# df = pd.DataFrame(data)
# print(df.size)
#________________________________________________________________________________________________-

#==============================
# 9. DataFrame dtypes
#==============================

# dtypes kya hota hai?

# Pandas mein df.dtypes batata hai ki DataFrame ke har column mein kis type ka data hai.

# Data Analyst ke liye yeh important hai, 
# kyunki data analyse karne se pehle humein pata hona 
# chahiye ki column mein numbers hain, text hai ya decimal values hain.

# 2. Example se samjho
# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Rahul"],
#     "Age": [25, 24, 26],
#     "Salary": [25000.50, 32000.75, 28000.25],
#     "Permanent": [True, False, True]
# }

# df = pd.DataFrame(data)

# print(df)
# print(df.dtypes)

# Output:

#   Employee  Age    Salary  Permanent
# 0     Amit   25  25000.50       True
# 1     Neha   24  32000.75      False
# 2    Rahul   26  28000.25       True

# Employee      object
# Age            int64
# Salary       float64
# Permanent       bool
# dtype: object
# 3. Output ko samjho
# Column	Data type	Meaning
# Employee	object	Text values
# Age	int64	Whole numbers
# Salary	float64	Decimal numbers
# Permanent	bool	True ya False

# Important: int64 aur float64 numbers ke data types hain. 
# Pandas mein text columns aksar object dikhate hain; 
# kuch situations mein string dtype bhi mil sakta hai.

# 4. dtype aur dtypes mein difference

# Python aur Pandas mein naam milte-julte hain, lekin use alag hai.

# df.dtypes → DataFrame ke saare columns ke data types batata hai.
# df["Age"].dtype → Sirf Age column ka data type batata hai.

# Example:

# print(df.dtypes)
# print(df["Age"].dtype)

# Output ki last line:

# int64

# Yaad rakho, dtypes aur dtype dono attributes hain, isliye inke saath () nahi lagate.

# Pandas DataFrame — dtypes Practice Questions

# Ab ye 3 questions khud solve karo. Solutions abhi nahi diye hain.

# ==========================================
# Pandas DataFrame — dtypes Practice
# ==========================================

# Q1. Create a DataFrame using a dictionary.
# Columns: Student, Marks, Passed
# Students: Amit, Neha, Rahul
# Marks: 85, 92, 67
# Passed: True, True, False
# Print the data type of every column using dtypes.

# import pandas as pd
# data = {
#     "Student": ["Amit", "Neha", "Rahul"],
#     "Marks": [67, 92, 85],
#     "Passed": ["True", "True", "False"]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df.dtypes)
#------------------------------------------------

# Q2. Create a DataFrame using a dictionary.
# Columns: Product, Quantity, Price
# Products: Laptop, Mouse, Keyboard
# Quantity: 5, 10, 8
# Price: 45000.50, 500.75, 1200.25
# Print only the data type of the Quantity column.

# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard"],
#     "Quantity": [5, 10, 8],
#     "Price": [45000.50, 500.75, 1200.25]
# }

# df = pd.DataFrame(data)

# print(df["Quantity"].dtype)


#---------------------------------------------

# Q3. Create a DataFrame using a dictionary.
# Columns: City, Temperature
# Cities: Kolkata, Delhi, Mumbai
# Temperature: 32.5, 35.2, 30.8
# Print the data types of all columns.

# import pandas as pd

# data = {
#     "City": ["Kolkata", "Delhi", "Mumbai"],
#     "Temperature": [32.5, 35.2, 30.8]
# }

# dataframe = pd.DataFrame(data)
# print(dataframe.dtypes)