# ========================================
# CODE NUMBERING BY:-

# 1 apply()                [24 TO 148]
# 2 Lambda with apply()    [153 TO 251]
# 3 Apply on Columns       [255 TO 366]
# 4 Apply with Conditions  [370 TO 484]
# =========================================

#========================================
# Complete Topic Overview
#========================================

# | No. | Topic                 | Kya seekhenge?                                 |
# | --: | --------------------- | ---------------------------------------------- |
# |   1 | `apply()`             | Custom function ko Pandas data par apply karna |
# |   2 | Lambda with `apply()` | Lambda function ke saath `apply()` use karna   |
# |   3 | Apply on Columns      | DataFrame ke columns par function apply karna  |
# |   4 | Apply with Conditions | Conditions ke basis par values modify karna    |

#================================
# Section 18. Apply & Functions
#--------------------------------
#Topic 1 — apply()
#================================

# 1. apply() kya karta hai?

# Pandas mein apply() ka use kisi function ko Series ya DataFrame ke data par apply karne ke liye hota hai.

# Maan lo hamare paas employees ki salary hai aur humein har employee ki salary mein ₹5,000 add karne hain.

# Example
# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Vikash", "Mohit", "Ravi"],
#     "Salary": [25000, 35000, 45000]
# })

# def increase_salary(salary):
#     return salary + 5000

# df["Salary"] = df["Salary"].apply(increase_salary)

# print(df)

# Output:

#      Name  Salary
# 0  Vikash   30000
# 1   Mohit   40000
# 2    Ravi   50000
# 2. Code ko samjho

# Step 1 — Function banana

# def increase_salary(salary):
#     return salary + 5000

# Ye function jo salary receive karega, usmein 5000 add karke return karega.

# Step 2 — apply() use karna

# df["Salary"].apply(increase_salary)

# Ye function ko Salary column ki har value par apply karega.

# Step 3 — Updated column

# df["Salary"] = df["Salary"].apply(increase_salary)

# Isse updated salaries wapas Salary column mein store ho jayengi.

# Important

# Normal Python function mein hum ek value pass karte hain:

# increase_salary(25000)

# Pandas apply() mein hum poora column pass karte hain:

# df["Salary"].apply(increase_salary)

# Pandas automatically har value ko function mein bhejta hai.

# Practice Questions — apply()
# Pandas — apply() Practice
# ==========================================
# Pandas Section 18 — Apply & Functions
# Topic 1: apply()
# ==========================================

# Q1.
# Create a DataFrame with a Price column containing
# 100, 200, and 300.
# Create a function that adds 50 to each price.
# Apply the function to the Price column.

# import pandas as pd

# df = pd.DataFrame({
#     "Price" : [100, 200, 300]
# })

# def add(price):
#     return price + 50

# result = df["Price"] = df["Price"].apply(add)
# print(result)
#------------------------------------------------

# Q2.
# Create a DataFrame with a Marks column containing
# 65, 75, and 85.
# Create a function that adds 5 bonus marks to each value.
# Apply the function to the Marks column.

# import pandas as pd

# df = pd.DataFrame({
#     "Marks" : [65,75,85]
# })

# def add(bonus):
#     return bonus + 5

# df["Marks"] = df["Marks"].apply(add)
# print(df)
#----------------------------------------

# Q3.
# Create a DataFrame with a Quantity column containing
# 2, 4, and 6.
# Create a function that multiplies each quantity by 10.
# Apply the function to the Quantity column.

# import pandas as pd

# df = pd.DataFrame({
#     "Quantity" : [2,4,6]
# })

# def multiply(quantity):
#     return quantity * 10

# df["Quantity"] = df["Quantity"].apply(multiply)
# print(df)

#_____________________________________________________________________________________________________

#==============================
# Topic 2 — Lambda with apply()
#==============================

# Pichhle topic mein humne apply() ke saath normal function (def) use kiya tha. 
# Ab wahi kaam lambda se karenge.
 
# 1. Lambda with apply() kya hai?

# Lambda ek short, anonymous function hota hai. Ismein alag se def likhne ki zarurat nahi hoti.

# Previous method — Normal function
# def add_bonus(salary):
#     return salary + 5000

