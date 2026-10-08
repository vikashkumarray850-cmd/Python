#========================================
# # 14: Practical NumPy for Data Analysis
#========================================
#-------------------------------
# Sales Data
# Employee Salaries
# Marks Data
# Product Prices
# Filtering Data
# Calculations on Data
#--------------------------------

# ========================================
# CODE NUMBERING BY:-

# 29  TO 124 Sales Data
# 128 TO 199 Employee Salaries
# 203 TO 281 Marks Data
# 678 TO 786 Product Prices
# 577 TO 688 Filtering Data
# 456 TO 786 Calculations on Data
# ========================================

# Ab hum NumPy ka practical Data Analyst part start kar rahe hain.

# Ab tak humne individual concepts seekhe. Ab unko combine karenge.

#==============================
# 1. Sales Data
#==============================

# Maan lo company ke paas 7 days ki sales hai:

# import numpy as np

# sales = np.array([1200, 1500, 1800, 1100, 2000, 1700, 2200])

# print(sales)

# Ab hum analysis kar sakte hain:

# print("Total Sales:", np.sum(sales))
# print("Average Sales:", np.mean(sales))
# print("Minimum Sales:", np.min(sales))
# print("Maximum Sales:", np.max(sales))

# Yaani ek hi dataset se:

# np.sum()   → Total
# np.mean()  → Average
# np.min()   → Lowest
# np.max()   → Highest
# Filtering bhi kar sakte hain

# Agar hume 1500 se zyada sales dekhni hain:

# high_sales = sales[sales > 1500]

# print(high_sales)

# Ye sirf matching values return karega.

# Data Analyst ka actual flow
# Sales Data
#     ↓
# NumPy Array
#     ↓
# Total / Average / Min / Max
#     ↓
# Condition
#     ↓
# Filtered Data
#     ↓
# Analysis

# Ab hum isi type ke practical questions karenge.

# Practice — Sales Data
# ==========================================
# NumPy — Practical Sales Data
# ==========================================

# Q1. Create a NumPy array representing 7 days of sales:
# [1200, 1500, 1800, 1100, 2000, 1700, 2200]
#
# Calculate and print:
# - Total sales
# - Average sales
# - Minimum sales
# - Maximum sales

# import numpy as np
# sales = np.array([1200, 1500, 1800, 1100, 2000, 1700, 2200])
# print(np.sum(sales))
# print(np.mean(sales))
# print(np.min(sales))
# print(np.max(sales))
#--------------------------------------

# Q2. Using the same sales data:
# [1200, 1500, 1800, 1100, 2000, 1700, 2200]
#
# Filter and print all sales values greater than 1500.

# import numpy as np
# sales = np.array([1200, 1500, 1800, 1100, 2000, 1700, 2200])
# result = sales [sales > 1500]
# print(result)
#---------------------------------------------

# Q3. Using the same sales data:
# [1200, 1500, 1800, 1100, 2000, 1700, 2200]
#
# Calculate and print the number of days
# where sales were greater than 1500.

# import numpy as np

# sales = np.array([1200, 1500, 1800, 1100, 2000, 1700, 2200])

# result = sales > 1500

# print(result)
# print(np.sum(result))
#_____________________________________________________________________________________________

#==============================
# 2. Employee Salaries
#==============================

# Data Analyst ke kaam mein salary data par humein 
# aksar ye cheezein nikalni hoti hain:

# Total salary
# Average salary
# Minimum salary
# Maximum salary
# Kisi condition ke basis par salary filter karna
# Kitne employees condition ko satisfy karte hain

# Example:

# import numpy as np

# salaries = np.array([30000, 45000, 55000, 40000, 60000, 35000])

# print("Total:", np.sum(salaries))
# print("Average:", np.mean(salaries))
# print("Minimum:", np.min(salaries))
# print("Maximum:", np.max(salaries))

# Output:

# Total: 265000
# Average: 44166.666666666664
# Minimum: 30000
# Maximum: 60000

# Ab filtering dekho.

# Agar humein ₹40,000 se greater salary chahiye:

# print(salaries[salaries > 40000])

# Output:

# [45000 55000 60000]

# Aur agar humein count karna ho ki ₹40,000 
# se greater salary kitne employees ki hai:

# print(np.sum(salaries > 40000))

# Output:

# 3

# Yahan wahi pattern use ho raha hai jo Sales Data mein kiya tha:

# Condition → Filter / Count → Analysis

# Ab practice karte hain.

# ==========================================
# NumPy — Practical Employee Salaries
# ==========================================

# Q1. Create a NumPy array representing the salaries
# of 6 employees:
# [30000, 45000, 55000, 40000, 60000, 35000]
#
# Calculate and print:
# - Total salary
# - Average salary
# - Minimum salary
# - Maximum salary

# import numpy as np
# salary = np.array([30000, 45000, 55000, 40000, 60000, 35000])
# print("Total:", np.sum(salary))
# print("Average:", np.mean(salary))
# print("Minimum:", np.min(salary))
# print("Maximum:", np.max(salary))
#------------------------------------------

# Q2. Using the same salary data:
# [30000, 45000, 55000, 40000, 60000, 35000]
#
# Filter and print all salaries greater than 40000.

# import numpy as np
# salary = np.array([30000, 45000, 55000, 40000, 60000, 35000])
# result = salary[salary > 40000]
# print(result)
#---------------------------------------------------

# Q3. Using the same salary data:
# [30000, 45000, 55000, 40000, 60000, 35000]
#
# Calculate and print the number of employees
# whose salary is greater than 40000.

# import numpy as np
# salary = np.array([30000, 45000, 55000, 40000, 60000, 35000])
# result = salary > 40000
# print(result)
# print(np.sum(result))
#__________________________________________________________________________________________________

#==============================
# 3. Marks Data
#==============================

# Marks Data — Useful Analysis

# Is baar hum:

# Passing marks identify karenge
# Fail students ke marks nikalenge
# Average se above marks find karenge

# Example:

# import numpy as np

# marks = np.array([45, 67, 82, 39, 91, 55, 72])

# average = np.mean(marks)

# print("Average:", average)
# print("Above Average:", marks[marks > average])
# print("Fail Marks:", marks[marks < 50])

# Yahan naya concept hai:

# average = np.mean(marks)
# marks[marks > average]

# Matlab pehle calculation karo, phir calculated value ko condition mein use karo.

# Ye Data Analyst ke liye zyada useful hai.

# Ab iske sirf 3 practical questions karte hain, repeat wale nahi.

# Theek hai. Ab Marks Data mein wahi practical part karte hain jo naya hai.

# ==========================================
# NumPy — Practical Marks Analysis
# ==========================================

# Q1. Create a NumPy array:
# [45, 67, 82, 39, 91, 55, 72]
#
# Calculate the average marks.
# Then filter and print all marks
# that are greater than the average.

# import numpy as np
# marks = np.array([45, 67, 82, 39, 91, 55, 72])
# average = np.mean(marks)

# print(marks [marks > average])
#---------------------------------------

# Q2. Using the same marks data:
# [45, 67, 82, 39, 91, 55, 72]
#
# Filter and print all marks below 50.

# import numpy as np
# marks = np.array([45, 67, 82, 39, 91, 55, 72])
# result = marks [marks < 50]
# print(result)
#---------------------------------------------

# Q3. Using the same marks data:
# [45, 67, 82, 39, 91, 55, 72]
#
# Calculate the difference between:
# - Maximum marks
# - Minimum marks

# import numpy as np
# marks = np.array([45, 67, 82, 39, 91, 55, 72])
# print("Maximum:",np.max(marks))
# print("Minimum:",np.min(marks))
