
# ========================================
# CODE NUMBERING BY:-

# 1 groupby()              [30 TO 162]
# 2 Group + sum            [166 TO 271]
# 3 Group + mean           [275 TO 387]
# 4 Group + count          [391 TO 496]
# 5 Group + min/max        [500 TO 622]
# 6 Multiple Aggregations  [626 TO 778]
# 7 agg()                  [782 TO 906]
# =========================================

# Complete Topic Overview
# ------------------------

# | No. | Topic                     | Kya seekhenge?                                  |
# | --: | ------------------------- | ----------------------------------------------- |
# |   1 | `groupby()`               | Data ko groups mein divide karna                |
# |   2 | Group + `sum()`           | Har group ka total nikalna                      |
# |   3 | Group + `mean()`          | Har group ka average nikalna                    |
# |   4 | Group + `count()`         | Har group mein records count karna              |
# |   5 | Group + `min()` / `max()` | Har group ki minimum aur maximum value nikalna  |
# |   6 | Multiple Aggregations     | Ek saath multiple calculations karna            |
# |   7 | `agg()`                   | Ek group par alag-alag calculations apply karna |

#==============================
# Section 13 — GroupBy
#--------------------------
# Topic 1 — groupby()
#==============================

# 1. groupby() kya karta hai?

# Maan lo hamare paas employees ka data hai:

# import pandas as pd

# employees_df = pd.DataFrame({
#     "Employee": ["Amit", "Neha", "Rahul", "Priya", "Rohit"],
#     "Department": ["IT", "HR", "IT", "HR", "Sales"],
#     "Salary": [25000, 30000, 35000, 32000, 40000]
# })

# print(employees_df)

# Output:

# Employee	Department	Salary
# Amit	IT	25000
# Neha	HR	30000
# Rahul	IT	35000
# Priya	HR	32000
# Rohit	Sales	40000

# Ab maan lo humein dekhna hai ki kaun-kaun se employees kis department mein hain.

# Hum likhenge:

# employees_df.groupby("Department")

# Lekin dhyan do: sirf groupby() likhne se humein grouped data ka normal table output nahi milta. 
# Ye ek GroupBy object banata hai, jiske upar hum calculations kar sakte hain.

# 2. Grouping ko samjho

# Hamare data mein 3 departments hain:

# IT → Amit, Rahul
# HR → Neha, Priya
# Sales → Rohit

# groupby("Department") employees ko unke department ke according groups mein baant deta hai.

# Abhi humne sirf grouping seekhi hai. Total aur average nikalna agle topics mein seekhenge.
#---

# Ek important baat

# Tumhe har question mein dobara DataFrame banane ki zaroorat nahi hai. 
# Agar employees_df pehle se bana hua hai, 
# toh usi par naya code chala sakte ho.

# | Tumhara kaam                   | Code                                                  |
# | ------------------------------ | ----------------------------------------------------- |
# | Group banana                   | `employees_df.groupby("Department")`                  |
# | Department-wise total salary   | `employees_df.groupby("Department")["Salary"].sum()`  |
# | Department-wise average salary | `employees_df.groupby("Department")["Salary"].mean()` |
# | Har group ka poora data dekhna | `for` loop                                            |


# Practice Questions — groupby() Basic
# ==========================================
# Pandas — Section 13: GroupBy
# Topic 1: groupby()
# ==========================================

# Q1. Create a DataFrame named employees_df with these columns:
# Employee: ["Amit", "Neha", "Rahul", "Priya"]
# Department: ["IT", "HR", "IT", "HR"]
# Salary: [25000, 30000, 35000, 32000]
# Group the DataFrame by Department.

# import pandas as pd

# employees_df = pd.DataFrame({
#     "Employee": ["Amit", "Neha", "Rahul", "Priya"],
#     "Department": ["IT", "HR", "IT", "HR"],
#     "Salary": [25000, 30000, 35000, 32000]
# })
# result = employees_df.groupby("Department")
# print(result)

# for Department, group in employees_df.groupby("Department"):
#     print("Department",Department),
#     print(group),
#     print()
#------------------------------------------------------------------

# Q2. Create a DataFrame named sales_df with these columns:
# Product: ["Laptop", "Mouse", "Laptop", "Mouse", "Keyboard"]
# Region: ["East", "West", "West", "East", "East"]
# Sales: [40000, 5000, 45000, 6000, 12000]
# Group the DataFrame by Region.

