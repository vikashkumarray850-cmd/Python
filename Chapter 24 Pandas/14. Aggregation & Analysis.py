# ========================================
# CODE NUMBERING BY:-

# 1 sum()             [36 TO 99]
# 2 mean()            [103 TO 160]
# 3 median()          [163 TO 331]
# 4 min()             [335 TO 389]
# 5 max()             [393 TO 427]
# 6 count()           [431 TO 488]
# 7 std()             [492 TO 583]
# 8 value_counts()    [587 TO 685]

# =========================================

#========================================
# Complete Topic Overview
#========================================


# | No. | Topic            | Kya seekhenge?                              |
# | --: | ---------------- | ------------------------------------------- |
# |   1 | `sum()`          | Column ki sabhi numeric values ka total     |
# |   2 | `mean()`         | Column ki values ka average                 |
# |   3 | `median()`       | Data ki middle value aur outliers ka effect |
# |   4 | `min()`          | Column ki sabse chhoti value                |
# |   5 | `max()`          | Column ki sabse badi value                  |
# |   6 | `count()`        | Column mein non-missing values ki ginti     |
# |   7 | `std()`          | Values average se kitni faili hui hain      |
# |   8 | `value_counts()` | Har unique value kitni baar aayi hai        |



#==================================
# Section 13 — GroupBy
#---------------------------------
# Topic 1 — sum() (Short Revision)
#==================================

# sum() ka use kisi numeric column ki values ko jodkar total nikalne ke liye hota hai.

# Example:

# import pandas as pd

# event_data = pd.DataFrame({
#     "Event": ["Concert", "Fair", "Festival", "Concert"],
#     "TicketsSold": [120, 200, 180, 150]
# })

# total_tickets = event_data["TicketsSold"].sum()

# print(total_tickets)

# Output:

# 650

# Calculation: 120 + 200 + 180 + 150 = 650

# Yahan:

# event_data["TicketsSold"] → TicketsSold column select karta hai.
# .sum() → us column ka total nikalta hai.

# ==========================================
# Pandas — Section 14: sum() Revision
# ==========================================

# Q1. Create a DataFrame named event_data with these columns:
# Event: ["Concert", "Fair", "Concert", "Festival"]
# TicketsSold: [120, 200, 150, 180]
# Calculate the total TicketsSold.

# import pandas as pd

# event_data = pd.DataFrame({
#     "Event": ["Concert", "Fair", "Concert", "Festival"],
#     "TicketsSold": [120, 200, 150, 180],
# })

# result = event_data["TicketsSold"].sum()
# print(result)
#-------------------------------------------------------

# Q2. Create a DataFrame named fuel_data with these columns:
# Vehicle: ["Bus", "Car", "Truck", "Van"]
# FuelCost: [2500, 800, 3200, 1200]
# Calculate the total FuelCost.

# import pandas as pd

# fuel_data = pd.DataFrame({
#     "Vehicle": ["Bus", "Car", "Truck", "Van"],
#     "FuelCost": [2500, 800, 3200, 1200]
# })

# total_cost = fuel_data["FuelCost"].sum()

# print(total_cost)
#_____________________________________________________________________________________________________

#===================================
# Topic 2 — mean() (Short Revision)
#===================================

# mean() ka use numeric values ka average nikalne ke liye hota hai.

# Example:

# import pandas as pd

# visitor_data = pd.DataFrame({
#     "Month": ["Jan", "Feb", "Mar", "Apr"],
#     "Visitors": [100, 200, 300, 400]
# })

# average_visitors = visitor_data["Visitors"].mean()

# print(average_visitors)

# Output:

# 250.0

# Calculation: (100 + 200 + 300 + 400) ÷ 4 = 250

# Practice Questions — mean()
# ==========================================
# Pandas — Section 14: mean() Revision
# ==========================================

# Q1. Create a DataFrame named delivery_data with these columns:
# City: ["Delhi", "Mumbai", "Kolkata", "Chennai"]
# DeliveryTime: [30, 45, 25, 40]
# Calculate the average DeliveryTime.

