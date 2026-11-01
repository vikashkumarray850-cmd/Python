# ========================================
# CODE NUMBERING BY:-

#  16 TO 153     pd.read_csv()
#  157 TO 286    CSV file read 
#  290 TO 367    pd.read_excel()
#  370 TO 533    Excel file read 
#  537 TO 669    File path 
#  673 TO 807    Data ko inspect
# ========================================

#==============================
# Topic 1: pd.read_csv()
#==============================

# 1. CSV file kya hoti hai?

# CSV ka full form Comma-Separated Values hai.

# CSV ek file format hai jisme data rows aur columns mein store hota hai.
# Aksar values commas se separate hoti hain.

# Maan lo tumhare paas employees.csv naam ki file hai:

# Employee,Department,Salary
# Amit,IT,25000
# Neha,HR,32000
# Rahul,Sales,28000
# Priya,IT,35000

# Is file mein:

# Employee, Department, Salary column names hain.
# Har agali line ek employee ka record hai.
# Har record mein employee ka naam, department aur salary hai.

# Data Analyst ko aksar CSV files mein sales, employees, 
# customers aur products ka data milta hai.
# Pandas se hum is data ko read karke analyse kar sakte hain.

# 2. pd.read_csv() kya karta hai?

# pd.read_csv() ka use CSV file ko read karke Pandas 
# DataFrame mein convert karne ke liye hota hai.

# Example:

# Maan lo employees.csv file tumhare Python script ke same folder mein hai.

# import pandas as pd

# df = pd.read_csv("employees.csv")

# print(df)

# Output:

#   Employee Department  Salary
# 0     Amit         IT   25000
# 1     Neha         HR   32000
# 2    Rahul      Sales   28000
# 3    Priya         IT   35000

# Samjho code mein kya hua:

# import pandas as pd — Pandas library import ki.
# pd.read_csv("employees.csv") — CSV file read ki.
# df = ... — Read kiye gaye data ko df variable mein store kiya.
# print(df) — DataFrame display kiya.

# Dhyan do: CSV file mein humne index nahi diya tha, 
# lekin Pandas ne automatically 0, 1, 2, 3 index bana diya.

# 3. Agar CSV file doosre folder mein ho toh?

# Maan lo tumhari file DataFiles folder ke andar hai:

# C:\PYTHON 37\
#     read_data.py
#     DataFiles\
#         employees.csv

# Tab relative path se file read kar sakte ho:

# df = pd.read_csv("DataFiles/employees.csv")

# Agar file ka path galat hua, toh Pandas file nahi 
# dhoondh payega aur error aa sakta hai.

# Important: pd.read_csv() sirf file ka naam nahi, 
# balki file ka path bhi accept karta hai.

# Pandas — Reading Data Practice Questions

# Ab ye 3 questions khud solve karo. Abhi solutions nahi diye hain.

# ==========================================
# Pandas Reading Data — Practice
# ==========================================

# Q1. Assume that "sales.csv" is in the same folder
# as your Python script.
# Import pandas and read the CSV file into a DataFrame
# named df.
# Print the DataFrame.

# import pandas as pd

# df = pd.read_csv("employees.csv")
# print(df)
#----------------------------------------

# Q2. Assume that "customers.csv" is inside a folder
# named "DataFiles".
# Read the CSV file into a DataFrame named customers_df.
# Print the DataFrame.

# import pandas as pd
# df = pd.read_csv("customer.csv")
# print(df)
#---------------------------------------------

# Q3. Assume that "products.csv" is inside a folder
# named "DataFiles".
# Read the CSV file into a DataFrame named products_df.
# Print only the DataFrame columns.

# import pandas as pd
# df = pd.read_csv("products.csv")
# print(df)
#+______________________________________________________________________________________________________+

#==============================
# Topic 2: CSV File Read
#==============================

# 1. CSV file ko DataFrame mein kaise read karein?

# Agar customers.csv tumhari Python file ke same folder mein hai, toh:

# import pandas as pd

# customers_df = pd.read_csv("customers.csv")

# print(customers_df)

# Isse CSV ka data Pandas DataFrame mein aa jayega.

# 2. Sirf kuch information check karna

# Saare column names dekhne ke liye:

# print(customers_df.columns)

# Rows aur columns ki sankhya dekhne ke liye:

# print(customers_df.shape)

# Dhyan rahe: shape hum pehle padh chuke hain. Yahan use sirf
# CSV read karne ke baad data check karne ke liye kar rahe hain.

# Practice Questions — Reading CSV Files

