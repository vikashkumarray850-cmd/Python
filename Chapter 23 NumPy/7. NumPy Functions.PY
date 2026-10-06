# ==========================================
# CODE NUMBERING BY:-

# 12 TO 86 np.sum()
# 89 TO 146 np.mean()
# 150 TO 195 np.min()
# 199 TO 255 np.max()
# 259 TO 358 np.std()
# 362 TO 458 np.median()
# ==========================================

#==============================
# 1. np.sum()
#==============================

# np.sum() ka use array ke saare elements ka total nikalne ke liye hota hai.

# Example:

# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(np.sum(numbers))

# Output:

# 150

# Kyun?

# 10 + 20 + 30 + 40 + 50 = 150
# Data Analyst mein use

# Maan lo kisi company ki daily sales hain:

# sales = np.array([1000, 1500, 2000, 1200, 1800])

# print(np.sum(sales))

# Output:

# 7500

# Yaani total sales = 7500.

# Ek important difference

# sum() Python ka built-in function hai, jabki:

# np.sum()

# NumPy ka function hai.

# NumPy arrays ke saath hum np.sum() use karna seekhenge.

# Practice — np.sum()
# ==========================================
# NumPy — np.sum()
# ==========================================

# Q1. Create a NumPy array:
# [10, 20, 30, 40, 50]
# Find the total of all elements using np.sum().

# import numpy as np
# number = np.array([10, 20, 30, 40, 50])
# print(np.sum(number))
#--------------------------------

# Q2. Create a NumPy array:
# [100, 200, 150, 300, 250]
# Find the total sales using np.sum().

# import numpy as np
# number = np.array([100, 200, 150, 300, 250])
# print(np.sum(number))
#--------------------------------

# Q3. Create a NumPy array:
# [5, 10, 15, 20, 25]
# Find the total of all elements using np.sum().

# import numpy as np
# number = np.array([5, 10, 15, 20, 25])
# print(np.sum(number))
#___________________________________________________________________________________________________

#==============================
# 2. np.mean() [AVERAGE]
#==============================


# np.mean() ka use average nikalne ke liye hota hai.

# Example:

# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(np.mean(numbers))

# Output:

# 30.0

# Calculation:

# (10 + 20 + 30 + 40 + 50) / 5
# = 150 / 5
# = 30

# Data Analyst mein mean ka use average sales, average salary, 
# average marks, average price etc. nikalne mein hota hai.

# Practice — np.mean()
# ==========================================
# NumPy — np.mean() [AVERAGE]
# ==========================================

# Q1. Create a NumPy array:
# [10, 20, 30, 40, 50]
# Find the average using np.mean().

# import numpy as np
# number = np.array([10, 20, 30, 40, 50])
# print(np.mean(number))
#-------------------------------------

# Q2. Create a NumPy array:
# [100, 200, 300, 400]
# Find the average using np.mean().

# import numpy as np
# number = np.array([100, 200, 300, 400])
# print(np.mean(number))
#---------------------------------

# Q3. Create a NumPy array:
# [50, 60, 70, 80, 90]
# Find the average using np.mean().

# import numpy as np
# number = np.array([50, 60, 70, 80, 90])
# print(np.mean(number))
#______________________________________________________________________________________________

#==============================
# 3. np.min()
#==============================

# np.min() array ke andar ki sabse chhoti value nikalta hai.

# Example:

# numbers = np.array([10, 50, 20, 80, 30])

# print(np.min(numbers))

# Output:

# 10

# Matlab array mein minimum value = 10.

# ==========================================
# NumPy — np.min()
# ==========================================

# Q1. Create a NumPy array:
# [10, 25, 5, 40, 15]
# Find the minimum value using np.min().

# import numpy as np
# number = np.array([10, 25, 5, 40, 15])
# print(np.min(number))
#--------------------------------------

# Q2. Create a NumPy array:
# [100, 50, 200, 25, 150]
# Find the minimum value using np.min().

# import numpy as np
# number = np.array([100, 50, 200, 25, 150])
# print(np.min(number))
#-------------------------------------------

# Q3. Create a NumPy array:
# [45, 30, 60, 10, 90]
# Find the minimum value using np.min().

# import numpy as np
# number = np.array([45, 30, 60, 10, 90])
# print(np.min(number))
#_________________________________________________________________________________________________

#==============================
# 4. np.max()
#==============================

# np.max() ka use array mein se sabse badi value nikalne ke liye hota hai.

# Example:

# import numpy as np

# numbers = np.array([10, 50, 20, 80, 30])

# print(np.max(numbers))

# Output:

# 80

# Matlab array mein maximum value = 80.

# Simple difference:

# np.min() → sabse chhoti value
# np.max() → sabse badi value

# Data Analyst mein iska use, for example, highest sales, highest salary,
#  highest marks, maximum price find karne mein hota hai.

# Practice — np.max()
# ==========================================
# NumPy — np.max()
# ==========================================

