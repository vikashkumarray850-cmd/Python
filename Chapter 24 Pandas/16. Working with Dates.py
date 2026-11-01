# ========================================
# CODE NUMBERING BY:-

# 1 pd.to_datetime()  [30 TO 156]
# 2 Extract Year      [159 TO 275]
# 3 Extract Month     [279 TO 402]
# 4 Extract Day       [406 TO 521]
# 5 Date Filtering    [525 TO 662
# 6 Date Difference   [666 TO 809]
# 7 dt accessor       [814 TO 938]
# =========================================

#========================================
# Complete Topic Overview
#========================================

# | No. | Topic              | Kya seekhenge?                                    |
# | --: | ------------------ | ------------------------------------------------- |
# |   1 | `pd.to_datetime()` | Text ko proper date format mein convert karna     |
# |   2 | Extract Year       | Date se year nikalna                              |
# |   3 | Extract Month      | Date se month nikalna                             |
# |   4 | Extract Day        | Date se day nikalna                               |
# |   5 | Date Filtering     | Specific dates ya date range ka data filter karna |
# |   6 | Date Difference    | Do dates ke beech ka difference nikalna           |
# |   7 | `.dt` accessor     | Pandas mein dates par operations karna            |

#==================================
# Section 16 — Working with Dates
#---------------------------------
# Topic 1: pd.to_datetime()
#==================================

# 1. Ye kya karta hai?

# Maan lo tumhare paas sales ki dates hain:

# import pandas as pd

# sales_data = pd.DataFrame({
#     "Product": ["Mouse", "Keyboard", "Monitor"],
#     "OrderDate": ["2026-01-15", "2026-02-20", "2026-03-10"]
# })

# print(sales_data.dtypes)

# OrderDate column ki values dekhne mein dates jaisi hain, 
# lekin Pandas unhe aksar object (text) ke roop mein read karta hai.

# Problem: Text par hum date-related calculations seedhe us tarah 
# nahi kar sakte jaise proper datetime values par karte hain.

# Iske liye pd.to_datetime() use hota hai.

# 2. Date ko convert kaise karein?
# sales_data["OrderDate"] = pd.to_datetime(
#     sales_data["OrderDate"]
# )

# print(sales_data.dtypes)

# Ab OrderDate ka data type datetime64[ns] ho jayega.

# Matlab Pandas ab is column ko date/time data ke roop mein samajhta hai.

# 3. Data Analyst ke liye iska use

# Maan lo company poochti hai:

# January mein kitni sales hui?
# 2026 mein kis date ko order aaya?
# Do orders ke beech kitne din ka difference hai?

# In questions ko solve karne ke liye dates ko sahi format mein rakhna important hai.

# Ek aur useful example:

# sales_data["OrderDate"] = pd.to_datetime(
#     sales_data["OrderDate"],
#     errors="coerce"
# )

# errors="coerce" ka matlab hai ki agar koi date invalid hui, 
# toh Pandas us value ko NaT bana dega. 
# NaT ka matlab hai missing/invalid datetime value.

# Practice Questions — pd.to_datetime()
# ==========================================
# Pandas — Section 16: pd.to_datetime()
# ==========================================

# Q1. Create a DataFrame named order_data.
# Columns:
# OrderID: [101, 102, 103]
# OrderDate: ["2026-04-10", "2026-05-15", "2026-06-20"]
#
# Convert OrderDate into datetime format.
# Print the data types.

# import pandas as pd

# order_data = pd.DataFrame({
#     "OrderID": [101, 102, 103],
#     "OrderDate": ["2026-04-10", "2026-05-15", "2026-06-20"]
# })

# order_data["OrderDate"] = pd.to_datetime(order_data["OrderDate"])

# print(order_data)
# print(order_data.dtypes)
#--------------------------------------------------------

# Q2. Create a DataFrame named delivery_data.
# Columns:
# OrderID: [201, 202, 203]
# DeliveryDate: ["2026-07-01", "invalid_date", "2026-07-15"]
#
# Convert DeliveryDate into datetime format.
# Handle invalid dates using errors="coerce".

