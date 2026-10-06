# ==========================================
# CODE NUMBERING BY:-

# 13 TO 134 Addition
# 137 TO 248 Subtraction
# 252 TO 370 Multiplication
# 374 TO 490 Division
# 494 TO 605 Power
# 609 TO 766 Comparison Operations
# ==========================================

# ==========================================
# 1. Addition
# ==========================================

# NumPy arrays par hum directly mathematical operations kar sakte hain.

# 1. Array Addition

# Agar do NumPy arrays ka same shape hai, to hum unhe directly add kar sakte hain.

# Example:

# import numpy as np

# a = np.array([10, 20, 30])
# b = np.array([1, 2, 3])

# print(a + b)

# Output:

# [11 22 33]

# Yahan NumPy same position ke elements ko add karta hai:

# a = [10  20  30]
# b = [ 1   2   3]
#      ↓   ↓   ↓
#      11  22  33

# Mathematically:

# 10 + 1 = 11
# 20 + 2 = 22
# 30 + 3 = 33
# 2D Array mein bhi same rule
# import numpy as np

# a = np.array([
#     [10, 20],
#     [30, 40]
# ])

# b = np.array([
#     [1, 2],
#     [3, 4]
# ])

# print(a + b)

# Output:

# [[11 22]
#  [33 44]]

# Yaani:

# 10 + 1 = 11
# 20 + 2 = 22
# 30 + 3 = 33
# 40 + 4 = 44
# Important

# NumPy mein:

# a + b

# ka matlab generally element-by-element addition hai.

# Ye normal Python lists se different behavior de sakta hai.

# Practice
# ==========================================
# NumPy — Array Addition
# ==========================================

# Q1. Create two 1D NumPy arrays:
# [10, 20, 30]
# [1, 2, 3]
# Add the two arrays and print the result.

# import numpy as np
# a = np.array([ 10, 20, 30])
# b = np.array([1, 2, 3])

# print(a + b)
#-------------------------------

# Q2. Create two 1D NumPy arrays:
# [100, 200, 300]
# [10, 20, 30]
# Add the two arrays and print the result.

# import numpy as np
# a = np.array([ 100, 200, 300])
# b = np.array([10, 20, 30])

# result = a + b

# print(result)
#---------------------------------------

# Q3. Create two 2D NumPy arrays:
# [[10, 20],
#  [30, 40]]
#
# [[5, 10],
#  [15, 20]]
#
# Add the two arrays and print the result.

# import numpy as np
# a = np.array([
#     [10, 20],
#     [30, 40]
# ])
# b = np.array([
#     [5, 10],
#     [15, 20]
# ])
# result = a + b
# print(result)
#___________________________________________________________________________________________

#==============================
# 2. Array Subtraction
#==============================
# Addition ki tarah NumPy arrays mein subtraction 
# bhi element-by-element hota hai.

# Example:

# import numpy as np

# a = np.array([10, 20, 30])
# b = np.array([1, 2, 3])

# print(a - b)

# Output:

# [ 9 18 27]

# Kaise?

# a = [10  20  30]
# b = [ 1   2   3]
#      ↓   ↓   ↓
#       9  18  27

# Matlab:

# 10 - 1 = 9
# 20 - 2 = 18
# 30 - 3 = 27
# 2D Array

# Same concept 2D mein bhi:

# import numpy as np

# a = np.array([
#     [10, 20],
#     [30, 40]
# ])

# b = np.array([
#     [1, 2],
#     [3, 4]
# ])

# print(a - b)

# Output:

# [[ 9 18]
#  [27 36]]

# Yaani har corresponding position par subtraction hota hai.

# Simple rule
# a + b   # Addition
# a - b   # Subtraction

# Dono mein same position ke elements ke saath operation hota hai.

# Practice
# ==========================================
# NumPy — Array Subtraction
# ==========================================

# Q1. Create two 1D NumPy arrays:
# [20, 40, 60]
# [5, 10, 15]
# Subtract the second array from the first array.

# import numpy as np
# a = np.array([20, 40, 60])
# b = np.array([5, 10, 15])

# print(a-b)
#-----------------------------

# Q2. Create two 1D NumPy arrays:
# [100, 200, 300]
# [10, 20, 30]
# Subtract the second array from the first array.

# import numpy as np
# a = np.array([ 100, 200, 300])
# b = np.array([10, 20, 30])

# result = a-b

# print(result)
#--------------------------------------

# Q3. Create two 2D NumPy arrays:
# [[50, 60],
#  [70, 80]]
#
# [[5, 10],
#  [15, 20]]
#
# Subtract the second array from the first array.

# import numpy as np
# a = np.array([
#     [50, 60],
#     [70, 80]
# ])
# b = np.array([
#     [5, 10],
#     [15, 20]
# ])

# print(a-b)
#________________________________________________________________________________________________________

#==============================
# 3. Array Multiplication
#==============================

# NumPy mein jab hum do arrays ko * se multiply karte hain,
#  to multiplication element-by-element hota hai.

