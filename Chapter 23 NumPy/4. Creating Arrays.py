# ==========================================
# CODE NUMBERING BY:-

# 15 TO 91 np.zeros()
# 93 TO 158 np.ones()
# 162 TO 234 np.full() 
# 238 TO 340 np.arange()
# 342 TO 439 np.linspace()
# ==========================================

# ==========================================
# NumPy — Creating Arrays: np.zeros()
# ==========================================

# 1.  np.zeros()
#____________________________

# np.zeros() ka use karke hum 0 se filled NumPy array bana sakte hain.

# 1D Array
# import numpy as np

# numbers = np.zeros(5)

# print(numbers)

# Output:

# [0. 0. 0. 0. 0.]

# Yahan 5 ka matlab hai 5 zeros.

# 2D Array

# Agar hume 2 rows aur 3 columns chahiye:

# numbers = np.zeros((2, 3))

# print(numbers)

# Output:

# [[0. 0. 0.]
#  [0. 0. 0.]]

# Yahan:

# 2 → rows
# 3 → columns
# Important difference
# np.zeros(5)

# → 5 zeros ka 1D array

# np.zeros((2, 3))

# → 2 rows × 3 columns ka 2D array

# Data Analyst mein np.zeros() ka use kabhi-kabhi 
# initial/empty numerical structure create karne ke liye hota hai.

# Practice
# ==========================================
# NumPy — Creating Arrays: np.zeros()
# ==========================================

# Q1. Create a 1D NumPy array containing 5 zeros.
# Print the array.

# import numpy as np
# numbers = np.zeros(5)
# print(numbers)
#_------------------------------------

# Q2. Create a 2D NumPy array with 3 rows and 4 columns.
# Fill all elements with zeros.
# Print the array.

# import numpy as np
# numbers = np.zeros((3,4))
# print(numbers)
#------------------------------------

# Q3. Create a 2D NumPy array with 2 rows and 5 columns.
# Fill all elements with zeros.
# Print the array.

# import numpy as np
# numbers = np.zeros((2, 5))
# print(numbers)
#__________________________________________________________________________________________________

# ==========================================
# 2.  np.ones()
# ==========================================

# 1.  np.ones()
#____________________________

# np.ones() bilkul np.zeros() jaisa hai, bas difference 
# ye hai ki saare elements 1 hote hain.

# Example:

# import numpy as np

# numbers = np.ones(5)

# print(numbers)

# Output:

# [1. 1. 1. 1. 1.]

# 2D:

# numbers = np.ones((2, 3))

# print(numbers)

# Output:

# [[1. 1. 1.]
#  [1. 1. 1.]]

# Yaani:

# np.zeros() → 0
# np.ones()  → 1

# ==========================================
# NumPy — Creating Arrays: np.ones()
# ==========================================

# Q1. Create a 1D NumPy array containing 6 ones.
# Print the array.

# import numpy as np
# numbers = np.ones(6)
# print(numbers)
#---------------------------------------

# Q2. Create a 2D NumPy array with 3 rows and 3 columns.
# Fill all elements with ones.
# Print the array.

# import numpy as np
# numbers = np.ones((3, 3))
# print(numbers)
#-------------------------------------

# Q3. Create a 2D NumPy array with 2 rows and 4 columns.
# Fill all elements with ones.
# Print the array.

# import numpy as np
# numbers = np.ones((2,4))
# print(numbers)

#____________________________________________________________________________________________

# ==========================================
# 3.  np.full()
# ==========================================
# np.full()

# np.full() ka use karke hum array ke har element 
# mein apni choice ki same value fill kar sakte hain.

# Example:

# import numpy as np

# numbers = np.full(5, 7)

# print(numbers)

# Output:

# [7 7 7 7 7]

# Yahan:

# 5 → total elements
# 7 → har element ki value

# 2D example:

# numbers = np.full((2, 3), 10)

# print(numbers)

# Output:

# [[10 10 10]
#  [10 10 10]]

# Simple difference:

# np.zeros() → sab jagah 0
# np.ones()  → sab jagah 1
# np.full()  → sab jagah apni chosen value

# Ab practice:

# ==========================================
# NumPy — Creating Arrays: np.full()
# ==========================================

# Q1. Create a 1D NumPy array with 5 elements.
# Fill every element with the value 7.
# Print the array.