# In questions ko customers.csv file ka use karke solve karo.

# ==========================================
# Pandas — Reading CSV Practice
# ==========================================

# Q1. Read "customers.csv" into a DataFrame
# named customers_df.
# Print the complete DataFrame.

# import pandas as pd

# customer_df = pd.read_csv("customer.csv")
# print(customer_df)
#-----------------------------------------

# Q2. Read "customers.csv" into a DataFrame.
# Print only the column names.

# import pandas as pd
# df = pd.read_csv("customer.csv")
# print(df.columns)
#------------------------------------

# Q3. Read "customers.csv" into a DataFrame.
# Print the number of rows and columns.

# import pandas as pd
# df = pd.read_csv("customer.csv")
# print(df.shape)
#__________________________________________________________________________________________________________

#==============================
# Topic 3: pd.read_excel()
#==============================


# 1. pd.read_excel() kya hota hai?

# Jaise hum pd.read_csv() se CSV file read karte hain, 
# waise hi pd.read_excel() ka use Excel file ko Pandas 
# DataFrame mein read karne ke liye hota hai.

# Excel files ke common extensions hain:

# .xlsx
# .xls

# Data Analyst ko company ki sales reports, 
# employee records aur financial reports aksar Excel files mein milti hain.

# 2. Excel file ko kaise read karein?

# Maan lo tumhare paas employees.xlsx naam ki Excel file hai.

# Usmein ye data hai:

# Employee	Department	Salary
# Amit	IT	25000
# Neha	HR	32000
# Rahul	Sales	28000
# Priya	IT	35000

# Agar Excel file tumhari Python script ke same folder mein hai, toh:

# import pandas as pd

# df = pd.read_excel("employees.xlsx")

# print(df)

# Pandas Excel file ka data read karke DataFrame mein store kar dega.

# 3. Agar error aaye toh?

# Excel files read karne ke liye aksar openpyxl 
# package chahiye hota hai, khaaskar .xlsx files ke liye.

# VS Code ke terminal mein install karo:

# python -m pip install openpyxl

# Installation ke baad dobara Python code run karo.

# 4. CSV aur Excel mein difference
# CSV	Excel
# pd.read_csv()	pd.read_excel()
# .csv file	.xlsx ya .xls file
# Comma-separated text data	Spreadsheet workbook
# read_csv("file.csv")	read_excel("file.xlsx")

# Yaad rakho: File ka actual naam aur extension code mein sahi hona chahiye.

# Pandas — Excel Reading Practice Questions
# ==========================================
# Pandas — read_excel() Practice
# ==========================================

# Q1. Read "employees.xlsx" into a DataFrame
# named employees_df.
# Print the complete DataFrame.

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx")
# print(employees_df)
#-------------------------------------------

# Q2. Read "sales.xlsx" into a DataFrame
# named sales_df.
# Print the DataFrame columns.

# import pandas as pd
# sales_df = pd.read_excel("sales.xlsx")
# print(sales_df.columns)
#----------------------------------------

# Q3. Read "products.xlsx" into a DataFrame
# named products_df.
# Print the DataFrame shape.

# import pandas as pd
# products_df = pd.read_excel("products.xlsx")
# print(products_df.shape)
#____________________________________________________________________________________________________________

#==============================
# Topic 5 — File Path
#==============================

# 1. File Path kya hota hai?

# File Path ka matlab hai kisi file ka computer mein location, yani file kahan save hai.

# Maan lo tumhari Excel file yahan save hai:

# C:\PYTHON 37\sales.xlsx

# Ismein:

# C:\ → Drive
# PYTHON 37 → Folder ka naam
# sales.xlsx → Excel file ka naam

# Python ko file read karne ke liye uski location pata honi chahiye.

# 2. Relative Path kya hota hai?

# Agar tumhari Python file aur Excel file ek hi folder mein hain, 
# toh sirf file ka naam likh sakte ho.

# Maan lo dono files C:\PYTHON 37 mein hain:

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")
# print(sales_df)

# Yahan "sales.xlsx" ek relative path hai.

# Python current working directory mein sales.xlsx ko dhoondhega.

# Dhyan do: Current working directory zaroori nahi ki hamesha tumhari Python script wala folder hi ho.

# 3. Absolute Path kya hota hai?

# Jab hum file ki poori location likhte hain, use absolute path kehte hain.

# Example:

# import pandas as pd

# sales_df = pd.read_excel(r"C:\PYTHON 37\sales.xlsx")
# print(sales_df)

