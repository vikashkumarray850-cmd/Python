# ========================================
# CODE NUMBERING BY:-

# 1 Missing Values       [29 TO 139] 
# 2 isna()               [143 TO 248]
# 3 isnull()             [252 TO 304]
# 4 notna()              [309 TO 411]
# 5 Missing Value Count  [415 TO 515]
# 6 fillna()             [519 TO 645]
# 7 dropna()             [649 TO 772]
# =========================================

# | No. | Topic                    | Kya seekhenge?                                         |
# | --- | ------------------------ | ------------------------------------------------------ |
# | 1   | Missing Values           | Missing data kya hota hai aur kyun hota hai            |
# | 2   | `isna()`                 | Missing values ko identify karna                       |
# | 3   | `isnull()`               | Missing values check karna                             |
# | 4   | `notna()`                | Jo values missing nahi hain, unhe identify karna       |
# | 5   | **Missing Values Count** | Har column mein kitni values missing hain, count karna |
# | 6   | `fillna()`               | Missing values ko fill karna                           |
# | 7   | `dropna()`               | Missing values wali rows ya columns remove karna       |


#_____________________________________________________________________________________________________

#==============================
# Section 11 — Missing Data
#--------------------------
# Topic 1: Missing Values
#==============================

# Missing Values kya hoti hain?

# Jab kisi DataFrame ke kisi cell mein value available nahi hoti, use Missing Value kehte hain.

# Maan lo ek company ka employee data hai:

# Index	Employee	Department	Salary
# 0	Amit	IT	25000
# 1	Neha	HR	NaN
# 2	Rahul	NaN	28000
# 3	Priya	IT	NaN

# Yahan:

# Neha ki Salary missing hai.
# Rahul ka Department missing hai.
# Priya ki Salary missing hai.

# NaN ka matlab: Not a Number. Pandas mein ye missing numeric 
# values ko represent karne ke liye bhi use hota hai.

# 2. Missing Values kyun hoti hain?

# Real-world data mein missing values kai reasons se ho sakti hain:

# Customer ne koi information nahi di.
# Data entry karte waqt value chhoot gayi.
# Kisi system se data collect nahi ho paya.
# Data merge karne ke baad kuch records ki information match nahi hui.

# Data Analyst ko analysis karne se pehle missing values ko identify karna chahiye, 
# kyunki ye calculations aur reports ko affect kar sakti hain.

# 3. Python mein Missing Value wala DataFrame banana
# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Rahul", "Priya"],
#     "Department": ["IT", "HR", None, "IT"],
#     "Salary": [25000, None, 28000, None]
# }

# df = pd.DataFrame(data)

# print(df)

# Yahan None ka use missing value create karne ke liye kiya hai. 
# Pandas ise aam taur par DataFrame mein NaN ya kisi doosre missing-value 
# representation ke roop mein dikhayega, data type ke hisaab se.

# Practice Questions — Missing Values Basic

# Ab ye 3 questions khud solve karo. Solutions abhi nahi diye gaye hain.

# ==========================================
# Pandas — Section 11: Missing Values
# ==========================================

# Q1. Create a DataFrame with these records:
# Employee: Amit, Neha, Rahul
# Salary: 25000, None, 30000
# Department: IT, HR, Sales
# Print the DataFrame.

# import pandas as pd

# data ={
#     "Employee"  :   ["Amit", "Neha", "Rahul"],
#     "Salary"    :   [25000, None, 30000],
#     "Department":   ["IT", "HR", "Sale"]
# }
# df = pd.DataFrame(data)
# print(df)
# ----------------------------------------------

# Q2. Create a DataFrame with these records:
# Product: Laptop, Mouse, Keyboard
# Price: 45000, 600, None
# Stock: 10, None, 25
# Print the DataFrame.

# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard"],
#     "Price"  : [45000, 600, None],
#     "Stock"  : [10, None, 25]
# }
# df = pd.DataFrame(data)
# print(df)
# -----------------------------------------------