# import pandas as pd

# sales_df = pd.DataFrame({
#     "Product": ["Laptop", "Mouse", "Laptop", "Mouse", "Keyboard"],
#     "Region": ["East", "West", "West", "East", "East"],
#     "Sales": [40000, 5000, 45000, 6000, 12000]
# })
# result = sales_df.groupby("Region")
# print(result)

# for region, group in sales_df.groupby("Region"):
#     print("Region", region)
#     print(group)
#     print()
#----------------------------------------------------------------

# Q3. Create a DataFrame named students_df with these columns:
# Student: ["Amit", "Neha", "Rahul", "Priya", "Rohit"]
# Class: ["A", "B", "A", "B", "A"]
# Marks: [80, 75, 90, 85, 70]
# Group the DataFrame by Class.

# import pandas as pd

# students_df = pd.DataFrame({
#     "Student": ["Amit", "Neha", "Rahul", "Priya", "Rohit"],
#     "Class": ["A", "B", "A", "B", "A"],
#     "Marks": [80, 75, 90, 85, 70]
# })

# result = students_df.groupby("Class")
# print(result)

# for Class, group in students_df.groupby("Class"):
#     print("Class", Class)
#     print(group)
#     print()
#_____________________________________________________________________________________________________

#==============================
# Topic 2 — GroupBy + sum()
#==============================

# Pichhle topic mein humne seekha tha ki groupby() data ko groups mein divide karta hai. 
# Ab hum seekhenge ki har group ka total kaise nikalte hain.

# 1. Example samjho

# Maan lo hamare paas sales ka data hai:

# import pandas as pd

# sales_df = pd.DataFrame({
#     "Product": ["Laptop", "Mouse", "Laptop", "Mouse", "Keyboard"],
#     "Region": ["East", "West", "West", "East", "East"],
#     "Sales": [40000, 5000, 45000, 6000, 12000]
# })

# print(sales_df)

# Ab humein har region ki total sales nikalni hain.

# 2. Sirf ek line mein total
# sales_df.groupby("Region")["Sales"].sum()

# Output:

# Region
# East    18000
# West    50000
# Name: Sales, dtype: int64
# 3. Is code ko samjho
# sales_df.groupby("Region")["Sales"].sum()
# Code	Kaam
# groupby("Region")	Sales ko region ke according group karta hai
# ["Sales"]	Sales column select karta hai
# .sum()	Har group ki sales ko add karta hai

# Calculation:

# East = 6,000 + 12,000 = 18,000
# West = 5,000 + 45,000 = 50,000

# Dhyan do: Product column ko select nahi kiya, kyunki humein Sales ka total chahiye.

# 4. Data Analyst ke liye iska use

# Maan lo company ke manager ko pata karna hai ki East aur West regions mein kitni sales hui. 
# Har record ko manually add karne ki zaroorat nahi—groupby() + sum() se total mil jayega.

# Practice Questions — GroupBy + sum()
# ==========================================
# Pandas — Section 13: GroupBy + sum()
# ==========================================

# Q1. Create a DataFrame named employees_df with these columns:
# Employee: ["Amit", "Neha", "Rahul", "Priya"]
# Department: ["IT", "HR", "IT", "HR"]
# Salary: [25000, 30000, 35000, 32000]
# Calculate the total Salary for each Department.

# import pandas as pd

# employees_df = pd.DataFrame({
#     "Employee": ["Amit", "Neha", "Rahul", "Priya"],
#     "Department": ["IT", "HR", "IT", "HR"],
#     "Salary": [25000, 30000, 35000, 32000]
# })

# result = employees_df.groupby("Department")["Salary"].sum()
# print(result)
#--------------------------------------------------------------

# Q2. Create a DataFrame named sales_df with these columns:
# Product: ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse"]
# Region: ["East", "West", "East", "West", "East"]
# Sales: [40000, 5000, 12000, 45000, 6000]
# Calculate the total Sales for each Region.

# import pandas as pd

# sales_df = pd.DataFrame({
#     "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse"],
#     "Region": ["East", "West", "East", "West", "East"],
#     "Sales": [40000, 5000, 12000, 45000, 6000]   
# })

# result = sales_df.groupby("Region")["Sales"].sum()
# print(result)
#---------------------------------------------------------------