# import pandas as pd

# delivery_data = pd.DataFrame({
#     "OrderID": [201, 202, 203],
#     "DeliveryDate": ["2026-07-01", "invalid_date", "2026-07-15"]
# })

# delivery_data["DeliveryDate"] = pd.to_datetime(
#     delivery_data["DeliveryDate"],
#     errors = "coerce"
# )

# print(delivery_data)
#--------------------------------------------

# Q3. Create a DataFrame named employee_data.
# Columns:
# Employee: ["Aman", "Riya", "Karan"]
# JoiningDate: ["2024-01-10", "2023-06-15", "2025-09-20"]
#
# Convert JoiningDate into datetime format.
# Print the DataFrame and its data types.

# import pandas as pd

# employee_data = pd.DataFrame({
#     "Employee": ["Aman", "Riya", "Karan"],
#     "JoiningDate": ["2024-01-10", "2023-06-15", "2025-09-20"]
# })

# employee_data["JoiningDate"] = pd.to_datetime(
#     employee_data["JoiningDate"]
# )

# print(employee_data)
# print(employee_data.dtypes)
#_____________________________________________________________________________________________________

#==============================
# Topic 2: Extract Year
#==============================

# Date se year nikalna

# Data Analyst ko aksar data ko year ke hisaab se analyse karna hota hai, 
# jaise 2024 mein kitne orders hue ya 2025 mein kitni sales hui.

# Pandas mein date column se year nikalne ke liye .dt.year use karte hain.

# Example
# import pandas as pd

# sales_data = pd.DataFrame({
#     "Product": ["Mouse", "Keyboard", "Monitor"],
#     "OrderDate": ["2024-05-10", "2025-08-15", "2026-02-20"],
#     "Sales": [1200, 2500, 4000]
# })

# sales_data["OrderDate"] = pd.to_datetime(sales_data["OrderDate"])

# sales_data["Year"] = sales_data["OrderDate"].dt.year

# print(sales_data)

# Output:

#     Product  OrderDate  Sales  Year
# 0     Mouse 2024-05-10   1200  2024
# 1  Keyboard 2025-08-15   2500  2025
# 2   Monitor 2026-02-20   4000  2026
# Samjho kaise kaam karta hai
# sales_data["OrderDate"] → date column select karta hai.
# .dt → Pandas ke date-related operations use karne deta hai.
# .year → har date se year nikalta hai.
# sales_data["Year"] = ... → nikale gaye years ko ek naye column mein store karta hai.

# Dhyan do: .dt.year use karne se pehle date column ko pd.to_datetime() 
# se datetime format mein convert karna zaroori hai.

# Practice Questions
# ==========================================
# Pandas — Section 16: Extract Year
# ==========================================

# Q1. Create a DataFrame named order_data.
# Columns:
# OrderID: [101, 102, 103]
# OrderDate: ["2023-04-10", "2024-07-15", "2025-11-20"]
#
# Convert OrderDate to datetime format.
# Extract the year into a new column named Year.
# Print the DataFrame.

# import pandas as pd

# order_data = pd.DataFrame({
#     "OrderID": [101, 102, 103],
#     "OrderDate": ["2023-04-10", "2024-07-15", "2025-11-20"]
# })

# order_data["OrderDate"] = pd.to_datetime(order_data["OrderDate"])
# order_data["Year"] = order_data["OrderDate"].dt.year

# print(order_data)
#-------------------------------------------

# Q2. Create a DataFrame named employee_data.
# Columns:
# Employee: ["Aman", "Riya", "Karan"]
# JoiningDate: ["2020-01-10", "2022-06-15", "2024-09-20"]
#
# Convert JoiningDate to datetime format.
# Extract the year into a new column named JoiningYear.
# Print only Employee and JoiningYear.

# import pandas as pd