# Q3. Create a DataFrame with these records:
# Student: Ravi, Mohit, Priya
# Marks: 80, None, 90
# City: Kolkata, Delhi, None
# Print the DataFrame.

# import pandas as pd

# data = {
#     "Student" : ["Ravi", "Mohit", "Priya"],
#     "Marks "  : [80, None, 90],
#     "City"    : ["Kolkata", "Delhi", None]
# }

# df = pd.DataFrame(data)
# print(df)
#_____________________________________________________________________________________________________

#==============================
# Topic 2 — isna()
#==============================

# Ab missing values ko identify karna seekhte hain.

# Maan lo hamara DataFrame hai:

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Rahul"],
#     "Salary": [25000, None, 30000],
#     "Department": ["IT", "HR", None]
# }

# df = pd.DataFrame(data)

# print(df)

# Output:

# Index	Employee	Salary	Department
# 0	Amit	25000	IT
# 1	Neha	NaN	HR
# 2	Rahul	30000	None
# isna() kya karta hai?

# isna() check karta hai ki DataFrame ke kis cell mein missing value hai.

# print(df.isna())

# Output:

# Index	Employee	Salary	Department
# 0	False	False	False
# 1	False	True	False
# 2	False	False	True

# Samjho:

# True = value missing hai.
# False = value missing nahi hai.

# Is example mein Neha ki Salary aur Rahul ka Department missing hai.

# Practice Questions — isna()
# ==========================================
# Pandas — Section 11: isna()
# ==========================================

# Q1. Create a DataFrame with these records:
# Employee: Amit, Neha, Rahul
# Salary: 25000, None, 30000
# Department: IT, HR, None
# Use isna() to identify missing values.
# # Print the result.

# import pandas as pd

# data ={
#     "Employee"  :   ["Amit", "Neha", "Rahul"],
#     "Salary"    :   [25000, None, 30000],
#     "Department":   ["IT", "HR", "Sale"]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df.isna())
#-------------------------------------------

# Q2. Create a DataFrame with these records:
# Product: Laptop, Mouse, Keyboard
# Price: 45000, None, 1200
# Stock: None, 40, 25
# Use isna() to identify missing values.
# Print the result.

# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard"],
#     "Price"  : [45000, None, 1200],
#     "Stock"  : [None, 40, 25]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df.isna())
#---------------------------------------------

# Q3. Create a DataFrame with these records:
# Student: Ravi, Mohit, Priya
# Marks: 80, None, 90
# City: Kolkata, Delhi, None
# Use isna() to identify missing values.
# Print the result.

# import pandas as pd

# data = {
#     "Student" : ["Ravi", "Mohit", "Priya"],
#     "Marks "  : [80, None, 90],
#     "City"    : ["Kolkata", "Delhi", None]
# }

# df = pd.DataFrame(data)
# print(df)
# print(df.isna())
#_____________________________________________________________________________________________________

#==============================
# Topic 3 — isnull()
#==============================

# Ab ek simple concept: isnull() aur isna() dono ka kaam same hai.

# Example:

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Rahul"],
#     "Salary": [25000, None, 30000]
# }

# df = pd.DataFrame(data)

# print(df.isna())
# print(df.isnull())

# Dono commands same result dengi:

# Index	Employee	Salary
# 0	False	False
# 1	False	True
# 2	False	False

# Yaad rakho:

# isna() → missing values check karta hai.
# isnull() → missing values check karta hai.
# Dono equivalent hain; inke results same hote hain.
# Practice Questions — isnull()
# ==========================================
# Pandas — Section 11: isnull()
# ==========================================

# Q1. Create a DataFrame with these records:
# Employee: Amit, Neha, Rahul
# Salary: 25000, None, 30000
# Use isnull() to identify missing values.
# Print the result.

# import pandas as pd

# data ={
#     "Employee"  :   ["Amit", "Neha", "Rahul"],
#     "Salary"    :   [25000, None, 30000]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df.isnull())