# Q1. Create a NumPy array:
# [10, 25, 5, 40, 15]
# Find the maximum value using np.max().

# import numpy as np
# numbers = np.array([10, 25, 5, 40, 15])
# print(np.max(numbers))
#-------------------------------------

# Q2. Create a NumPy array:
# [100, 50, 200, 25, 150]
# Find the maximum value using np.max().

# import numpy as np
# numbers = np.array([100, 50, 200, 25, 150])
# print(np.max(numbers))
#--------------------------------------------

# Q3. Create a NumPy array:
# [45, 30, 60, 10, 90]
# Find the maximum value using np.max().

# import numpy as np
# numbers = np.array([45, 30, 60, 10, 90])
# print(np.max(numbers))
#_____________________________________________________________________________________________________

#=================================
# 5. np.std() [Standard Deviation]
#=================================

# std ka full form hai Standard Deviation.

# Simple language mein:

# np.std() batata hai ki values average (mean) ke around kitni spread out hain.

# Example:

# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(np.std(numbers))

# Output approximately:

# 14.142135623730951
# Is number ka matlab kya hai?

# Pehle humara mean:

# (10 + 20 + 30 + 40 + 50) / 5
# = 30

# Ab values mean 30 se kitni door hain:

# 10 → 30 se 20 door
# 20 → 30 se 10 door
# 30 → 30 se 0 door
# 40 → 30 se 10 door
# 50 → 30 se 20 door

# Isliye data mein spread hai.

# np.std() isi spread ko mathematically calculate karta hai.

# Ek important comparison

# Ye do datasets dekho:

# a = np.array([29, 30, 31])
# b = np.array([10, 30, 50])

# print(np.mean(a))
# print(np.mean(b))

# print(np.std(a))
# print(np.std(b))

# Dono ka mean 30 hai.

# Lekin:

# a ki values 30 ke bahut close hain → standard deviation small
# b ki values 30 se kaafi door hain → standard deviation large

# Yahi np.std() ka main idea hai:

# Small std → values close together
# Large std → values more spread out

# Data Analyst mein iska use data ki variability / 
# spread samajhne ke liye hota hai.

# Abhi formula ya manual calculation ki zarurat nahi hai. 
# NumPy mein function use karna focus hai.

# Practice — np.std()
# ==========================================
# NumPy — np.std()
# ==========================================

# Q1. Create a NumPy array:
# [10, 20, 30, 40, 50]
# Find the standard deviation using np.std().

# import numpy as np
# num = np.array([10, 20, 30, 40, 50])
# print(np.std(num))
#---------------------------------

# Q2. Create a NumPy array:
# [29, 30, 31]
# Find the standard deviation using np.std().

# import numpy as np
# num = np.array([29, 30, 31])
# print(np.std(num))
#--------------------------------

# Q3. Create a NumPy array:
# [10, 30, 50]
# Find the standard deviation using np.std().

# import numpy as np
# num = np.array([10, 30, 50])
# print(np.std(num))
#____________________________________________________________________________________________________

#==============================
# 6 np.median()
#==============================

# np.median() ka use middle value nikalne ke liye hota hai.

# Sabse important rule:

# Pehle values ko ascending order mein arrange karo, 
# phir middle value = Median.

# Example 1 — Odd number of values
# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(np.median(numbers))

# Output:

# 30.0

# Kyuki:

# 10  20  [30]  40  50
#           ↑
#        middle

# Isliye median = 30.

# Example 2 — Even number of values
# numbers = np.array([10, 20, 30, 40])

# print(np.median(numbers))

# Yahan 4 values hain, isliye exact single middle value nahi hai.

# Beech ki 2 values:

# 10  [20  30]  40

# Ab:

# (20 + 30) / 2 = 25

# Output:

# 25.0
# Data Analyst mein Median kyu useful hai?

# Median especially useful hota hai jab data mein outliers ho.

# Example:

# 20, 22, 25, 27, 500

# Yahan 500 bahut bada value hai.

# Mean kaafi affect hoga, lekin median:

# 20  22  [25]  27  500

# Median = 25

# Isliye salary, house price, transaction amount 

# jaise data mein median kaafi useful hota hai.

# Practice — np.median()
# ==========================================
# NumPy — np.median() 
# ==========================================

# Q1. Create a NumPy array with the values:
# [10, 20, 30, 40, 50]
# Find and print the median using np.median().

# import numpy as np
# num = np.array([10, 20, 30, 40, 50])
# print(np.median(num))
#-----------------------------------------------

# Q2. Create a NumPy array with the values:
# [15, 25, 35, 45]
# Find and print the median using np.median().

# import numpy as np
# num = np.array([15, 25, 35, 45])
# print(np.median(num))
#--------------------------------------------------

# Q3. Create a NumPy array with the values:
# [10, 20, 25, 30, 500]
# Find and print the median using np.median().

import numpy as np
num = np.array([10, 20, 30, 40, 500])
print(np.median(num))

