# ========================================
# CODE NUMBERING BY:-

# 10 TO 132 np.random / np.random.randint()
# 136 TO 199 np.random.rand()
# 203 TO 281 Basic random data generation
# ========================================

#==============================
# 1. np.random
#==============================

# Data Analyst ke liye random numbers ka use kahan hota hai?

# Sample data generate karne mein
# Testing/practice data banane mein
# Simulation mein
# Dummy sales, marks, salary data generate karne mein
# 13.1 np.random

# np.random NumPy ka random-number related module hai.

# Iske andar different functions hote hain, jaise:

# np.random.randint()
# np.random.rand()

# Hum pehle randint() samjhenge.

# np.random.randint()

# Ye random integer generate karta hai.

# Basic syntax:

# np.random.randint(start, stop)

# Important: stop include nahi hota.

# Example:

# import numpy as np

# num = np.random.randint(1, 10)

# print(num)

# Output har baar different ho sakta hai:

# 7

# Ya:

# 3

# Ya:

# 9

# Lekin 10 nahi aayega.

# Matlab:

# 1 ≤ number < 10
# Multiple random numbers

# Agar hume ek se zyada numbers chahiye:

# import numpy as np

# num = np.random.randint(1, 10, 5)

# print(num)

# Yahan:

# 1 → starting value
# 10 → stopping value (excluded)
# 5 → kitne random numbers chahiye

# Example output:

# [4 8 2 7 1]

# Har execution mein values change ho sakti hain.

# Data Analyst example

# Suppose hume practice ke liye 10 random employee salaries generate karni hain:

# import numpy as np

# salary = np.random.randint(25000, 80000, 10)

# print(salary)

# Ye 25,000 se 79,999 ke beech 10 random integer salaries generate karega.

# Important: Randomly generated values har run mein 
# change ho sakti hain. Ye normal behavior hai.

# Practice — np.random.randint()
# ==========================================
# NumPy — np.random.randint() Practice
# ==========================================

# Q1. Generate one random integer between 1 and 100.
#
# Print the result.

# import numpy as np
# num = np.random.randint(1, 100)
# print(num)
#------------------------------------------------------

# Q2. Generate 5 random integers between 10 and 50.
#
# Print the resulting NumPy array.

# import numpy as np
# num = np.random.randint(10, 50, 5)
# print(num)
#-------------------------------------------------------

# Q3. Generate 10 random employee salaries between
# 20000 and 60000.
#
# Print the resulting NumPy array.

# import numpy as np
# salary = np.random.randint(20000, 60000, 10)
# print(salary)
#_______________________________________________________________________________________________________

#==============================
# 2. np.rand()
#==============================

# np.random.rand()

# rand() 0 se 1 ke beech random decimal numbers generate karta hai.

# Example:

# import numpy as np

# num = np.random.rand()

# print(num)

# Possible output:

# 0.735421

# Multiple values:

# num = np.random.rand(5)

# print(num)

# Possible output:

# [0.24 0.81 0.13 0.67 0.45]

# Yahan 5 ka matlab 5 random decimal values.

# Difference yaad rakho
# randint() → random integers
# rand()    → random decimal values between 0 and 1

# ==========================================
# NumPy — np.random.rand() Practice
# ==========================================

# Q1. Generate one random decimal number between 0 and 1.
#
# Print the result.

# import numpy as np
# number = np.random.rand()
# print(number)
#-----------------------------------------------------

# Q2. Generate 5 random decimal numbers between 0 and 1.
#
# Print the resulting NumPy array.

# import numpy as np
# num = np.random.rand(5)
# print(num)
#-------------------------------------

# Q3. Generate 10 random decimal numbers between 0 and 1.
#
# Print the resulting NumPy array.

# import numpy as np
# num = np.random.rand(10)
# print(num)
#_____________________________________________________________________________________________________

#================================
# 3. Basic Random Data Generation
#================================

# Ab hum randint() aur rand() ko combine karke dummy data generate karenge.

# Data Analyst practice mein jab actual dataset available nahi hota, 
# tab testing ke liye aisa data generate karna useful hota hai.

# Example 1 — Sales Data

# Maan lo 10 days ki sales generate karni hain:

# import numpy as np

# sales = np.random.randint(1000, 10000, 10)

# print(sales)

# Yahan:

# 1000 → minimum
# 10000 → maximum excluded
# 10 → 10 sales values
# Example 2 — Product Prices
# import numpy as np

# prices = np.random.randint(50, 500, 5)

# print(prices)

# Ye 50 se 499 ke beech 5 random prices generate karega.

# Example 3 — Percentage Data

# Agar decimal values chahiye:

# import numpy as np

# percentage = np.random.rand(5) * 100

# print(percentage)

# np.random.rand(5) → 0–1 ke beech values.

# * 100 → unhe 0–100 range mein convert kar deta hai.

# Practice
# ==========================================
# NumPy — Basic Random Data Generation
# ==========================================

# Q1. Generate 7 random daily sales values
# between 1000 and 10000.
#
# Print the NumPy array.

# import numpy as np
# sales = np.random.randint(1000,10000,7)
# print(sales)
#------------------------------------

# Q2. Generate 5 random product prices
# between 100 and 1000.
#
# Print the NumPy array.

# import numpy as np
# prices = np.random.randint(100, 1000, 5)
# print(prices)
#-------------------------------------------

# Q3. Generate 10 random percentage values
# between 0 and 100 using np.random.rand().
#
# Print the NumPy array.

import numpy as np
percentage = np.random.rand(10)* 100
print(percentage)