# ISNA(), ISNULL() YE DONO SAME HI KAAM KARTA HAI ISLIYE HUM EK HI QUESTION KARENGE ....

#_____________________________________________________________________________________________________

#==============================
# Topic 4: notna()
#==============================

# notna() kya karta hai?

# notna() check karta hai ki kaun-si values missing nahi hain.

# True → value available hai.
# False → value missing hai.

# Example:

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Rahul"],
#     "Salary": [25000, None, 30000],
#     "Department": ["IT", "HR", None]
# }

# df = pd.DataFrame(data)

# print(df.notna())

# Output:

# Index	Employee	Salary	Department
# 0	True	True	True
# 1	True	False	True
# 2	True	True	False

# Samjho:

# Amit ki saari values available hain, isliye True.
# Neha ki Salary missing hai, isliye wahan False.
# Rahul ka Department missing hai, isliye wahan False.
# 2. isna() aur notna() mein difference
# Method	True ka matlab
# isna()	Value missing hai
# notna()	Value missing nahi hai

# Dono ek-doosre ke opposite results dete hain.

# Practice Questions — notna()
# ==========================================
# Pandas — Section 11: notna()
# ==========================================

# Q1. Create a DataFrame with these records:
# Employee: Amit, Neha, Rahul
# Salary: 25000, None, 30000
# Department: IT, HR, None
# Use notna() to identify available values.
# Print the result.

# import pandas as pd

# data ={
#     "Employee"  :   ["Amit", "Neha", "Rahul"],
#     "Salary"    :   [25000, None, 30000],
#     "Department":   ["IT", "HR", None]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df.notna())
#-----------------------------------------------

# Q2. Create a DataFrame with these records:
# Product: Laptop, Mouse, Keyboard
# Price: None, 600, 1200
# Stock: 10, None, 25
# Use notna() to identify available values.
# Print the result.

# import pandas as pd

# data ={
#     "Product"  :   ["Laptop", "Mouse", "Keyboard"],
#     "Price"    :   [None, 600, 12000],
#     "Stock"    :   [10, None, 25]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df.notna())
#-----------------------------------------------

# Q3. Create a DataFrame with these records:
# Student: Ravi, Mohit, Priya
# Marks: 80, None, 90
# City: Kolkata, Delhi, None
# Use notna() to identify available values.
# Print the result.

# import pandas as pd

# data ={
#     "Student" :   ["Ravi", "Mohit", "Priya"],
#     "Marks"  :   [80, None, 90],
#     "City"    :   ["Kolkata", "Delhi", None]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df.notna())
#_____________________________________________________________________________________________________

#==============================
# Topic 5: Missing Values Count
#==============================

# Ab hum ek bahut important Data Analyst concept seekhenge: 
# har column mein kitni missing values hain, unhe count karna.

# Maan lo:

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Rahul", "Priya"],
#     "Salary": [25000, None, 30000, None],
#     "Department": ["IT", "HR", None, "IT"]
# }

# df = pd.DataFrame(data)

# print(df.isna().sum())

# Output:

# Employee      0
# Salary        2
# Department    1
# dtype: int64
# Iska matlab kya hai?
# Column	Missing Values
# Employee	0
# Salary	2
# Department 1
# df.isna() missing cells ko True/False mein dikhata hai.
# .sum() har column mein True values count karta hai, 
# kyunki Pandas mein True ka numeric value 1 hota hai aur False ka 0.

# Yaad rakhne wala code:

# df.isna().sum()

# Ye har column ki missing values count karta hai.

# Practice Questions — Missing Values Count
# ==========================================
# Pandas — Missing Values Count
# ==========================================

# Q1. Create a DataFrame with these records:
# Employee: Amit, Neha, Rahul, Priya
# Salary: 25000, None, 30000, None
# Department: IT, HR, None, IT
# Count the missing values in each column.
# Print the result.

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Rahul", "Priya"],
#     "Salary": [25000, None, 30000, None],
#     "Department": ["IT", "HR", None, "IT"]
# }