# Q3. Create a DataFrame named orders_df with these columns:
# Category: ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"]
# City: ["Kolkata", "Delhi", "Delhi", "Kolkata", "Kolkata"]
# Amount: [15000, 5000, 20000, 7000, 10000]
# Calculate the total Amount for each City.

# import pandas as pd

# order_df = pd.DataFrame({
#     "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
#     "City": ["Kolkata", "Delhi", "Delhi", "Kolkata", "Kolkata"],
#     "Amount": [15000, 5000, 20000, 7000, 10000]   
# })
# result = order_df.groupby("City")["Amount"].sum()
# print(result)
#_____________________________________________________________________________________________________

#==============================
# Topic 3 — mean()
#==============================

# mean() ka matlab hota hai average (औसत) nikalna.

# 1. Pehle average samjho

# Maan lo IT department mein 3 employees ki salaries hain:

# ₹25,000
# ₹35,000
# ₹40,000

# Average salary:

# (25,000 + 35,000 + 40,000) ÷ 3 = ₹33,333.33

# Pandas mein hum ye calculation automatically karwa sakte hain.

# 2. Example dekho
# import pandas as pd

# employees_df = pd.DataFrame({
#     "Employee": ["Amit", "Neha", "Rahul", "Priya"],
#     "Department": ["IT", "HR", "IT", "HR"],
#     "Salary": [25000, 30000, 35000, 32000]
# })

# result = employees_df.groupby("Department")["Salary"].mean()

# print(result)

# Output:

# Department
# HR    31000.0
# IT    30000.0
# Name: Salary, dtype: float64
# 3. Code ko step-by-step samjho
# employees_df.groupby("Department")["Salary"].mean()
# groupby("Department") — employees ko department ke hisaab se group karta hai.
# ["Salary"] — Salary column select karta hai.
# .mean() — har department ki average salary nikalta hai.

# Calculation:

# HR: (30,000 + 32,000) ÷ 2 = ₹31,000
# IT: (25,000 + 35,000) ÷ 2 = ₹30,000

# Yaad rakho:

# .sum() → Total
# .mean() → Average

# Dono mein groupby() ka kaam same hai; sirf calculation badalti hai.

# Practice Questions — GroupBy + mean()
# ==========================================
# Pandas — Section 13: GroupBy + mean()
# ==========================================

# Q1. Create a DataFrame named employees_df with these columns:
# Employee: ["Amit", "Neha", "Rahul", "Priya"]
# Department: ["IT", "HR", "IT", "HR"]
# Salary: [25000, 30000, 35000, 32000]
# Calculate the average Salary for each Department.

# import pandas as pd

# employees_df = pd.DataFrame({
#     "Employee": ["Amit", "Neha", "Rahul", "Priya"],
#     "Department": ["IT", "HR", "IT", "HR"],
#     "Salary": [25000, 30000, 35000, 32000]
# })

# result = employees_df.groupby("Department")["Salary"].mean()
# print(result)
#------------------------------------------------------------------

# Q2. Create a DataFrame named sales_df with these columns:
# Product: ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse"]
# Region: ["East", "West", "East", "West", "East"]
# Sales: [40000, 5000, 12000, 45000, 6000]
# Calculate the average Sales for each Region.

# import pandas as pd

# sales_df = pd.DataFrame({
#     "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse"],
#     "Region": ["East", "West", "East", "West", "East"],
#     "Sales": [40000, 5000, 12000, 45000, 6000]
# })

# result = sales_df.groupby("Region")["Sales"].mean()
# print(result)
#-----------------------------------------------------------

# Q3. Create a DataFrame named orders_df with these columns:
# Category: ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"]
# City: ["Kolkata", "Delhi", "Delhi", "Kolkata", "Kolkata"]
# Amount: [15000, 5000, 20000, 7000, 10000]
# Calculate the average Amount for each City.

# import pandas as pd

# orders_df =pd.DataFrame({
#     "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
#     "City": ["Kolkata", "Delhi", "Delhi", "Kolkata", "Kolkata"],
#     "Amount": [15000, 5000, 20000, 7000, 10000]
# })

# result = orders_df.groupby("City")["Amount"].mean()
# print(result)
#____________________________________________________________________________________________________

#==============================
# Topic 4— GroupBy + count()
#==============================

# 1. count() kya karta hai?

# Pandas mein count() har group ke andar non-missing values ki ginti karta hai.