# df["Salary"] = df["Salary"].apply(add_bonus)
# New method — Lambda function
# df["Salary"] = df["Salary"].apply(lambda salary: salary + 5000)

# Dono ka result same hoga.

# 2. Example

# Maan lo employees ki salary mein 10% increase karna hai.

# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Vikash", "Mohit", "Ravi"],
#     "Salary": [25000, 35000, 45000]
# })

# df["Salary"] = df["Salary"].apply(lambda salary: salary * 1.10)

# print(df)

# Output:

#      Name  Salary
# 0  Vikash   27500
# 1   Mohit   38500
# 2    Ravi   49500
# 3. Lambda code ko samjho
# lambda salary: salary * 1.10
# lambda → Lambda function start karta hai.
# salary → Input parameter hai.
# : → Function expression ko separate karta hai.
# salary * 1.10 → Calculation karke result return karta hai.

# Important: Lambda mein return likhne ki zarurat nahi hoti. 
# Expression ka result automatically return hota hai.

# 4. Practice Questions — Lambda with apply()
# Pandas — Lambda with apply() Practice
# ==========================================
# Pandas Section 18 — Apply & Functions
# Topic 2: Lambda with apply()
# ==========================================

# Q1.
# Create a DataFrame with a Price column containing
# 100, 200, and 300.
# Increase each price by 20% using lambda with apply().

# import pandas as pd

# df = pd.DataFrame({
#     "Price" : [100, 200, 300]
# })
# df["Price"] = df["Price"].apply(lambda price : price * 1.20)
# print(df)
#---------------------------------------------------

# Q2.
# Create a DataFrame with a Marks column containing
# 60, 70, and 80.
# Add 10 bonus marks to each value using lambda with apply().

# import pandas as pd

# df = pd.DataFrame({
#     "Marks" : [60,70,80]
# })

# df["Marks"] = df["Marks"].apply(lambda marks : marks + 10)
# print(df)
#-----------------------------------------------
# Q3.
# Create a DataFrame with a Quantity column containing
# 5, 10, and 15.
# Multiply each quantity by 3 using lambda with apply().

# import pandas as pd

# df = pd.DataFrame({
#     "Quantity" : [5, 10, 15]
# })

# df["Quantity"] = df["Quantity"].apply(lambda quantity : quantity * 3)
# print(df)
#_____________________________________________________________________________________________________

#==============================
# Topic 3 — Apply on Columns.
#==============================

# 1. Apply on Columns kya hai?

# Jab hum kisi DataFrame ke column par function apply karte hain, toh apply() ka use hota hai.

# Maan lo hamare paas employees ka DataFrame hai:

# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Vikash", "Mohit", "Ravi"],
#     "Salary": [25000, 35000, 45000],
#     "Bonus": [2000, 3000, 4000]
# })

# Ab humein har employee ki salary aur bonus ko add karke Total Salary nikalni hai.

# Example 1 — Column par function apply karna
# def calculate_total(salary):
#     return salary + 5000

# df["Salary"] = df["Salary"].apply(calculate_total)

# print(df)

# Is example mein function sirf Salary column par apply hua.

# Example 2 — Multiple Columns se calculation

# Agar humein Salary aur Bonus ko add karke naya column banana hai:

# df["Total Salary"] = df["Salary"] + df["Bonus"]

# print(df)

# Output:

#      Name  Salary  Bonus  Total Salary
# 0  Vikash   25000   2000         27000
# 1   Mohit   35000   3000         38000
# 2    Ravi   45000   4000         49000

# Important distinction:

# df["Salary"].apply(function) → Salary column ki har value par function apply karta hai.
# df["Salary"] + df["Bonus"] → Dono columns ki corresponding values add karta hai.

# Data Analyst ke kaam mein multiple columns se calculations karna bahut common hai.

# Practice Questions — Apply on Columns
# Pandas — Apply on Columns Practice
# ==========================================
# Pandas Section 18 — Apply & Functions
# Topic 3: Apply on Columns
# ==========================================

# Q1.
# Create a DataFrame with Salary and Bonus columns.
# Salary: 25000, 35000, 45000
# Bonus: 2000, 3000, 4000
# Create a Total Salary column by adding Salary and Bonus.

# import pandas as pd