# df = pd.DataFrame(data)
# print(df.isna().sum())
#----------------------------------------------

# Q2. Create a DataFrame with these records:
# Product: Laptop, Mouse, Keyboard, Monitor
# Price: 45000, None, 1200, None
# Stock: None, 40, 25, 18
# Count the missing values in each column.
# Print the result.

# import pandas as pd

# data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
#     "Price": [45000, None, 1200, None],
#     "Stock": [None, 40, 25, 18]
# }

# df = pd.DataFrame(data)
# print(df.isna().sum())
#---------------------------------------------

# Q3. Create a DataFrame with these records:
# Student: Ravi, Mohit, Priya, Aman
# Marks: 80, None, 90, 75
# City: Kolkata, Delhi, None, None
# Count the missing values in each column.
# Print the result.

# import pandas as pd

# data = {
#     "Student" : ["Ravi", "Mohit",  "Priya", "Aman"],
#     "Marks": [80, None, 90, 75],
#     "City": ["Kolkata", "Delhi", None, None]
# }

# df = pd.DataFrame(data)
# print(df.isna().sum())
#_____________________________________________________________________________________________________

#==============================
# Topic 6: fillna()
#==============================

# fillna() kya karta hai?

# fillna() ka use DataFrame ya Series ki missing values ko kisi 
# doosri value se fill karne ke liye hota hai.

# Maan lo employee data hai:

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Rahul", "Priya"],
#     "Salary": [25000, None, 30000, None]
# }

# df = pd.DataFrame(data)

# print(df)

# Ab Salary ki missing values ko 0 se fill karte hain:

# result = df.fillna(0)

# print(result)

# Output:

# Index	Employee	Salary
# 0	Amit	25000
# 1	Neha	0
# 2	Rahul	30000
# 3	Priya	0

# Yahan dono missing Salary values 0 se replace ho gayi hain.

# 2. Sirf ek column ki missing values fill karna

# Maan lo Salary ki missing values ko 30000 se fill karna hai, 
# lekin baaki columns ko change nahi karna.

# df["Salary"] = df["Salary"].fillna(30000)

# print(df)

# Isse sirf Salary column ki missing values fill hongi.

# Important: 0 ya 30000 sirf examples hain. 
# Real analysis mein replacement value soch-samajhkar choose karni chahiye. 
# Salary ki missing value ka matlab zaroori nahi ki salary zero ho.

# 3. fillna() aur original DataFrame
# result = df.fillna(0)

# Ismein result result variable mein store hota hai aur original 
# df default behaviour mein unchanged rehta hai.

# Agar tum likho:

# df = df.fillna(0)

# Toh df variable ab filled DataFrame ko refer karega.

# Practice Questions — fillna()

# Ab ye 3 questions solve karo. Solutions abhi nahi diye gaye hain.

# ==========================================
# Pandas — Section 11: fillna()
# ==========================================

# Q1. Create a DataFrame with these records:
# Employee: Amit, Neha, Rahul
# Salary: 25000, None, 30000
# Fill missing values in the DataFrame with 0.
# Store the result in a new DataFrame.
# Print the result.

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Priya"],
#     "Salary": [25000, None, 30000]
# }

# df = pd.DataFrame(data)
# print(df.fillna(0))
#--------------------------------------------

# Q2. Create a DataFrame with these records:
# Product: Laptop, Mouse, Keyboard
# Price: 45000, None, 1200
# Stock: 10, 40, None
# Fill missing values in the DataFrame with 0.
# Store the result in a new DataFrame.
# Print the result.

# import pandas as pd

# data ={
#     "Product"  :   ["Laptop", "Mouse", "Keyboard"],
#     "Price"    :   [45000, None, 12000],
#     "Stock"    :   [10, 40, None]
# }
# df = pd.DataFrame(data)
# print(df.fillna(0))
#-------------------------------------------

