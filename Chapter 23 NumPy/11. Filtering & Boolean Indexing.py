# ==============================
# CODE NUMBERING BY:-

# 10 TO 97  Conditions on Arrays
# 100 TO 146 Boolean Arrays
# 150 TO 262 Filtering Data
# ==============================

#==============================
# # 1 Conditions on Arrays
#==============================

# Pehle humne comparison operations padhe the:

# >   <   >=   <=   ==   !=

# NumPy array par condition lagane se hume True / False ka array milta hai.

# Example:

# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# result = numbers > 30

# print(result)

# Output:

# [False False False  True  True]

# Kyun?

# 10 > 30  → False
# 20 > 30  → False
# 30 > 30  → False
# 40 > 30  → True
# 50 > 30  → True

# Yaani NumPy har element ko separately check karta hai.

# Data Analyst example

# Maan lo employee salaries hain:

# salary = np.array([25000, 35000, 45000, 55000, 65000])

# print(salary > 40000)

# Output:

# [False False  True  True  True]

# Abhi hum sirf True/False condition bana rahe hain.

# Next step mein isi Boolean result ka use karke actual values filter karenge.

# Practice — .1
# ==========================================
# NumPy — Conditions on Arrays Practice
# ==========================================

# Q1. Create a NumPy array:
# [10, 25, 40, 55, 70]
#
# Check which values are greater than 40.
# Print the Boolean result.

# import numpy as np
# num = np.array([10, 25, 40, 55, 70])
# result = num > 40
# print(result)
#----------------------------------

# Q2. Create a NumPy array:
# [15, 30, 45, 60, 75]
#
# Check which values are less than or equal to 45.
# Print the Boolean result.

# import numpy as np
# num = np.array([15, 30, 45, 60, 75])
# result = num <= 45
# print(result)
#------------------------------

# Q3. Create a NumPy array:
# [100, 200, 300, 400, 500]
#
# Check which values are equal to 300.
# Print the Boolean result.

# import numpy as np
# num = np.array([100, 200, 300, 400, 500])
# result = num == 300
# print(result)
#_____________________________________________________________________________________________

#==============================
# 2. Boolean Arrays
#==============================

# Actually tumne jo abhi outputs dekhe:

# [False False True False False]

# yehi Boolean Array hai.

# Boolean Array mein har element sirf:

# True

# ya

# False

# hota hai.

# Example:

# import numpy as np

# marks = np.array([35, 55, 70, 25, 90])

# result = marks >= 50

# print(result)

# Output:

# [False  True  True False  True]

# Matlab:

# 35 >= 50 → False
# 55 >= 50 → True
# 70 >= 50 → True
# 25 >= 50 → False
# 90 >= 50 → True

# Important: Boolean array khud actual values nahi deta; 
# ye batata hai ki kaunsi position condition satisfy karti hai.

# Aur isi Boolean array ko hum next step mein use karke actual data filter karenge.
# यही Data Analysis mein bahut useful hai.
#______________________________________________________________________________________________________

#==============================
# Filtering Data
#==============================

# Filtering Data

# Abhi tak humne condition lagakar True/False dekha:

# marks = np.array([35, 55, 70, 25, 90])

# print(marks >= 50)

# Output:

# [False  True  True False  True]

# Lekin Data Analysis mein hume True/False nahi, 
# actual values chahiye jo condition satisfy karti hain.

# Uske liye array ke andar condition directly laga sakte hain:

# import numpy as np

# marks = np.array([35, 55, 70, 25, 90])

# result = marks[marks >= 50]

# print(result)

# Output:

# [55 70 90]
# Isko step-by-step samjho
# marks[marks >= 50]

# Outer:

# marks[ ... ]

# → actual values select karega.

# Inner:

# marks >= 50

# → Boolean condition banayega:

# [False True True False True]

# Phir NumPy sirf True wali values rakhta hai:

# 55
# 70
# 90
# Data Analyst example

# Maan lo salaries:

# salary = np.array([25000, 35000, 45000, 55000, 65000])

# high_salary = salary[salary > 40000]

# print(high_salary)

# Output:

# [45000 55000 65000]

# Yaani humne ₹40,000 se zyada salary wale employees filter kar liye.

# Simple rule
# Condition:
# salary > 40000

# Filtering:
# salary[salary > 40000]

# Ab practice karo:

# ==========================================
# NumPy — Filtering Data Practice
# ==========================================

# Q1. Create a NumPy array:
# [10, 25, 40, 55, 70]
#
# Filter and print only the values greater than 40.

# import numpy as np
# num = np.array([10, 25, 40, 55, 70])
# result = num[num > 40]
# print(result)
#---------------------------------------

# Q2. Create a NumPy array:
# [15, 30, 45, 60, 75]
#
# Filter and print only the values less than or equal to 45.

# import numpy as np
# num = np.array([15, 30, 45, 60, 75])
# result = num[num <= 45]
# print(result)
#-----------------------------------------

# Q3. Create a NumPy array:
# [100, 200, 300, 400, 500]
#
# Filter and print only the value equal to 300.

import numpy as np
num = np.array([100, 200, 300, 400, 500])
result = num[num == 300]
print(result)