# Data Analyst ke kaam mein iska use hota hai, jaise:

# Har department mein kitni employees ki salary available hai.
# Har city mein kitne sales records hain.
# Har product ke kitne records hain.
# Example
# import pandas as pd

# employees_df = pd.DataFrame({
#     "Employee": ["Amit", "Neha", "Rahul", "Priya"],
#     "Department": ["IT", "HR", "IT", "HR"],
#     "Salary": [25000, 30000, 35000, 32000]
# })

# result = employees_df.groupby("Department")["Employee"].count()

# print(result)

# Output:

# Department
# HR    2
# IT    2
# Name: Employee, dtype: int64
# Step-by-step samjho
# employees_df.groupby("Department")["Employee"].count()
# groupby("Department") → employees ko department ke hisaab se group karta hai.
# ["Employee"] → Employee column select karta hai.
# .count() → har department mein available employee names count karta hai.

# HR mein 2 employees hain aur IT mein bhi 2 employees hain.

# count() aur sum() mein difference
# Method	Kaam
# sum()	Values ka total nikalta hai
# mean()	Values ka average nikalta hai
# count()	Non-missing values count karta hai

# Important: count() missing values ko count nahi karta. 
# Aur groupby() ke baad jis column par count() lagate ho, 
# usi column ki non-missing values count hoti hain.

# Practice Questions — GroupBy + count()
# ==========================================
# Pandas — Section 13: GroupBy + count()
# ==========================================

# Q1. Create a DataFrame named employees_df with these columns:
# Employee: ["Amit", "Neha", "Rahul", "Priya", "Mohit"]
# Department: ["IT", "HR", "IT", "HR", "IT"]
# Salary: [25000, 30000, 35000, 32000, 28000]
# Count the employees in each Department.

# import pandas as pd

# employees_df = pd.DataFrame({
#     "Employee": ["Amit", "Neha", "Rahul", "Priya", "Mohit"],
#     "Department": ["IT", "HR", "IT", "HR", "IT"],
#     "Salary": [25000, 30000, 35000, 32000, 28000]
# })

# result = employees_df.groupby("Department")["Salary"].count()
# print(result)
#-----------------------------------------------------------

# Q2. Create a DataFrame named sales_df with these columns:
# Product: ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse"]
# Region: ["East", "West", "East", "West", "East"]
# Sales: [40000, 5000, 12000, 45000, 6000]
# Count the Sales records in each Region.

# import pandas as pd

# sales_df = pd.DataFrame({
#     "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse"],
#     "Region": ["East", "West", "East", "West", "East"],
#     "Sales": [40000, 5000, 12000, 45000, 6000]
# })

# result = sales_df.groupby("Region")["Sales"].count()
# print(result)
#--------------------------------------------------------

# Q3. Create a DataFrame named orders_df with these columns:
# Category: ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"]
# City: ["Kolkata", "Delhi", "Delhi", "Kolkata", "Kolkata"]
# Amount: [15000, 5000, 20000, 7000, 10000]
# Count the orders in each City.

# import pandas as pd

# orders_df =pd.DataFrame({
#     "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
#     "City": ["Kolkata", "Delhi", "Delhi", "Kolkata", "Kolkata"],
#     "Amount": [15000, 5000, 20000, 7000, 10000]
# })

# result = orders_df.groupby("City")["Amount"].count()
# print(result)
#_____________________________________________________________________________________________________

#==================================
# Topic 5: GroupBy + min() / max()
#==================================

# 1. Ye methods kya karte hain?
# min() → har group ki sabse chhoti value nikalta hai.
# max() → har group ki sabse badi value nikalta hai.

# Data Analyst ke kaam mein inka use minimum delivery time, 
# maximum product price, highest marks aur lowest transaction amount nikalne mein hota hai.

# 2. Example: Students ke marks

# Maan lo ek coaching centre mein alag-alag batches ke students ke marks hain.

# import pandas as pd

# marks_data = pd.DataFrame({
#     "Student": ["Aman", "Riya", "Karan", "Pooja", "Simran"],
#     "Batch": ["Morning", "Evening", "Morning", "Evening", "Morning"],
#     "Marks": [78, 92, 65, 85, 88]
# })

# lowest_marks = marks_data.groupby("Batch")["Marks"].min()
# highest_marks = marks_data.groupby("Batch")["Marks"].max()

# print("Minimum marks:")
# print(lowest_marks)