# employee_data = pd.DataFrame({
#     "Employee": ["Aman", "Riya", "Karan"],
# "JoiningDate": ["2020-01-10", "2022-06-15", "2024-09-20"]
# })

# employee_data["JoiningDate"] = pd.to_datetime(employee_data["JoiningDate"])
# employee_data["JoiningYear"] = employee_data["JoiningDate"].dt.year

# print(employee_data[["Employee", "JoiningYear"]])
#----------------------------------------------------

# Q3. Create a DataFrame named sales_data.
# Columns:
# Product: ["Mouse", "Keyboard", "Monitor"]
# OrderDate: ["2024-02-10", "2024-08-15", "2025-03-20"]
# Sales: [1500, 2500, 4000]
#
# Convert OrderDate to datetime format.
# Extract the year into a new column named Year.
# Calculate total Sales for each Year.

# import pandas as pd

# sales_data = pd.DataFrame({
#     "Product": ["Mouse", "Keyboard", "Monitor"],
#     "OrderDate": ["2024-02-10", "2024-08-15", "2025-03-20"],
#     "Sales": [1500, 2500, 4000]
# })

# # Convert OrderDate into datetime format
# sales_data["OrderDate"] = pd.to_datetime(sales_data["OrderDate"])

# # Extract year
# sales_data["Year"] = sales_data["OrderDate"].dt.year

# # Calculate total sales for each year
# yearly_sales = sales_data.groupby("Year")["Sales"].sum()

# print(yearly_sales)
#_____________________________________________________________________________________________________

#==============================
# Topic 3: Extract Month
#==============================

# Date column se month number nikalne ke liye Pandas mein .dt.month use karte hain.

# Data Analyst ke liye yeh useful hai, jaise monthly sales analyse 
# karna ya dekhna ki kis month mein kitne orders aaye.

# 1. Example
# import pandas as pd

# sales_data = pd.DataFrame({
#     "Product": ["Mouse", "Keyboard", "Monitor"],
#     "OrderDate": ["2026-01-15", "2026-06-20", "2026-12-10"],
#     "Sales": [1500, 2500, 4000]
# })

# sales_data["OrderDate"] = pd.to_datetime(sales_data["OrderDate"])

# sales_data["Month"] = sales_data["OrderDate"].dt.month

# print(sales_data)

# Output:

#     Product  OrderDate  Sales  Month
# 0     Mouse 2026-01-15   1500      1
# 1  Keyboard 2026-06-20   2500      6
# 2   Monitor 2026-12-10   4000     12
# 2. Kaise kaam karta hai?
# sales_data["Month"] = sales_data["OrderDate"].dt.month
# .dt — date-related operations ke liye.
# .month — date se month number nikalne ke liye.
# ["Month"] — nikale gaye month ko naye column mein store karta hai.

# Yaad rakho:

# January = 1
# June = 6
# December = 12

# Important: .dt.month month ka number deta hai, month ka naam nahi.

# Practice Questions
# ==========================================
# Pandas — Section 16: Extract Month
# ==========================================

# Q1. Create a DataFrame named order_data.
# Columns:
# OrderID: [101, 102, 103]
# OrderDate: ["2026-01-10", "2026-05-15", "2026-11-20"]

# Convert OrderDate to datetime format.
# Extract the month into a new column named Month.
# Print the DataFrame.

# import pandas as pd

# order_data = pd.DataFrame({
#     "OrderID": [101, 102, 103],
#     "OrderDate": ["2026-01-10", "2026-05-15", "2026-11-20"]
# })

# order_data["OrderDate"] = pd.to_datetime(
#     order_data["OrderDate"]
# )

# order_data["month"] = order_data["OrderDate"].dt.month
# print(order_data)
#-------------------------------------------------

# Q2. Create a DataFrame named employee_data.
# Columns:
# Employee: ["Aman", "Riya", "Karan"]
# JoiningDate: ["2020-03-10", "2022-07-15", "2024-12-20"]
#
# Convert JoiningDate to datetime format.
# Extract the month into a new column named JoiningMonth.
# Print only Employee and JoiningMonth.