# Example:

# import numpy as np

# a = np.array([10, 20, 30])
# b = np.array([2, 3, 4])

# print(a * b)

# Output:

# [20 60 120]

# Kaise?

# a = [10  20  30]
# b = [ 2   3   4]
#      ↓   ↓   ↓
#      20  60  120

# Matlab:

# 10 × 2 = 20
# 20 × 3 = 60
# 30 × 4 = 120
# 2D Array mein bhi same
# import numpy as np

# a = np.array([
#     [10, 20],
#     [30, 40]
# ])

# b = np.array([
#     [2, 3],
#     [4, 5]
# ])

# print(a * b)

# Output:

# [[ 20  60]
#  [120 200]]

# Yahan bhi same position ke elements multiply hue:

# 10 × 2 = 20
# 20 × 3 = 60
# 30 × 4 = 120
# 40 × 5 = 200
# Important: * aur Matrix Multiplication alag hain

# Abhi hum:

# a * b

# seekh rahe hain → element-by-element multiplication.

# Matrix multiplication (@) abhi nahi karna hai; woh NumPy 
# ke Data Analyst roadmap mein required topic nahi hai.

# Practice
# ==========================================
# NumPy — Array Multiplication
# ==========================================

# Q1. Create two 1D NumPy arrays:
# [2, 4, 6]
# [10, 20, 30]
# Multiply the two arrays and print the result.

# import numpy as np
# a = np.array([2, 4, 6])
# b = np.array([10, 20, 30])
# result = a * b

# print(result)
#--------------------------------

# Q2. Create two 1D NumPy arrays:
# [5, 10, 15]
# [2, 3, 4]
# Multiply the two arrays and print the result.

# import numpy as np
# x = np.array([5, 10, 15])
# y = np.array([2, 3, 4])
# result = x * y

# print(result)
#--------------------------------

# Q3. Create two 2D NumPy arrays:
# [[10, 20],
#  [30, 40]]
#
# [[2, 3],
#  [4, 5]]
#
# Multiply the two arrays and print the result.

# import numpy as np
# x = np.array([
#     [10, 20],
#     [30, 40]
# ])
# y = np.array([
#     [2, 3],
#     [4, 5]
# ])
# result = x * y
# print(result)
#______________________________________________________________________________________________________

#==============================
# 4. Array Division
#==============================

# NumPy mein / use karke do arrays ko divide kar sakte hain.

# Yahan bhi operation element-by-element hota hai.


# Example:

# import numpy as np

# a = np.array([10, 20, 30])
# b = np.array([2, 4, 5])

# print(a / b)

# Output:

# [5. 5. 6.]

# Kaise?

# 10 ÷ 2 = 5
# 20 ÷ 4 = 5
# 30 ÷ 5 = 6

# NumPy result ko generally float mein deta hai:

# [5. 5. 6.]
# 2D Array
# import numpy as np

# a = np.array([
#     [10, 20],
#     [30, 40]
# ])

# b = np.array([
#     [2, 4],
#     [5, 8]
# ])

# print(a / b)

# Output:

# [[5.  5. ]
#  [6.  5. ]]

# Kyunki:

# 10 ÷ 2 = 5
# 20 ÷ 4 = 5
# 30 ÷ 5 = 6
# 40 ÷ 8 = 5
# Simple rule
# a + b   # Addition
# a - b   # Subtraction
# a * b   # Multiplication
# a / b   # Division

# Sabhi operations mein corresponding elements par operation hota hai.

# Practice
# ==========================================
# NumPy — Array Division
# ==========================================

# Q1. Create two 1D NumPy arrays:
# [20, 40, 60]
# [2, 4, 5]
# Divide the first array by the second array.

# import numpy as np
# a = np.array([20, 40, 60])
# b = np.array([2, 4, 5])
# result = a / b

# print(result)
#-------------------------------

# Q2. Create two 1D NumPy arrays:
# [100, 200, 300]
# [10, 20, 50]
# Divide the first array by the second array.

# import numpy as np
# x = np.array([100, 200, 300])
# y = np.array([10, 20, 50])
# result = x / y

# print(result)
#-----------------------------

# Q3. Create two 2D NumPy arrays:
# [[20, 40],
#  [60, 80]]
#
# [[2, 4],
#  [3, 8]]
#
# Divide the first array by the second array.

# import numpy as np

# a = np.array([
#     [20, 40],
#     [60, 80]
# ])

# b = np.array([
#     [2, 4],
#     [3, 8]
# ])

# print(a / b)
#______________________________________________________________________________________________

# ==========================================
# 5. Power Operation
# ==========================================

# NumPy array mein ** ka use power ke liye hota hai.

# Example:

# import numpy as np

# numbers = np.array([2, 3, 4])

# print(numbers ** 2)

# Output:

# [ 4  9 16]

# Kyunki:

# 2² = 4
# 3² = 9
# 4² = 16

# Yahan bhi operation element-by-element hai.

# Pehle 2² = 4

# 2² ka matlab hai:

# 2 ko 2 baar multiply karo

# 2 × 2 = 4

# Isliye:

# 2² = 4

# Different powers
# numbers = np.array([2, 3, 4])

# print(numbers ** 3)

# Output:

# [ 8 27 64]

# Kyunki:

# 2³ = 8
# 3³ = 27
# 4³ = 64
# Do arrays ke saath bhi
# import numpy as np

# a = np.array([2, 3, 4])
# b = np.array([2, 2, 3])

# print(a ** b)

# Output:

# [ 4  9 64]

# Kyunki:

# 2² = 4
# 3² = 9
# 4³ = 64
# Simple rule
# a + b   # Addition
# a - b   # Subtraction
# a * b   # Multiplication
# a / b   # Division
# a ** b  # Power

# Ye sab NumPy mein element-by-element operations hain.

# Practice
# ==========================================
# NumPy — Power Operation
# ==========================================

# Q1. Create a NumPy array:
# [2, 3, 4]
# Calculate the square of every element.

# import numpy as np
# number = np.array([2, 3, 4])
# print(number ** 2)
#----------------------------

# Q2. Create a NumPy array:
# [2, 3, 5]
# Calculate the cube of every element.

# import numpy as np
# number = np.array([2, 3, 4])
# print(number ** 3)
#------------------------------------------

# Q3. Create two NumPy arrays:
# [2, 3, 4]
# [3, 2, 2]
# Raise each element of the first array to the corresponding power
# from the second array.

# import numpy as np

# a = np.array([2, 3, 4])
# b = np.array([3, 2, 2])

# print(a ** b)
#______________________________________________________________________________________________________-

# ==========================================
# 6. Comparison Operations
# ==========================================

# 1. > Greater Than

# > ka matlab hai bada hai.

# import numpy as np

# numbers = np.array([10, 20, 30, 40])

# print(numbers > 25)

# Output:

# [False False  True  True]

# Kyun?

# 10 > 25  → False
# 20 > 25  → False
# 30 > 25  → True
# 40 > 25  → True

# NumPy har element ko individually check karta hai.

# 2. < Less Than

# < ka matlab hai chhota hai.

# numbers = np.array([10, 20, 30, 40])

# print(numbers < 25)

# Output:

# [ True  True False False]
# 3. >= Greater Than or Equal To

# Matlab bada ya barabar.

# numbers = np.array([10, 20, 30, 40])

# print(numbers >= 30)

# Output:

# [False False  True  True]

# Yahan 30 >= 30 bhi True hai, kyunki equal allowed hai.

# 4. <= Less Than or Equal To
# numbers = np.array([10, 20, 30, 40])

# print(numbers <= 20)

# Output:

# [ True  True False False]
# 5. == Equal To

# == check karta hai ki value equal hai ya nahi.

# numbers = np.array([10, 20, 30, 40])

# print(numbers == 20)

# Output:

# [False  True False False]
# 6. != Not Equal To

# != ka matlab equal nahi hai.

# numbers = np.array([10, 20, 30, 40])

# print(numbers != 20)

# Output:

# [ True False  True  True]
# Data Analyst mein iska use

# Ye bahut important hai, kyunki baad mein isi concept se hum data filtering karenge.

# Example:

# sales = np.array([100, 500, 200, 800, 300])

# print(sales > 300)

# Output:

# [False  True False  True False]

# Yaani hum identify kar sakte hain ki kaunse values 300 se greater hain.

# ==========================================
# NumPy — Comparison Operations
# ==========================================

# Q1. Create a NumPy array:
# [10, 20, 30, 40, 50]
# Check which elements are greater than 25 using >.

# import numpy as np
# number = np.array([10, 20, 30, 40, 50])
# print(number > 25)
#----------------------------------------

# Q2. Create a NumPy array:
# [5, 10, 15, 20, 25]
# Check which elements are less than 15 using <.

# import numpy as np
# numbers = np.array([5, 10, 15, 20, 25])

# print(numbers < 15)
#---------------------------------------------

# Q3. Create a NumPy array:
# [10, 20, 30, 40, 50]
# Check which elements are greater than or equal to 30 using >=.

# import numpy as np
# numbers = np.array([10, 20, 30, 40, 50])

# print(numbers >= 30)
#----------------------------------------------

# Q4. Create a NumPy array:
# [5, 10, 15, 20, 25]
# Check which elements are less than or equal to 15 using <=.

import numpy as np
numbers = np.array([5, 10, 15, 20, 25])

print(numbers <= 15)
#----------------------------------

# Q5. Create a NumPy array:
# [10, 20, 30, 40, 50]
# Check which element is equal to 30 using ==.

import numpy as np
numbers = np.array([10, 20, 30, 40,50])

print(numbers == 30)
#-----------------------------------

# Q6. Create a NumPy array:
# [100, 200, 300, 400, 500]
# Check which elements are not equal to 300 using !=.

import numpy as np
numbers = np.array([10, 20, 30, 40])

print(numbers != 300)