# print("\nMaximum marks:")
# print(highest_marks)
# Output
# Minimum marks:
# Batch
# Evening    85
# Morning    65
# Name: Marks, dtype: int64

# Maximum marks:
# Batch
# Evening    92
# Morning    88
# Name: Marks, dtype: int64
# Step-by-step samjho

# Pehle Morning aur Evening batches ke groups banenge.

# Morning batch: 78, 65, 88

# min() → 65
# max() → 88

# Evening batch: 92, 85

# min() → 85
# max() → 92

# Dhyan do: groupby("Batch") groups banata hai. 
# Uske baad min() ya max() har group ki selected column par calculation karta hai.

# Practice Questions — GroupBy + min() / max()

# Is baar teen alag scenarios hain: hospital, online store aur transport service.

# ==========================================
# Pandas — GroupBy + min() / max()
# ==========================================

# Q1. Create a DataFrame named hospital_data with these columns:
# Patient: ["Aarav", "Meera", "Kabir", "Sana", "Ishaan"]
# Ward: ["A", "B", "A", "B", "A"]
# WaitingTime: [25, 40, 15, 30, 50]
# Find the minimum WaitingTime in each Ward.

# import pandas as pd

# hospital_data = pd.DataFrame({
#     "Patient": ["Aarav", "Meera", "Kabir", "Sana", "Ishaan"],
#     "Ward": ["A", "B", "A", "B", "A"],
#     "WaitingTime": [25, 40, 15, 30, 50]
# })
# result = hospital_data.groupby("Ward")["WaitingTime"].min()
# print(result)
#------------------------------------------------------------------

# Q2. Create a DataFrame named shop_inventory with these columns:
# Item: ["Bag", "Shoes", "Watch", "Bag", "Watch"]
# Store: ["Central", "North", "Central", "North", "Central"]
# Price: [1200, 2500, 3000, 1500, 2200]
# Find the maximum Price in each Store.

# import pandas as pd

# shop_inventory =pd.DataFrame({
#     "Item": ["Bag", "Shoes", "Watch", "Bag", "Watch"],
#     "Store": ["Central", "North", "Central", "North", "Central"],
#     "Price": [1200, 2500, 3000, 1500, 2200]
# })
# result = shop_inventory.groupby("Store")["Price"].max()
# print(result)
#----------------------------------------------------------------

# Q3. Create a DataFrame named delivery_log with these columns:
# OrderID: [501, 502, 503, 504, 505, 506]
# Vehicle: ["Van", "Bike", "Van", "Bike", "Van", "Bike"]
# DeliveryHours: [4, 2, 6, 3, 5, 1]
# Find both the minimum and maximum DeliveryHours for each Vehicle

# import pandas as  cd

# delivery_log = cd.DataFrame({
#     "OrderID": [501, 502, 503, 504, 505, 506],
#     "Vehicle": ["Van", "Bike", "Van", "Bike", "Van", "Bike"],
#     "DeliveryHours": [4, 2, 6, 3, 5, 1]   
# })

# min_time = delivery_log.groupby("Vehicle")["DeliveryHours"].min()
# max_time = delivery_log.groupby("Vehicle")["DeliveryHours"].max()

# print("minimum delivery hours:")
# print(min_time)

# print("\nmaximum delivery hours:")
# print(max_time)
#_____________________________________________________________________________________________________

#================================
# Topic 6: Multiple Aggregations
#================================

# 1. Multiple Aggregations kya hota hai?

# Ab tak hum ek baar mein ek calculation kar rahe the:

# data.groupby("Category")["Revenue"].sum()

# Isse har category ka total Revenue milta hai.

# Lekin Data Analyst ko aksar ek hi dataset se kai calculations chahiye hoti hain, jaise:

# Total Revenue
# Average Revenue
# Minimum Revenue
# Maximum Revenue

# Multiple Aggregations se hum ek hi group par ye calculations ek saath kar sakte hain.

# 2. Example: Online courses

# Maan lo ek learning platform par alag-alag course categories ki fees record ki gayi hain.

# import pandas as pd

# course_data = pd.DataFrame({
#     "Course": ["Python", "SQL", "Excel", "Pandas", "Power BI", "Advanced SQL"],
#     "Category": ["Programming", "Database", "Office", "Programming", "Office", "Database"],
#     "Fee": [5000, 3000, 2000, 6000, 4000, 5000]
# })