# import pandas as pd

# employee_data = pd.DataFrame({
#     "Employee": ["Aman", "Riya", "Karan"],
#     "JoiningDate": ["2020-03-10", "2022-07-15", "2024-12-20"]
# })

# employee_data["JoiningDate"] = pd.to_datetime(
#     employee_data["JoiningDate"]
# )

# employee_data["JoiningMonth"] = employee_data["JoiningDate"].dt.month

# print(employee_data[["Employee", "JoiningMonth"]])
#--------------------------------------------------------

# Q3. Create a DataFrame named sales_data.
# Columns:
# Product: ["Mouse", "Keyboard", "Monitor", "Laptop"]
# OrderDate: ["2026-01-10", "2026-01-20", "2026-02-15", "2026-02-25"]
# Sales: [1000, 2000, 3000, 4000]
#
# Convert OrderDate to datetime format.
# Extract the month into a new column named Month.
# Calculate total Sales for each Month.

# import pandas as pd

# sales_data = pd.DataFrame({
#     "Product": ["Mouse", "Keyboard", "Monitor", "Laptop"],
#     "OrderDate": ["2026-01-10", "2026-01-20", "2026-02-15", "2026-02-25"],
#     "Sales": [1000, 2000, 3000, 4000]
# })

# sales_data["OrderDate"] = pd.to_datetime(
#     sales_data["OrderDate"]
# )

# sales_data["Month"] = sales_data["OrderDate"].dt.month

# Month_sale = sales_data.groupby("Month")["Sales"].sum()

# print(Month_sale)
#_____________________________________________________________________________________________________

#==============================
# Topic 4 — Extract Day
#==============================

# Date column se mahine ki tareekh (day number) nikalne ke liye .dt.day use karte hain.

# Example: 2026-02-25 mein:

# Year = 2026
# Month = 2
# Day = 25
# 1. Example
# import pandas as pd

# order_data = pd.DataFrame({
#     "OrderID": [101, 102, 103],
#     "OrderDate": ["2026-01-10", "2026-05-15", "2026-11-20"]
# })

# order_data["OrderDate"] = pd.to_datetime(order_data["OrderDate"])

# order_data["Day"] = order_data["OrderDate"].dt.day

# print(order_data)

# Output:

#    OrderID  OrderDate  Day
# 0      101 2026-01-10   10
# 1      102 2026-05-15   15
# 2      103 2026-11-20   20
# 2. Important difference
# Code	Kya nikalega?	Example: 2026-05-15
# .dt.year	Year	2026
# .dt.month	Month number	5
# .dt.day	Tareekh	15

# Teeno mein .dt common hai, bas aage ka attribute badalta hai.

# Practice Questions
# ==========================================
# Pandas — Section 16: Extract Day
# ==========================================

# Q1. Create a DataFrame named order_data.
# Columns:
# OrderID: [101, 102, 103]
# OrderDate: ["2026-01-05", "2026-05-17", "2026-11-28"]
#
# Convert OrderDate to datetime format.
# Extract the day into a new column named Day.
# Print the DataFrame.

# import pandas as pd

# order_data =pd.DataFrame({
#     "OrderID": [101, 102, 103],
#     "OrderDate": ["2026-01-05", "2026-05-17", "2026-11-28"]
# })

# order_data["OrderDate"] = pd.to_datetime(order_data["OrderDate"])

# order_data["Day"] = order_data["OrderDate"].dt.day
# print(order_data)
#-----------------------------------------------------

# Q2. Create a DataFrame named employee_data.
# Columns:
# Employee: ["Aman", "Riya", "Karan"]
# JoiningDate: ["2020-03-10", "2022-07-15", "2024-12-20"]
#
# Convert JoiningDate to datetime format.
# Extract the day into a new column named JoiningDay.
# Print only Employee and JoiningDay.

# import pandas as pd

