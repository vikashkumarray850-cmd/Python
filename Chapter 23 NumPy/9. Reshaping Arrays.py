# ==============================
# CODE NUMBERING BY:-

# 12 TO 137 .reshape()
# 141 TO 244 flatten()
# 248 TO 313 .ravel()
# ==============================

# 9. Reshaping Array

#==============================
# 1. reshape()
#==============================

# reshape() ka simple meaning hai:

# Array ka shape change karna, bina values ko change kiye.

# Example:

# import numpy as np

# num = np.array([10, 20, 30, 40, 50, 60])

# print(num)

# Output:

# [10 20 30 40 50 60]

# Ye 1D array hai.

# Ab isko 2 × 3 banana hai:

# num2 = num.reshape(2, 3)

# print(num2)

# Output:

# [[10 20 30]
#  [40 50 60]]

# Pehle:

# 1D

# [10 20 30 40 50 60]

# Baad mein:

# 2D

# [10 20 30]
# [40 50 60]
# Important rule

# reshape(rows, columns)

# num.reshape(2, 3)

# means:

# 2 rows × 3 columns
# Lekin ek important condition ⚠️

# Total elements same rehne chahiye.

# Hamare array mein:

# 6 values

# Isliye ye possible hain:

# num.reshape(2, 3)  # 6 elements
# num.reshape(3, 2)  # 6 elements
# num.reshape(6, 1)  # 6 elements
# num.reshape(1, 6)  # 6 elements

# Lekin:

# num.reshape(2, 4)

# ❌ nahi chalega, kyunki 2 × 4 = 8, jabki array mein sirf 6 elements hain.

# Data Analyst mein kahan useful?

# Suppose data ek long 1D format mein hai:

# [10,20,30,40,50,60]

# Aur humein usko rows + columns wale structure mein convert karna hai:

# 10 20 30
# 40 50 60

# Tab .reshape() useful hota hai.

# Practice — .reshape()
# ==========================================
# NumPy — reshape() Practice
# ==========================================

# Q1. Create a NumPy array:
# [10, 20, 30, 40, 50, 60]
#
# Reshape the array into 2 rows and 3 columns.
# Print the result.

# import numpy as np
# num = np.array([10, 20, 30, 40, 50, 60])
# result = num.reshape(2, 3)
# print(result)
#----------------------------------------------

# Q2. Create a NumPy array:
# [100, 200, 300, 400, 500, 600]
#
# Reshape the array into 3 rows and 2 columns.
# Print the result.

# import numpy as np
# num = np.array([100, 200, 300, 400, 500, 600])
# result = num.reshape(3,2)
# print(result)
#------------------------------------------------

# Q3. Create a NumPy array:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
# Reshape the array into 3 rows and 4 columns.
# Print the result.

# import numpy as np
# num = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# result = num.reshape(3, 4)
# print(result)
#____________________________________________________________________________________________________

#==============================
# 2. flatten() 
#==============================

# .flatten() kya karta hai?

# flatten() ek 2D array ko 1D array mein convert karta hai.

# Example:

# import numpy as np

# num = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# result = num.flatten()

# print(result)

# Output:

# [10 20 30 40 50 60]

# Pehle:

# [[10 20 30]
#  [40 50 60]]

# Ye 2D tha.

# flatten() ke baad:

# [10 20 30 40 50 60]

# Ye 1D ho gaya.

# Simple difference
# reshape()  → shape change karta hai
# flatten()  → array ko 1D bana deta hai

# Example:

# num.reshape(3, 2)

# → 1D se 2D

# num.flatten()

# → 2D se 1D

# Practice — .flatten()
# ==========================================
# NumPy — flatten() Practice
# ==========================================

# Q1. Create this 2D NumPy array:
# [[10, 20, 30],
#  [40, 50, 60]]
#
# Convert it into a 1D array using flatten().
# Print the result.

# import numpy as np
# num = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])
# result = num.flatten()
# print(result)
#-----------------------------------------

# Q2. Create this 2D NumPy array:
# [[100, 200],
#  [300, 400],
#  [500, 600]]
#
# Convert it into a 1D array using flatten().
# Print the result.

# import numpy as np
# num = np.array([
#     [100, 200],
#     [300, 400],
#     [500, 600]
# ])
# result = num.flatten()
# print(result)
#------------------------------------

# Q3. Create this 2D NumPy array:
# [[1, 2, 3, 4],
#  [5, 6, 7, 8]]
#
# Convert it into a 1D array using flatten().
# Print the result.

# import numpy as np
# num = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]
# ])
# result = num.flatten()
# print(result)
#_______________________________________________________________________________________________________

#==============================
# 3. ravel()
#==============================

# .ravel() bhi 2D array ko 1D array mein convert karta hai.

# Example:

# import numpy as np

# num = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# result = num.ravel()

# print(result)

# Output:

# [10 20 30 40 50 60]
# flatten() vs ravel()

# Dono ka basic output same hota hai:

# 2D
# [[10 20 30]
#  [40 50 60]]

#        ↓

# 1D
# [10 20 30 40 50 60]

# Main difference:

# flatten() → generally new copy banata hai.
# ravel() → possible ho to original array ka view return karta hai.

# Data Analyst ke perspective se abhi itna yaad rakhna enough hai:

# flatten() → 2D → 1D
# ravel()   → 2D → 1D
# Section 9 status
# 1. reshape()  ✅
# 2. flatten()  ✅
# 3. ravel()    ⏳  ← current

# ravel() ka ek simple practice karte hain:

# Create this 2D NumPy array:
# [[10, 20],
#  [30, 40],
#  [50, 60]]
#
# Convert it into a 1D array using ravel().
# Print the result.

# import numpy as np
# num = np.array([
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ])
# result = num.ravel()
# print(result)