# result = course_data.groupby("Category")["Fee"].agg(
#     ["sum", "mean", "min", "max"]
# )

# print(result)
# Output
                #  sum    mean   min   max
# Category
# Database        8000  4000.0  3000  5000
# Office          6000  3000.0  2000  4000
# Programming    11000  5500.0  5000  6000
# 3. Code ko step-by-step samjho

# Is line ko dhyan se dekho:

# result = course_data.groupby("Category")["Fee"].agg(
#     ["sum", "mean", "min", "max"]
# )

# Step 1 — groupby("Category")

# Courses ko category ke hisaab se group karega.

# Step 2 — ["Fee"]

# Sirf Fee column par calculation hogi.

# Step 3 — .agg()

# agg() ka use ek ya ek se zyada aggregation functions apply karne ke liye hota hai.

# ["sum", "mean", "min", "max"]

# Inka matlab:

# Function	Result
# sum	Total fees
# mean	Average fees
# min	Sabse kam fee
# max	Sabse zyada fee
# Ek important baat

# Pehle hum likhte the:

# course_data.groupby("Category")["Fee"].sum()

# Ab multiple calculations ke liye:

# course_data.groupby("Category")["Fee"].agg(["sum", "mean", "min", "max"])

# Yahan .agg() ke andar function names strings ke roop mein diye hain, isliye sum aur mean ke baad parentheses nahi lagate.

# Practice Questions — Multiple Aggregations

# Is baar datasets mein movie ratings, electricity consumption aur travel expenses hain.

# ==========================================
# Pandas — Section 13: Multiple Aggregations
# ==========================================

# Q1. Create a DataFrame named movie_stats with these columns:
# Movie: ["Film A", "Film B", "Film C", "Film D", "Film E", "Film F"]
# Genre: ["Action", "Comedy", "Action", "Comedy", "Drama", "Drama"]
# Rating: [8.5, 7.2, 9.0, 6.8, 8.1, 7.5]
# For each Genre, calculate the mean, minimum, and maximum Rating.

# import pandas as pd

# movie_stats = pd.DataFrame({
#     "Movie": ["Film A", "Film B", "Film C", "Film D", "Film E", "Film F"],
#     "Genre": ["Action", "Comedy", "Action", "Comedy", "Drama", "Drama"],
#     "Rating": [8.5, 7.2, 9.0, 6.8, 8.1, 7.5]  
# })

# result = movie_stats.groupby("Genre")["Rating"].agg(
#     ["mean", "min",  "max" ]
# )

# print(result)
#---------------------------------------------------------------------

# Q2. Create a DataFrame named power_usage with these columns:
# Building: ["Tower A", "Tower B", "Tower C", "Tower D", "Tower E", "Tower F"]
# Zone: ["North", "South", "North", "South", "North", "South"]
# Units: [450, 320, 500, 280, 400, 350]
# For each Zone, calculate the total, average, and maximum Units.

# import pandas as pd

# power_usage = pd.DataFrame({
#     "Building": ["Tower A", "Tower B", "Tower C", "Tower D", "Tower E", "Tower F"],
#     "Zone": ["North", "South", "North", "South", "North", "South"],
#     "Units": [450, 320, 500, 280, 400, 350]
# })

# result = power_usage.groupby("Zone")["Units"].agg(
#     ["sum", "mean", "max"]
# )

# print(result)
#-----------------------------------------------------------------

# Q3. Create a DataFrame named travel_costs with these columns:
# TripID: [201, 202, 203, 204, 205, 206]
# Transport: ["Train", "Bus", "Train", "Bus", "Flight", "Flight"]
# Cost: [800, 300, 1200, 250, 4500, 5000]
# For each Transport, calculate the sum, mean, minimum, and maximum cost.

# import pandas as pd

# travel_costs = pd.DataFrame({
#     "TripID": [201, 202, 203, 204, 205, 206],
#     "Transport": ["Train", "Bus", "Train", "Bus", "Flight", "Flight"],
#     "Cost": [800, 300, 1200, 250, 4500, 5000]
# })

# result = travel_costs.groupby("Transport")["Cost"].agg(
#     ["sum", "mean", "min", "max"]
# )

# print(result)
#_____________________________________________________________________________________________________

#==============================
# Topic 7 — agg()
#==============================