# employee_data = pd.DataFrame({
#     "Employee": ["Aman", "Riya", "Karan"],
#     "JoiningDate": ["2020-03-10", "2022-07-15", "2024-12-20"]
# })

# employee_data["JoiningDate"] = pd.to_datetime(
#     employee_data["JoiningDate"]
# )

# employee_data["JoiningDay"] = employee_data["JoiningDate"].dt.day

# print(employee_data[["Employee", "JoiningDay"]])
#-----------------------------------------------------

# Q3. Create a DataFrame named sales_data.
# Columns:
# Product: ["Mouse", "Keyboard", "Monitor", "Laptop"]
# OrderDate: ["2026-01-10", "2026-01-20", "2026-02-15", "2026-02-25"]
# Sales: [1000, 2000, 3000, 4000]
#
# Convert OrderDate to datetime format.
# Extract the day into a new column named Day.
# Print only Product, Day and Sales.


# import pandas as pd

# sales_data = pd.DataFrame({
#     "Product": ["Mouse", "Keyboard", "Monitor", "Laptop"],
#     "OrderDate": ["2026-01-10", "2026-01-20", "2026-02-15", "2026-02-25"],
#     "Sales": [1000, 2000, 3000, 4000]
# })

# sales_data["OrderDate"] = pd.to_datetime(
#     sales_data["OrderDate"]
# )

# sales_data["Day"] = sales_data["OrderDate"].dt.day

# print(sales_data[["Product", "Day", "Sales"]])
##_____________________________________________________________________________________________________

#==============================
# Topic 5: Date Filtering
#==============================

# Date Filtering ka matlab hai date ke basis par DataFrame se specific rows select karna.

# Data Analyst ke kaam mein iska use hota hai, jaise:

# January ke orders dekhna.
# Kisi particular date ke baad ki sales check karna.
# Ek date range ke andar ke transactions nikalna.
# 1. Example: Specific date ke baad ka data

# Maan lo humein sirf 15 February 2026 ke baad ke orders chahiye.

# import pandas as pd

# sales_data = pd.DataFrame({
#     "Product": ["Mouse", "Keyboard", "Monitor", "Laptop"],
#     "OrderDate": ["2026-01-10", "2026-02-15", "2026-03-20", "2026-04-25"],
#     "Sales": [1000, 2000, 3000, 4000]
# })

# sales_data["OrderDate"] = pd.to_datetime(sales_data["OrderDate"])

# filtered_data = sales_data[
#     sales_data["OrderDate"] > "2026-02-15"
# ]

# print(filtered_data)

# Output:

#     Product  OrderDate  Sales
# 2   Monitor 2026-03-20   3000
# 3    Laptop 2026-04-25   4000

# Samjho:

# > ka matlab hai date ke baad.
# < ka matlab hai date se pehle.
# >= ka matlab hai date par ya uske baad.
# <= ka matlab hai date par ya usse pehle.

# Dhyan do: > lagane par 15 February wali row include nahi hogi.

# 2. Example: Date range ke beech ka data

# Maan lo humein 1 February se 31 March 2026 tak ke orders chahiye.

# filtered_data = sales_data[
#     (sales_data["OrderDate"] >= "2026-02-01") &
#     (sales_data["OrderDate"] <= "2026-03-31")
# ]

# print(filtered_data)

# Output:

#     Product  OrderDate  Sales
# 1  Keyboard 2026-02-15   2000
# 2   Monitor 2026-03-20   3000

# Yahan & ka matlab hai dono conditions true honi chahiye.

# Important: Multiple conditions ko combine karte waqt har condition ke around parentheses () lagao.

# Practice Questions
# ==========================================
# Pandas — Section 16: Date Filtering
# ==========================================

# Q1. Create a DataFrame named order_data.
# Columns:
# OrderID: [101, 102, 103, 104]
# OrderDate: ["2026-01-10", "2026-02-15", "2026-03-20", "2026-04-25"]
# Sales: [1000, 2000, 3000, 4000]

# Convert OrderDate to datetime format.
# Filter and print only those orders whose OrderDate
# is after "2026-02-15".