# import numpy as np
# numbers = np.full(5,7)
# print(numbers)
#-----------------------------------------

# Q2. Create a 2D NumPy array with 2 rows and 3 columns.
# Fill every element with the value 100.
# Print the array.

# import numpy as np
# numbers = np.full((2, 3), 100)
# print(numbers)
#------------------------------------

# Q3. Create a 2D NumPy array with 3 rows and 4 columns.
# Fill every element with the value 50.
# Print the array.

# import numpy as np
# numbers = np.full((3, 4), 50)
# print(numbers)

#_______________________________________________________________________________-

# ==========================================
# 4. np.arange()
# ==========================================

# np.arange() ka use karke hum sequence of numbers 
# ka NumPy array bana sakte hain.

# Basic syntax:

# np.arange(start, stop, step)
# 1. Sirf stop
# import numpy as np

# numbers = np.arange(5)

# print(numbers)

# Output:

# [0 1 2 3 4]

# Yahan 5 include nahi hota.

# 2. start aur stop
# numbers = np.arange(2, 7)

# print(numbers)

# Output:

# [2 3 4 5 6]

# Yaani:

# start = 2
# stop  = 7

# 7 include nahi hoga.

# 3. step
# numbers = np.arange(2, 11, 2)

# print(numbers)

# Output:

# [ 2  4  6  8 10]

# Yahan:

# start = 2
# stop  = 11
# step  = 2

# Har baar number 2 se increase ho raha hai.

# Important rule
# np.arange(start, stop, step)

# start → include
# stop  → exclude
# step  → kitna gap

# Example:

# np.arange(10, 20, 3)

# Output:

# [10 13 16 19]

# Ab 3 practice questions:

# ==========================================
# NumPy — Creating Arrays: np.arange()
# ==========================================

# Q1. Create a NumPy array containing numbers
# from 0 to 9 using np.arange().
# Print the array.

# import numpy as np
# numbers = np.arange(0,9)
# print(numbers)
#-------------------------------------

# Q2. Create a NumPy array containing numbers
# from 5 to 15 using np.arange().
# Print the array.

# import numpy as np
# numbers = np.arange(5,15)
# print(numbers)
#----------------------------------

# Q3. Create a NumPy array starting from 10
# and ending before 30, with a step of 5.
# Print the array.

# import numpy as np
# numbers = np.arange(10, 30, 5)
# print(numbers)
#__________________________________________________________________________________________

# ==========================================
# 5. np.linspace()
# ==========================================

# np.linspace() ka use do numbers ke beech evenly spaced 
# numbers generate karne ke liye hota hai.

# Basic syntax:

# np.linspace(start, stop, num)

# Yahan:

# start → starting value
# stop → ending value
# num → total kitni values chahiye
# Simple example
# import numpy as np

# numbers = np.linspace(0, 10, 5)

# print(numbers)

# Output:

# [ 0.   2.5  5.   7.5 10. ]

# Dekho:

# 0 → 2.5 → 5 → 7.5 → 10

# Total 5 values hain aur values ke beech gap equal hai.

# arange() vs linspace()

# Ye difference important hai:

# np.arange(0, 10, 2)

# Yahan hum step dete hain:

# 0  2  4  6  8

# Lekin:

# np.linspace(0, 10, 5)

# Yahan hum total number of values dete hain:

# 0  2.5  5  7.5  10

# Simple rule:

# arange()   → step kitna?
# linspace() → total values kitni?
# Ek aur example
# numbers = np.linspace(10, 20, 3)

# print(numbers)

# Output:

# [10. 15. 20.]

# 3 values hain aur spacing equal hai.

# Ab np.linspace() ke 3 practice questions:

# ==========================================
# NumPy — Creating Arrays: np.linspace()
# ==========================================

# Q1. Create a NumPy array with 5 evenly spaced
# values between 0 and 20.
# Print the array.

# import numpy as np
# numbers = np.linspace(0, 20, 5)
# print(numbers)
#----------------------------------------


# Q2. Create a NumPy array with 6 evenly spaced
# values between 10 and 30.
# Print the array.

# import numpy as np
# numbers = np.linspace(10, 30, 6)
# print(numbers)
#------------------------------------------------

# Q3. Create a NumPy array with 4 evenly spaced
# values between 5 and 20.
# Print the array.

# import numpy as np
# numbers = np.linspace(5, 20, 4)
# print(numbers)