# Pichhle topic mein humne ek hi column par multiple calculations ki thi. 
# Ab dekhenge ki alag-alag columns par alag calculations ek saath kaise karte hain.

# 1. Example samjho
# import pandas as pd

# store_data = pd.DataFrame({
#     "Store": ["A", "B", "A", "B", "A", "B"],
#     "Product": ["Rice", "Oil", "Wheat", "Rice", "Oil", "Wheat"],
#     "Price": [500, 150, 400, 550, 180, 450],
#     "Quantity": [10, 5, 8, 12, 6, 9]
# })

# Maan lo humein har Store ke liye:

# Total Price nikalna hai.
# Average Quantity nikalni hai.
# Products ki count nikalni hai.

# Iske liye:

# result = store_data.groupby("Store").agg({
#     "Price": "sum",
#     "Quantity": "mean",
#     "Product": "count"
# })

# print(result)

# Output:

#        Price  Quantity  Product
# Store
# A       1080       8.0        3
# B       1150      10.0        3
# 2. Code ko samjho
# groupby("Store") → Data ko Store A aur Store B mein divide karta hai.
# "Price": "sum" → Har Store ka total Price.
# "Quantity": "mean" → Har Store ki average Quantity.
# "Product": "count" → Har Store mein Product ke non-missing records ki count.

# Dhyan do: Dictionary mein column ka naam key hota hai aur calculation value hoti hai.

# Practice Questions
# ==========================================
# Pandas — Section 13: agg()
# ==========================================

# Q1. Create a DataFrame named hospital_stats with these columns:
# Hospital: ["H1", "H2", "H1", "H2", "H1", "H2"]
# Doctor: ["A", "B", "C", "D", "E", "F"]
# Patients: [40, 55, 35, 60, 50, 45]
# Fees: [500, 600, 450, 700, 550, 650]
# For each Hospital, calculate the total Patients and average Fees
# using agg().

# import pandas as pd

# hospital_stats = pd.DataFrame({
#     "Hospital": ["H1", "H2", "H1", "H2", "H1", "H2"],
#     "Doctor": ["A", "B", "C", "D", "E", "F"],
#     "Patients": [40, 55, 35, 60, 50, 45],
#     "Fees": [500, 600, 450, 700, 550, 650]
# })

# result = hospital_stats.groupby("Hospital").agg({
#     "Patients" : "sum",
#     "Fees" : "mean"
# })

# print(result)
#-----------------------------------------------------------------

# Q2. Create a DataFrame named cafe_orders with these columns:
# Cafe: ["Central", "West", "Central", "West", "Central", "West"]
# Item: ["Tea", "Coffee", "Sandwich", "Tea", "Coffee", "Sandwich"]
# Orders: [30, 25, 20, 35, 40, 15]
# Revenue: [300, 500, 400, 350, 800, 300]
# For each Cafe, calculate the maximum Orders and total Revenue
# using agg().

# import pandas as pd

# cafe_orders = pd.DataFrame({
#     "Cafe": ["Central", "West", "Central", "West", "Central", "West"],
#     "Item": ["Tea", "Coffee", "Sandwich", "Tea", "Coffee", "Sandwich"],
#     "Orders": [30, 25, 20, 35, 40, 15],
#     "Revenue": [300, 500, 400, 350, 800, 300]
# })

# result = cafe_orders.groupby("Cafe").agg({
#     "Orders" : "max",
#     "Revenue": "sum"
# })

# print(result)
#-------------------------------------------------------------

# Q3. Create a DataFrame named delivery_stats with these columns:
# Area: ["North", "South", "North", "South", "North", "South"]
# Courier: ["A", "B", "C", "D", "E", "F"]
# DeliveryTime: [25, 40, 30, 35, 20, 45]
# Distance: [5, 8, 6, 7, 4, 9]
# For each Area, calculate the minimum DeliveryTime,
# average Distance, and count of Couriers using agg().

import pandas as pd

delivery_stats =pd.DataFrame({
    "Area": ["North", "South", "North", "South", "North", "South"],
    "Courier": ["A", "B", "C", "D", "E", "F"],
    "DeliveryTime": [25, 40, 30, 35, 20, 45],
    "Distance": [5, 8, 6, 7, 4, 9],
})

result = delivery_stats.groupby("Area").agg({
   "DeliveryTime" : "min",
    "Distance" : "mean",
    "Courier" : "count"
})
print(result)