# import pandas as pd

# order_data = pd.DataFrame({
#     "OrderID": [101, 102, 103, 104],
#     "OrderDate": ["2026-01-10", "2026-02-15", "2026-03-20", "2026-04-25"],
#     "Sales": [1000, 2000, 3000, 4000]
# })

# order_data["OrderDate"]= pd.to_datetime(order_data["OrderDate"])

# filter_data = order_data[
#     order_data["OrderDate"] > "2026-02-15"
# ]
# print(filter_data)
#--------------------------------------

# Q2. Use the same order_data DataFrame.
# Filter and print orders whose OrderDate is on or
# after "2026-02-15".

# import pandas as pd

# order_data = pd.DataFrame({
#     "OrderID": [101, 102, 103, 104],
#     "OrderDate": ["2026-01-10", "2026-02-15", "2026-03-20", "2026-04-25"],
#     "Sales": [1000, 2000, 3000, 4000]
# })

# order_data["OrderDate"] = pd.to_datetime(order_data["OrderDate"])

# filtered_data = order_data[
#     order_data["OrderDate"] >= "2026-02-15"
# ]

# print(filtered_data)
#------------------------------------------------

# Q3. Use the same order_data DataFrame.
# Filter and print orders whose OrderDate is between
# "2026-02-01" and "2026-03-31", including both dates

# import pandas as pd

# order_data = pd.DataFrame({
#     "OrderID": [101, 102, 103, 104],
#     "OrderDate": ["2026-01-10", "2026-02-15", "2026-03-20", "2026-04-25"],
#     "Sales": [1000, 2000, 3000, 4000]
# })

# order_data["OrderDate"] = pd.to_datetime(order_data["OrderDate"])

# filter_data = order_data[
#     (order_data["OrderDate"]>= "2026-02-01") &
#     (order_data["OrderDate"]<= "2026-03-31")
# ]

# print(filter_data)
#_____________________________________________________________________________________________________

#==============================
# Topic 6: Date Difference
#==============================

# Date Difference ka matlab hai do dates ke beech kitne din ka difference hai, woh calculate karna.

# Data Analyst ke liye iska use:

# Order aur delivery ke beech kitne din lage.
# Employee ko company join kiye kitne din hue.
# Do transactions ke beech kitne din ka gap hai.
# 1. Example: Order aur Delivery ke beech kitne din lage?
# import pandas as pd

# delivery_data = pd.DataFrame({
#     "OrderID": [101, 102, 103],
#     "OrderDate": ["2026-01-01", "2026-02-10", "2026-03-15"],
#     "DeliveryDate": ["2026-01-05", "2026-02-18", "2026-03-20"]
# })

# delivery_data["OrderDate"] = pd.to_datetime(delivery_data["OrderDate"])
# delivery_data["DeliveryDate"] = pd.to_datetime(delivery_data["DeliveryDate"])

# delivery_data["DeliveryDays"] = (
#     delivery_data["DeliveryDate"] - delivery_data["OrderDate"]
# ).dt.days

# print(delivery_data)
# Output
#    OrderID  OrderDate DeliveryDate  DeliveryDays
# 0       101 2026-01-01   2026-01-05             4
# 1       102 2026-02-10   2026-02-18             8
# 2       103 2026-03-15   2026-03-20             5
# 2. Code ko samjho

# Step 1: Dono columns ko datetime mein convert karo.

# delivery_data["OrderDate"] = pd.to_datetime(delivery_data["OrderDate"])
# delivery_data["DeliveryDate"] = pd.to_datetime(delivery_data["DeliveryDate"])

# Step 2: Dono dates ko subtract karo.

# delivery_data["DeliveryDate"] - delivery_data["OrderDate"]

# Isse date difference milta hai, jo Pandas mein Timedelta ke form mein hota hai.

# Step 3: Sirf din nikaalo.

# .dt.days

# Yeh difference ko days ki sankhya mein convert karta hai.