# import pandas as pd

# delivery_data =pd.DataFrame({
#     "City": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
#     "DeliveryTime": [30, 45, 25, 40]
# })
# avg_time = delivery_data["DeliveryTime"].mean()
# print(avg_time)
#-------------------------------------------------------

# Q2. Create a DataFrame named exam_results with these columns:
# Student: ["Amit", "Neha", "Rahul", "Priya"]
# Marks: [75, 85, 65, 95]
# Calculate the average Marks.

# import pandas as pd

# exam_results =pd.DataFrame({
#     "Student": ["Amit", "Neha", "Rahul", "Priya"],
#     "Marks": [75, 85, 65, 95]
# })
# avg_marks = exam_results["Marks"].mean()
# print(avg_marks)
#_____________________________________________________________________________________________________

#==============================
# Topic 3 — median()
#==============================

# 1. median() kya hota hai?

# median() ka use data ki middle value nikalne ke liye hota hai.

# Median nikalne se pehle values ko ascending order (chhoti se badi) mein arrange karte hain.

# Example:

# import pandas as pd

# salary_data = pd.DataFrame({
#     "Employee": ["A", "B", "C", "D", "E"],
#     "Salary": [20000, 25000, 30000, 35000, 90000]
# })

# result = salary_data["Salary"].median()

# print(result)

# Output:

# 30000.0

# Values ascending order mein hain:

# 20000, 25000, 30000, 35000, 90000

# Beech ki value 30000 hai, isliye median 30000 hai.

# 2. Agar values ki sankhya even ho toh?

# Maan lo data hai:

# 100, 200, 300, 400

# Ismein 4 values hain, isliye ek middle value nahi hai. Beech ki dono values 200 aur 300 hain.

# Median = (200 + 300) ÷ 2 = 250

# Pandas khud ye calculation kar leta hai:

# numbers = pd.Series([100, 200, 300, 400])

# print(numbers.median())

# Output:

# 250.0
# 3. Data Analyst ke liye median kyu important hai?

# Maan lo employees ki salaries hain:

# 25000, 28000, 30000, 32000, 200000

# Yahan ek employee ki salary baaki salaries se kaafi zyada hai.

# Mean = 63,000
# Median = 30,000

# Mean high salary ki wajah se kaafi badh gaya, jabki median middle salary ko represent karta hai.

# Isliye salary analysis mein mean aur median dono dekhna useful hota hai.

# Ab ek interactive example bhi dekho—values badal kar samajh sakte ho ki mean kaise change hota hai.

# Original amounts
# Equal shares
# 2
# 4
# 7
# x
# ˉ
# =
# 3
# 2+4+7
# 	​

# =
# 3
# 13
# 	​

# =4 
# 3
# 1
# 	​

# x̄ is the arithmetic mean (simple average)
# x
# 1
# 	​

# x
# 1
# 	​

# x
# 2
# 	​

# x
# 2
# 	​

# x
# 3
# 	​

# x
# 3
# 	​

# Give feedback
# Practice Questions — median()
# ==========================================
# Pandas — Section 14: median()
# ==========================================

# Q1. Create a DataFrame named rent_data with these columns:
# Area: ["North", "South", "East", "West", "Central"]
# MonthlyRent: [12000, 15000, 10000, 18000, 14000]
# Calculate the median MonthlyRent.

# import pandas as pd

# rent_data = pd.DataFrame({
#     "Area": ["North", "South", "East", "West", "Central"],
#     "MonthlyRent": [12000, 15000, 10000, 18000, 14000]
# })

# median_value = rent_data["MonthlyRent"].median()
# print(median_value)
#------------------------------------------------------

# Q2. Create a DataFrame named response_data with these columns:
# Team: ["A", "B", "C", "D", "E", "F"]
# ResponseTime: [12, 18, 10, 25, 15, 20]
# Calculate the median ResponseTime.