# Yahan r ka use Windows path mein backslashes ko safely handle karne ke liye kiya gaya hai.

# Ek aur tarika:

# sales_df = pd.read_excel("C:/PYTHON 37/sales.xlsx")

# Forward slashes / bhi use kar sakte ho.

# 4. File nahi milne par kya hoga?

# Agar Python ko file diye gaye path par nahi milti, toh aam taur par FileNotFoundError aayega.

# Example:

# sales_df = pd.read_excel("wrong_file.xlsx")

# Agar wrong_file.xlsx us location par nahi hai, toh error aayega.

# Important: File ka naam aur extension bilkul match hone chahiye, 
# jaise sales.xlsx aur sales.csv alag files hain.

# Practice Questions — File Path

# Neeche 3 questions hain. Pehle khud solve karna; abhi solutions nahi diye gaye hain.

# ==========================================
# Pandas — File Path Practice
# ==========================================

# Q1. Read "employees.xlsx" using a relative path.
# Store the DataFrame in employees_df.
# Print the complete DataFrame.

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx")
# print(employees_df)
#------------------------------------------
# Q2. Read "sales.xlsx" using the absolute path:
# C:\PYTHON 37\sales.xlsx
# Store the DataFrame in sales_df.
# Print the DataFrame shape.

# import pandas as pd

# sales_df = pd.read_excel(r"C:\PYTHON 37\sales.xlsx")
# print(sales_df.shape)
#---------------------------------------------
# Q3. Read "products.xlsx" using a relative path.
# Store the DataFrame in products_df.
# Print the DataFrame columns.

# import pandas as pd

# products_df = pd.read_excel("products.xlsx")
# print(products_df.columns)
#_____________________________________________________________________________________________

#==============================
# Topic 6 — Data ko Inspect
#==============================

# 1. Data Inspect karna kya hota hai?

# Jab hum CSV ya Excel file ko Pandas mein read karte hain, 
# toh analysis karne se pehle data ko check karna zaroori hota hai.

# Hum dekhte hain:

# Data mein kya hai?
# Kitni rows aur columns hain?
# Column names kya hain?
# Data types kya hain?
# Data sahi tarah load hua hai ya nahi?

# Data ko check karne ke is process ko Data Inspection kehte hain.

# 2. Example DataFrame

# Maan lo hamare paas sales.xlsx file hai.

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")

# print(sales_df)

# Ab hum alag-alag commands se data inspect kar sakte hain.

# A. head() — Shuru ki 5 rows

# print(sales_df.head())

# head() default mein pehli 5 rows dikhata hai.

# Agar pehli 3 rows dekhni hain:

# print(sales_df.head(3))

# B. tail() — Aakhri 5 rows

# print(sales_df.tail())

# Agar aakhri 2 rows dekhni hain:

# print(sales_df.tail(2))

# C. shape — Rows aur Columns

# print(sales_df.shape)

# Example output:

# (8, 4)

# Iska matlab 8 rows aur 4 columns hain.

# D. columns — Column Names

# print(sales_df.columns)

# Isse DataFrame ke saare column names milte hain.

# E. dtypes — Data Types

# print(sales_df.dtypes)

# Isse pata chalta hai ki har column ka data type kya hai, 
# jaise integer, float ya string/object.

# 3. Data Inspection ka Combined Example

# Ek hi baar mein saari commands run karke dekho:

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")

# print(sales_df.head())
# print(sales_df.tail())
# print(sales_df.shape)
# print(sales_df.columns)
# print(sales_df.dtypes)

# Abhi humne head(), tail(), shape, columns aur dtypes revise kiye. 
# info() aur describe() ko hum apne roadmap ke Section 5: 
# Inspecting Data mein detail se padhenge.

# Practice Questions — Data Inspection
# ==========================================
# Pandas — Data Inspection Practice
# ==========================================

# Q1. Read "employees.xlsx" into employees_df.
# Display the first 3 rows.

# import pandas as pd
# employees_df = pd.read_csv("employees.csv")
# print(employees_df.head(3))
#--------------------------------------------------------

# Q2. Read "sales.xlsx" into sales_df.
# Display the last 2 rows.
# Print the number of rows and columns.

# import pandas as pd
# sales_df = pd.read_csv("sales.csv")
# print(sales_df.tail(2))
#----------------------------------------------

# Q3. Read "products.xlsx" into products_df.
# Print all column names and their data types.

# import pandas as pd
# products_df = pd.read_csv("products.csv")
# print(products_df.dtypes)
# print(products_df.columns)
#__________________________________________________________________________________________________