# Example: 5 January − 1 January ka difference 4 days hai, 5 days nahi.

# Practice Questions
# ==========================================
# Pandas — Section 16: Date Difference
# ==========================================

# Q1. Create a DataFrame named delivery_data.
# Columns:
# OrderID: [101, 102, 103]
# OrderDate: ["2026-01-01", "2026-02-10", "2026-03-15"]
# DeliveryDate: ["2026-01-06", "2026-02-20", "2026-03-25"]
#
# Convert both date columns to datetime format.
# Calculate the difference in days.
# Store the result in a new column named DeliveryDays.
# Print the DataFrame.

# import pandas as pd

# delivery_data = pd.DataFrame({
#     "OrderID": [101, 102, 103],
#     "OrderDate": ["2026-01-01", "2026-02-10", "2026-03-15"],
#     "DeliveryDate": ["2026-01-06", "2026-02-20", "2026-03-25"]
# })

# delivery_data["OrderDate"] = pd.to_datetime(delivery_data["OrderDate"])
# delivery_data["DeliveryDate"] = pd.to_datetime(delivery_data["DeliveryDate"])

# delivery_data["DeliveryDays"] = (
#     delivery_data["DeliveryDate"] - delivery_data["OrderDate"]
# ).dt.days

# print(delivery_data)
#-------------------------------------------------

# Q2. Create a DataFrame named employee_data.
# Columns:
# Employee: ["Aman", "Riya", "Karan"]
# JoiningDate: ["2026-01-01", "2026-02-01", "2026-03-01"]
# LastDate: ["2026-01-11", "2026-02-16", "2026-03-21"]
#
# Convert both date columns to datetime format.
# Calculate the difference in days.
# Store the result in a new column named DaysWorked.
# Print only Employee and DaysWorked.

# import pandas as pd

# employee_data = pd.DataFrame({
#     "Employee": ["Aman", "Riya", "Karan"],
#     "JoiningDate": ["2026-01-01", "2026-02-01", "2026-03-01"],
#     "LastDate": ["2026-01-11", "2026-02-16", "2026-03-21"]
# })

# employee_data["JoiningDate"] = pd.to_datetime(employee_data["JoiningDate"])
# employee_data["LastDate"] = pd.to_datetime(employee_data["LastDate"])

# employee_data["DaysWorked"] = (
#     employee_data["JoiningDate"] - employee_data["LastDate"]
# ).dt.days

# print(employee_data)
#------------------------------------------

# Q3. Create a DataFrame named order_data.
# Columns:
# OrderID: [201, 202, 203]
# OrderDate: ["2026-04-01", "2026-04-10", "2026-04-20"]
# DeliveryDate: ["2026-04-04", "2026-04-15", "2026-04-30"]
#
# Convert both date columns to datetime format.
# Calculate the difference in days.
# Store the result in a new column named DeliveryDays.
# Print only OrderID and DeliveryDays.

# import pandas as pd


# order_data = pd.DataFrame({
#     "OrderID": [201, 202, 203],
#     "OrderDate": ["2026-04-01", "2026-04-10", "2026-04-20"],
#     "DeliveryDate": ["2026-04-04", "2026-04-15", "2026-04-30"]
# })

# order_data["OrderDate"] = pd.to_datetime(order_data["OrderDate"])
# order_data["DeliveryDate"] = pd.to_datetime(order_data["DeliveryDate"])

# order_data["DeliveryDays"] =(
#     order_data["OrderDate"] - order_data["DeliveryDate"]
# ).dt.days

# print(order_data[["OrderID", "DeliveryDays"]])

#_____________________________________________________________________________________________________

#==============================
# Topic 7 — .dt accessor
#==============================

# .dt Pandas mein datetime column ke parts aur properties ko access karne ke liye use hota hai.

# Ab tak tum .dt.year, .dt.month, .dt.day aur .dt.days use kar chuke ho. 
# Aaj inka connection samjhenge aur kuch useful date properties dekhenge.

# 1. Example
# import pandas as pd