# Q3. Create a DataFrame with these records:
# Employee: Amit, Neha, Rahul
# Salary: 25000, None, 30000
# Fill only the missing Salary values with 35000.
# Keep the other columns unchanged.
# Print the DataFrame.

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Priya"],
#     "Salary": [25000, None, 30000]
# }

# df = pd.DataFrame(data)

# df["Salary"] = df["Salary"].fillna(35000)
# print(df)
#_____________________________________________________________________________________________________

#==============================
# Topic 7 — dropna()
#==============================

# dropna() kya karta hai?

# dropna() ka use missing values wale rows ya columns ko remove karne ke liye hota hai.

# Maan lo hamare paas ye DataFrame hai:

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Rahul", "Priya"],
#     "Salary": [25000, None, 30000, 35000],
#     "Department": ["IT", "HR", None, "Sales"]
# }

# df = pd.DataFrame(data)

# print(df)

# DataFrame:

# Index	Employee	Salary	Department
# 0	Amit	25000	IT
# 1	Neha	NaN	HR
# 2	Rahul	30000	NaN
# 3	Priya	35000	Sales

# Ab hum dropna() use karte hain:

# result = df.dropna()

# print(result)

# Output:

# Index	Employee	Salary	Department
# 0	Amit	25000	IT
# 3	Priya	35000	Sales

# Kya hua?

# Neha ki Salary missing thi, isliye uski row remove ho gayi.
# Rahul ka Department missing tha, isliye uski row remove ho gayi.
# Amit aur Priya ki rows mein koi missing value nahi thi, isliye woh bach gayi.
# 2. Important baat

# Default mein dropna() us row ko remove karta hai jismein kam se kam ek missing value ho.

# Agar tum result ko naye DataFrame mein store karte ho:

# new_df = df.dropna()

# Toh original df default behaviour mein unchanged rehta hai.

# Dhyan do: Har missing value ko remove karna zaroori nahi hota. 
# Agar kisi row mein useful information hai, toh kabhi-kabhi fillna() 
# use karna zyada suitable ho sakta hai.

# Practice Questions — dropna()
# ==========================================
# Pandas — Section 11: dropna()
# ==========================================

# Q1. Create a DataFrame with these records:
# Employee: Amit, Neha, Rahul, Priya
# Salary: 25000, None, 30000, 35000
# Department: IT, HR, None, Sales
# Remove rows containing missing values.
# Store the result in a new DataFrame.
# Print the result.

# import pandas as pd

# data = {
#     "Employee": ["Amit", "Neha", "Rahul", "Priya"],
#     "Salary": [25000, None, 30000, 35000],
#     "Department": ["IT", "HR", None, "Sales"]
# }

# df = pd.DataFrame(data)
# result = df.dropna()
# print(result)
#----------------------------------------------

# Q2. Create a DataFrame with these records:
# Product: Laptop, Mouse, Keyboard, Monitor
# Price: 45000, None, 1200, 16000
# Stock: 10, 40, None, 18
# Remove rows containing missing values.
# Store the result in a new DataFrame.
# Print the result.

# import pandas as pd

# data ={
#     "Product"  :   ["Laptop", "Mouse", "Keyboard", "Monitor"],
#     "Price"    :   [45000, None, 1200, 16000],
#     "Stock"    :   [10, 40, None, 18]
# }
# df = pd.DataFrame(data)
# result = df.dropna()
# print(result)
#---------------------------------------------

# Q3. Create a DataFrame with these records:
# Student: Ravi, Mohit, Priya, Aman
# Marks: 80, None, 90, 75
# City: Kolkata, Delhi, None, Mumbai
# Remove rows containing missing values.
# Store the result in a new DataFrame.
# Print the result.

import pandas as pd

data = {
    "Student" : ["Ravi", "Mohit",  "Priya", "Aman"],
    "Marks": [80, None, 90, 75],
    "City": ["Kolkata", "Delhi", None, "Mumbai"]
}
df = pd.DataFrame(data)
new_df = df.dropna()
print(new_df)