# df = pd.DataFrame({
#     "Salary": [25000, 35000, 45000],
#     "Bonus": [2000, 3000, 4000]
# })

# df["Total_salary"] = df["Salary"] + df["Bonus"]
# print(df)
#---------------------------------------------------

# Q2.
# Create a DataFrame with Price and Quantity columns.
# Price: 100, 200, 300
# Quantity: 2, 3, 4
# Create a Total Amount column by multiplying Price and Quantity.

# import pandas as pd

# df = pd.DataFrame({
#     "Price": [100, 200, 300],
#     "Quantity": [2, 3, 4]
# })

# df["Total_Amount"] = df["Price"] * df["Quantity"]
# print(df)
#--------------------------------------------------------

# Q3.
# Create a DataFrame with Basic Salary and Allowance columns.
# Basic Salary: 20000, 30000, 40000
# Allowance: 3000, 4000, 5000
# Create a Total Salary column using a custom function
# with apply() on the DataFrame.

# import pandas as pd

# df = pd.DataFrame({
#     "Basic Salary": [20000, 30000, 40000],
#     "Allowance": [3000, 4000, 5000]
# })

# def calculate_total(row):
#     return row["Basic Salary"] + row["Allowance"]

# df["Total Salary"] = df.apply(calculate_total, axis=1)

# print(df)
#_____________________________________________________________________________________________________

#================================
# Topic 4 — Apply with Conditions
#================================

# Is topic mein hum seekhenge ki condition ke basis par DataFrame 
# ki values kaise modify karte hain, using apply().

# 1. Basic Example

# Maan lo employees ki salary ke basis par bonus dena hai:

# import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Vikash", "Mohit", "Ravi"],
#     "Salary": [25000, 40000, 60000]
# })

# def calculate_bonus(salary):
#     if salary >= 50000:
#         return salary * 0.20
#     else:
#         return salary * 0.10

# df["Bonus"] = df["Salary"].apply(calculate_bonus)

# print(df)

# Output:

#      Name  Salary    Bonus
# 0  Vikash   25000   2500.0
# 1   Mohit   40000   4000.0
# 2    Ravi   60000  12000.0
# 2. Samjho kaise kaam karta hai

# df["Salary"].apply(calculate_bonus):

# Salary column ki har value function ko bhejta hai.
# Function if-else condition check karta hai.
# Condition ke according bonus calculate karta hai.
# Result Bonus column mein store hota hai.
# Practice Questions
# ==========================================
# Pandas Section 18 — Apply & Functions
# Topic 4: Apply with Conditions
# ==========================================

# Q1.
# Create a DataFrame with a Marks column.
# Marks: 85, 45, 70, 30
# Create a Result column using apply().
# If Marks >= 40, return "Pass".
# Otherwise, return "Fail".

# import pandas as pd

# df = pd.DataFrame({
#     "Marks": [85, 45, 70, 30]
# })
# def calclate_marks(marks):
#     if marks >= 40:
#         return "Pass"
#     else:
#         return "fail"

# df["result"] = df["Marks"].apply(calclate_marks)

# print(df)
#----------------------------------------

# Q2.
# Create a DataFrame with Salary column.
# Salary: 25000, 40000, 60000, 80000
# Create a Bonus column using apply().
# If Salary >= 50000, calculate 20% bonus.
# Otherwise, calculate 10% bonus.

# import pandas as pd

# df = pd.DataFrame({
#     "Salary": [25000, 40000, 60000, 80000]
# })

# def calculate_bonus(salary):
#     if salary >= 50000:
#         return salary * 0.20
#     else:
#         return salary * 0.10

# df["Bonus"] = df["Salary"].apply(calculate_bonus)

# print(df)
#----------------------------------------------------

# Q3.
# Create a DataFrame with Price column.
# Price: 500, 1200, 2500, 4000
# Create a Discount column using apply().
# If Price >= 2000, calculate 15% discount.
# Otherwise, calculate 5% discount.

import pandas as pd

df = pd.DataFrame({
    "Price": [500, 1200, 2500, 4000]
})

def discount(price):
    if price >= 2000:
        return price * 0.15
    else :
        return price * 0.05

df["Discount"] = df["Price"].apply(discount)
print(df)