# import pandas as pd

# response_data = pd.DataFrame({
#     "Team": ["A", "B", "C", "D", "E", "F"],
#     "ResponseTime": [12, 18, 10, 25, 15, 20]
# })
# result = response_data["ResponseTime"].median()
# print(result)
#-------------------------------------------------------

# Q3. Create a DataFrame named transaction_data with these columns:
# TransactionID: [101, 102, 103, 104, 105]
# Amount: [500, 700, 600, 800, 5000]
# Calculate both the mean and median Amount.

# import pandas as pd

# transaction_data = pd.DataFrame({
#     "TransactionID": [101, 102, 103, 104, 105],
#     "Amount": [500, 700, 600, 800, 5000]
# })

# mean_Amount = transaction_data["Amount"].mean()
# median_Amount = transaction_data["Amount"].median()

# print(mean_Amount)
# print(median_Amount)
#_____________________________________________________________________________________________________

#================================
# Topic 4: min() (Short Revision)
#================================

# min() kisi numeric column ki sabse chhoti value nikalta hai.

# Example:

# import pandas as pd

# order_data = pd.DataFrame({
#     "OrderID": [101, 102, 103, 104],
#     "DeliveryDays": [5, 2, 7, 3]
# })

# result = order_data["DeliveryDays"].min()
# print(result)

# Output:

# 2
# Practice Questions — min()
# ==========================================
# Pandas — Section 14: min() Revision
# ==========================================

# Q1. Create a DataFrame named exam_scores with these columns:
# Student: ["Amit", "Neha", "Rahul", "Priya"]
# Marks: [78, 65, 92, 54]
# Find the minimum Marks.

# import pandas as pd

# exam_scores = pd.DataFrame({
#     "Student": ["Amit", "Neha", "Rahul", "Priya"],
#     "Marks": [78, 65, 92, 54]
# })

# result = exam_scores["Marks"].min()
# print(result)
#----------------------------------------------------

# Q2. Create a DataFrame named shipment_data with these columns:
# ShipmentID: [201, 202, 203, 204, 205]
# Weight: [25, 18, 32, 12, 21]
# Find the minimum Weight.

# import pandas as pd

# shipment_data = pd.DataFrame({
#     "ShipmentID": [201, 202, 203, 204, 205],
#     "Weight": [25, 18, 32, 12, 21]
# })

# result = shipment_data["Weight"].min()
# print(result)
#_____________________________________________________________________________________________________

#==============================
# Topic 5 — max() (Short Revision)
#==============================

# ==========================================
# Pandas — Section 14: max() Revision
# ==========================================

# Q1. Create a DataFrame named rainfall_data with these columns:
# City: ["Pune", "Jaipur", "Kochi", "Shimla"]
# Rainfall: [40, 15, 80, 55]
# Find the maximum Rainfall.

# import pandas as pd

# rainfall_data = pd.DataFrame({
#     "City": ["Pune", "Jaipur", "Kochi", "Shimla"],
#     "Rainfall": [40, 15, 80, 55]
# })

# print(rainfall_data["Rainfall"].max())
#--------------------------------------------

# Q2. Create a DataFrame named auction_data with these columns:
# Item: ["Painting", "Vase", "Watch", "Sculpture", "Book"]
# BidAmount: [12000, 8500, 22000, 18000, 3000]
# Find the maximum BidAmount.

# import pandas as pd

# auction_data = pd.DataFrame({
#     "Item": ["Painting", "Vase", "Watch", "Sculpture", "Book"],
#     "BidAmount": [12000, 8500, 22000, 18000, 3000]
# })

# print(auction_data["BidAmount"].max())
#_____________________________________________________________________________________________________

#==============================
#Topic 6 — count() (Short Revision).
#==============================

# 1. count() kya karta hai?

# count() kisi column mein non-missing values ki ginti karta hai. 
# NaN values ko count nahi karta.

# Example:

