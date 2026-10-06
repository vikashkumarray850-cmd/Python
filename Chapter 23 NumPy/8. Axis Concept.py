# =======================================================
# CODE NUMBERING BY:-

# 11 TO 111 axis=0
# 115 TO 202 axis=1
# 206 TO 276 Row-wise Calculation vs Column-wise Calculation
# ==========================================================

#8. AXIS CONCEPT
#==============================
# 1. axis=0
#==============================

# Data Analyst ke liye axis bahut important hai, 
# especially jab 2D arrays par calculation karni hoti hai.

# Hum isko slowly samjhenge.

# Sabse pehle: Axis kya hota hai?

# 2D array ko dekho:

# numbers = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# Ismein:

#         Column
#         ↓   ↓   ↓
#        10  20  30
#        40  50  60
#        70  80  90
# axis=0

# axis=0 ka matlab columns ke direction mein calculation.

# Example:

# print(np.sum(numbers, axis=0))

# Calculation:

# Column 1 → 10 + 40 + 70 = 120
# Column 2 → 20 + 50 + 80 = 150
# Column 3 → 30 + 60 + 90 = 180

# Output:

# [120 150 180]
# Simple rule
# axis=0 → columns ke according
# axis=1 → rows ke according

# ⚠️ Lekin ek important point: axis=0 ko yaad karte waqt
#  "columns calculate hote hain" samjho; direction technically 
#  rows ko collapse karti hai.

# Abhi axis=1 nahi karenge. Pehle axis=0 ko properly practice karenge.

# Practice — axis=0
# ==========================================
# NumPy — axis=0 Practice
# ==========================================

# Q1. Create this 2D NumPy array:
# [[10, 20, 30],
#  [40, 50, 60],
#  [70, 80, 90]]
#
# Find the sum of each column using np.sum() with axis=0.

# import numpy as np
# num = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])
# print(np.sum(num, axis=0))
#----------------------------------

# Q2. Create this 2D NumPy array:
# [[5, 10],
#  [15, 20],
#  [25, 30]]
#
# Find the mean of each column using np.mean() with axis=0.

# import numpy as np
# num = np.array([
#     [5, 10],
#     [15, 20],
#     [25, 30]
# ])
# print(np.mean(num, axis=0))
#------------------------------------------

# Q3. Create this 2D NumPy array:
# [[100, 200, 300],
#  [50, 150, 250]]
#
# Find the maximum value from each column using np.max() with axis=0.

# import numpy as np
# num = np.array([
#     [100, 200, 300],
#     [50, 150, 250]
# ])
# print(np.max(num, axis=0))
#_________________________________________________________________________________________--

#==============================
# 2. axis=1
#==============================

# axis=1 ka matlab hai row-wise calculation.

# Same array:

# numbers = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# Agar:

# np.sum(numbers, axis=1)

# toh har row ka sum milega:

# Row 1 → 10 + 20 + 30 = 60
# Row 2 → 40 + 50 + 60 = 150
# Row 3 → 70 + 80 + 90 = 240

# Output:

# [ 60 150 240]
# Yaad rakho
# axis=0 → Column-wise
# axis=1 → Row-wise

# Aur axis=1 bhi sirf sum() ke liye nahi hai:

# np.mean(numbers, axis=1)
# np.min(numbers, axis=1)
# np.max(numbers, axis=1)
# np.std(numbers, axis=1)
# np.median(numbers, axis=1)

# Sab use kar sakte ho.

# Practice — axis=1
# ==========================================
# NumPy — axis=1 Practice
# ==========================================

# Q1. Create this 2D NumPy array:
# [[10, 20, 30],
#  [40, 50, 60],
#  [70, 80, 90]]
#
# Find the sum of each row using np.sum() with axis=1.
# import numpy as np
# num = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])
# print(np.sum(num, axis=1))
#--------------------------------------

# Q2. Create this 2D NumPy array:
# [[10, 20],
#  [30, 40],
#  [50, 60]]
#
# Find the mean of each row using np.mean() with axis=1.

# import numpy as np
# num = np.array([
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ])
# print(np.mean(num, axis=1))
#--------------------------------

# Q3. Create this 2D NumPy array:
# [[100, 200, 50],
#  [400, 150, 300]]
#
# Find the maximum value from each row using np.max() with axis=1.

# import numpy as np
# num = np.array([
#     [100, 200, 50],
#     [400, 150, 300]
# ])
# print(np.max(num, axis=1))
#________________________________________________________________________________________________

#==================================================
# 3 Row-wise Calculation vs Column-wise Calculation
#==================================================

# Q1. Create this 2D NumPy array:
# [[10, 20, 30],
#  [40, 50, 60],
#  [70, 80, 90]]
#
# Find the sum of each row.
#
# Find the sum of each column.

# import numpy as np

# num = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# # Sum of each row
# print(np.sum(num, axis=1))

# # Sum of each column
# print(np.sum(num, axis=0))
#-------------------------------------

# Q2. Create this 2D NumPy array:
# [[10, 20],
#  [30, 40],
#  [50, 60]]
#
# Find the mean of each row.
#
# Find the mean of each column.

# import numpy as np

# num = np.array([
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ])

# # Mean of each row
# print(np.mean(num, axis=1))

# # Mean of each column
# print(np.mean(num, axis=0))
#----------------------------------

# Q3. Create this 2D NumPy array:
# [[100, 50, 200],
#  [300, 150, 250]]
#
# Find the minimum value from each row.
#
# Find the maximum value from each column.

import numpy as np

num = np.array([
    [100, 50, 200],
    [300, 150, 250]
])

# Minimum value from each row
print(np.min(num, axis=1))

# Maximum value from each column
print(np.max(num, axis=0))