# sales_data = pd.DataFrame({
#     "Product": ["Mouse", "Keyboard", "Monitor"],
#     "OrderDate": ["2026-01-10", "2026-05-17", "2026-11-28"]
# })

# sales_data["OrderDate"] = pd.to_datetime(sales_data["OrderDate"])

# sales_data["Year"] = sales_data["OrderDate"].dt.year
# sales_data["Month"] = sales_data["OrderDate"].dt.month
# sales_data["Day"] = sales_data["OrderDate"].dt.day
# sales_data["Weekday"] = sales_data["OrderDate"].dt.day_name()

# print(sales_data)

# Output:

#     Product  OrderDate  Year  Month  Day   Weekday
# 0     Mouse 2026-01-10  2026      1   10  Saturday
# 1  Keyboard 2026-05-17  2026      5   17    Sunday
# 2   Monitor 2026-11-28  2026     11   28  Saturday
# 2. Important .dt properties
# Code	Kya nikalta hai?	Example
# .dt.year	Year	2026
# .dt.month	Month number	5
# .dt.day	Month ki tareekh	17
# .dt.day_name()	Weekday ka naam	Sunday
# .dt.dayofweek	Weekday ka number	6 for Sunday
# .dt.days	Timedelta difference ke days	7

# Ek important difference: .dt.day date column par use hota hai, 
# jabki .dt.days date difference ke Timedelta result par use hota hai.

# 3. Data Analyst ke liye iska use

# Maan lo tumhe pata karna hai ki Sunday ko kitni sales hui. 
# Tum pehle weekday nikal sakte ho aur phir filter kar sakte ho:

# sales_data["Weekday"] = sales_data["OrderDate"].dt.day_name()

# sunday_sales = sales_data[
#     sales_data["Weekday"] == "Sunday"
# ]

# print(sunday_sales)

# Isse sirf Sunday wale orders milenge.

# Practice Questions
# ==========================================
# Pandas — Section 16: .dt Accessor
# ==========================================

# Q1. Create a DataFrame named order_data.
# Columns:
# OrderID: [101, 102, 103]
# OrderDate: ["2026-01-10", "2026-05-17", "2026-11-28"]

# Convert OrderDate to datetime format.
# Extract Year, Month and Day into separate columns.
# Print the DataFrame.

# import pandas as pd

# order_data = pd.DataFrame({
#     "OrderID": [101, 102, 103],
#     "OrderDate": ["2026-01-10", "2026-05-17", "2026-11-28"]
# })

# order_data["OrderDate"] = pd.to_datetime(order_data["OrderDate"])

# order_data["Year"] = order_data["OrderDate"].dt.year
# order_data["Month"] = order_data["OrderDate"].dt.month
# order_data["Day"] = order_data["OrderDate"].dt.day

# print(order_data)
#----------------------------------------------

# Q2. Use the same order_data DataFrame.
# Extract the weekday name into a new column named Weekday.
# Print only OrderID and Weekday.

# import pandas as pd

# order_data = pd.DataFrame({
#     "OrderID": [101, 102, 103],
#     "OrderDate": ["2026-01-10", "2026-05-17", "2026-11-28"]
# })

# order_data["OrderDate"] = pd.to_datetime(order_data["OrderDate"])

# order_data["Weekday"] = order_data["OrderDate"].dt.day_name()

# print(order_data[["OrderID", "Weekday"]])
#-----------------------------------------------

# Q3. Use the same order_data DataFrame.
# Filter and print only those orders that were placed on Sunday.

import pandas as pd

order_data = pd.DataFrame({
    "OrderID": [101, 102, 103],
    "OrderDate": ["2026-01-10", "2026-05-17", "2026-11-28"]
})

order_data["OrderDate"] = pd.to_datetime(order_data["OrderDate"])

order_data["weekday"] = order_data["OrderDate"].dt.day_name()

sanday_order = order_data[
    order_data["weekday"] == "Sunday"
]

print(sanday_order)