# import pandas as pd

# course_data = pd.DataFrame({
#     "Student": ["Amit", "Neha", "Rahul", "Priya"],
#     "Score": [75, 80, None, 90]
# })

# print(course_data["Score"].count())

# Output:

# 3

# Kyunki Score column mein 3 valid values hain; None count nahi hota.

# 2. Practice Questions — count()
# ==========================================
# Pandas — Section 14: count() Revision
# ==========================================

# Q1. Create a DataFrame named library_data with these columns:
# Book: ["Python", "SQL", "Excel", "Power BI"]
# Copies: [10, 15, 8, 12]
# Find the count of values in the Copies column.

# import pandas as pd

# library_data = pd.DataFrame({
#     "Book": ["Python", "SQL", "Excel", "Power BI"],
#     "Copies": [10, 15, 8, 12]
# })

# print(library_data["Copies"].count())
#--------------------------------------------------

# Q2. Create a DataFrame named feedback_data with these columns:
# Customer: ["Amit", "Neha", "Ravi", "Priya", "Mohit"]
# Rating: [4, None, 5, 3, None]
# Find the count of values in the Rating column.

# import pandas as pd

# feedback_data = pd.DataFrame({
#     "Customer": ["Amit", "Neha", "Ravi", "Priya", "Mohit"],
#     "Rating": [4, None, 5, 3, None]
# })

# print(feedback_data["Rating"].count())
#_____________________________________________________________________________________________________

#====================================
# Topic 7: std() — Standard Deviation
#====================================

# 1. std() kya hota hai?

# std() ka full form Standard Deviation hai. 
# Yeh batata hai ki data ki values average (mean) se kitni faili hui hain.

# Low standard deviation: Values ek-doosre aur average ke paas hain.
# High standard deviation: Values zyada faili hui hain.
# 2. Example
# import pandas as pd

# marks_data = pd.DataFrame({
#     "Student": ["Amit", "Neha", "Ravi", "Priya"],
#     "Marks": [48, 50, 52, 50]
# })

# print(marks_data["Marks"].std())

# Output lagbhag:

# 1.632993

# Marks 48, 50, 52 aur 50 ek-doosre ke paas hain, isliye standard deviation kam hai.

# Ab doosra example dekho:

# marks_data = pd.DataFrame({
#     "Student": ["Amit", "Neha", "Ravi", "Priya"],
#     "Marks": [10, 30, 70, 90]
# })

# print(marks_data["Marks"].std())

# Output lagbhag:

# 36.055513

# Is baar marks zyada faile hue hain, isliye standard deviation bhi zyada hai.

# Important: Pandas mein Series.std() by default sample standard deviation calculate karta hai. 
# Abhi formula yaad karne ki zaroorat nahi hai.

# 3. Practice Questions — std()
# ==========================================
# Pandas — Section 14: Standard Deviation
# ==========================================

# Q1. Create a DataFrame named temperature_data with these columns:
# City: ["Delhi", "Mumbai", "Kolkata", "Chennai"]
# Temperature: [30, 32, 31, 33]
# Calculate the standard deviation of "Temperature".

# import pandas as pd

# temperature_data = pd.DataFrame({
#     "City": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
#     "Temperature": [30, 32, 31, 33]
# })

# print(temperature_data["Temperature"].std())
#------------------------------------------------------

# Q2. Create a DataFrame named player_data with these columns:
# Player: ["Aman", "Rohit", "Karan", "Vijay", "Sohan"]
# Runs: [10, 45, 25, 60, 20]
# Calculate the standard deviation of Runs.

# import pandas as pd

# player_data = pd.DataFrame({
#     "Player": ["Aman", "Rohit", "Karan", "Vijay", "Sohan"],
#     "Runs": [10, 45, 25, 60, 20]
# })

# print(player_data["Runs"].std())
#------------------------------------------------------------

# Q3. Create a DataFrame named delivery_data with these columns:
# OrderID: [101, 102, 103, 104, 105]
# DeliveryDays: [2, 8, 4, 10, 6]
# Calculate the standard deviation of DeliveryDays.

# import pandas as pd

# delivery_data = pd.DataFrame({
#     "OrderID": [101, 102, 103, 104, 105],
#     "DeliveryDays": [2, 8, 4, 10, 6]
# })

# print(delivery_data["DeliveryDays"].std())
#_____________________________________________________________________________________________________

#==============================
# Topic 8 — value_counts()
#==============================

# value_counts() kya karta hai?

# value_counts() kisi column mein har unique value kitni baar aayi hai, uski counting karta hai.

# Maan lo ek shop mein alag-alag payment methods use hue:

# import pandas as pd

# payment_data = pd.DataFrame({
#     "Customer": ["Amit", "Neha", "Ravi", "Priya", "Mohit", "Kiran"],
#     "Payment": ["UPI", "Cash", "UPI", "Card", "Cash", "UPI"]
# })

# print(payment_data["Payment"].value_counts())

# Output:

# Payment
# UPI     3
# Cash    2
# Card    1
# Name: count, dtype: int64

# Samjho:

# UPI → 3 baar use hua.
# Cash → 2 baar use hua.
# Card → 1 baar use hua.

# Yahan value_counts() ne unique payment methods ko count kiya 
# aur default mein sabse zyada aane wali value ko pehle dikhaya.

# 3. Data Analyst ke liye iska use

# Maan lo tumhe customer data diya gaya hai aur pata karna hai:

# Kitne customers ne Premium plan liya?
# Kitne customers ne Basic plan liya?
# Kaunsa product sabse zyada baar order hua?
# Survey mein kaunsi category sabse zyada select hui?

# Aise questions ke liye value_counts() bahut useful hai.

# 4. Practice Questions — value_counts()

# Ab tum ye 3 questions khud solve karo. Solutions abhi nahi diye gaye hain.

# ==========================================
# Pandas — Section 14: value_counts()
# ==========================================

# Q1. Create a DataFrame named device_data with these columns:
# User: ["Aman", "Riya", "Karan", "Pooja", "Rahul", "Neha"]
# Device: ["Mobile", "Laptop", "Mobile", "Tablet", "Laptop", "Mobile"]
# Count how many times each value appears in the Device column.

# import pandas as pd

# device_data = pd.DataFrame({
#     "User": ["Aman", "Riya", "Karan", "Pooja", "Rahul", "Neha"],
#     "Device": ["Mobile", "Laptop", "Mobile", "Tablet", "Laptop", "Mobile"]
# })

# print(device_data["Device"].value_counts())
#---------------------------------------------------

# Q2. Create a DataFrame named order_status_data with these columns:
# OrderID: [101, 102, 103, 104, 105, 106, 107]
# Status: ["Delivered", "Pending", "Delivered", "Cancelled",
#          "Pending", "Delivered", "Pending"]
# Count how many times each value appears in the Status column.

# import pandas as pd

# order_status_data = pd.DataFrame({
#     "OrderID": [101, 102, 103, 104, 105, 106, 107],
#     "Status": ["Delivered", "Pending", "Delivered", "Cancelled",
#          "Pending", "Delivered", "Pending"]
# })

# print(order_status_data["Status"].value_counts())
#--------------------------------------------------------------

# Q3. Create a DataFrame named course_data with these columns:
# Student: ["Amit", "Neha", "Ravi", "Priya", "Mohit", "Kiran", "Simran"]
# Course: ["Python", "SQL", "Python", "Excel", "SQL", "Python", "Excel"]
# Count how many times each value appears in the Course column

import pandas as pd

course_data = pd.DataFrame({
    "Student": ["Amit", "Neha", "Ravi", "Priya", "Mohit", "Kiran", "Simran"],
    "Course": ["Python", "SQL", "Python", "Excel", "SQL", "Python", "Excel"]
})

print(course_data["Course"].value_counts())