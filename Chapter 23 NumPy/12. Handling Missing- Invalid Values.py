# ==============================
# CODE NUMBERING BY:-

# 10 TO 97 np.nan
# 103 TO 179 np.isnan() 
# 182 TO 307 Basic Missing-Value Operations
# ==============================

#==============================
# 1 np.nan
#==============================

# Data Analysis mein kabhi-kabhi data missing hota hai.

# Example:

# Salary → 25000
# Salary → 35000
# Salary → missing
# Salary → 50000

# NumPy mein missing numerical value represent karne ke liye commonly:

# np.nan

# use karte hain.

# nan ka meaning hai:

# Not a Number

# Example:

# import numpy as np

# salary = np.array([25000, 35000, np.nan, 50000])

# print(salary)

# Output:

# [25000. 35000.    nan 50000.]

# Notice karo ki np.nan ke wajah se array ke numbers float ban gaye.

# np.nan ko normal value ki tarah compare nahi karna chahiye

# Example:

# print(np.nan == np.nan)

# Output:

# False

# Isliye missing value check karne ke liye hum baad mein:

# np.isnan()

# use karenge.

# Abhi sirf np.nan samjho:

# np.nan → missing numerical value ko represent karta hai
# Practice — np.nan
# ==========================================
# NumPy — np.nan Practice
# ==========================================

# Q1. Create a NumPy array:
# [100, 200, np.nan, 400, 500]
#
# Print the array.

# import numpy as np
# num = np.array([100, 200, np.nan, 400, 50])
# print(num)
#--------------------------------------------

# Q2. Create a NumPy array representing employee salaries:
# [25000, 35000, np.nan, 55000, 65000]
#
# Print the array and check its dtype.

# import numpy as np
# salary = np.array([25000, 35000, np.nan, 55000, 65000])
# print(salary)
# print(salary.dtype)
#-----------------------------------------------------

# Q3. Create a NumPy array:
# [10, np.nan, 30, np.nan, 50]
#
# Print the array.

# import numpy as np
# num = np.array([10, np.nan, 30, np.nan, 50])
# print(num)
#___________________________________________________________________________________________________


#==============================
# 2. np.isnan()
#==============================

# np.isnan() ka kaam kya hai?

# np.nan se hum missing value ko represent karte hain.

# Lekin agar hume check karna ho ki array mein kaunsi values missing hain, 
# tab np.isnan() use karte hain.

# Example:

# import numpy as np

# data = np.array([10, np.nan, 30, np.nan, 50])

# print(np.isnan(data))

# Output:

# [False  True False  True False]

# Meaning:

# 10       → False → missing nahi hai
# np.nan   → True  → missing hai
# 30       → False → missing nahi hai
# np.nan   → True  → missing hai
# 50       → False → missing nahi hai
# Important rule
# np.isnan(data)

# Missing values → True

# Normal values → False

# Ye ek Boolean array return karta hai.

# Data Analyst mein iska use bahut important hai, 
# kyunki real dataset mein missing values identify 
# karne ke liye isi type ka check karte hain.

# Practice
# ==========================================
# NumPy — np.isnan() Practice
# ==========================================

# Q1. Create a NumPy array:
# [10, 20, np.nan, 40, np.nan]
#
# Use np.isnan() to check which values are missing.

# import numpy as np
# num = np.array([10, 20, np.nan, 40, np.nan])
# print(np.isnan(num))
#---------------------------------------------------

# Q2. Create a NumPy array representing employee salaries:
# [25000, np.nan, 40000, 55000, np.nan]
#
# Use np.isnan() to identify the missing salary values.

# import numpy as np
# salary = np.array([25000, np.nan, 40000, 55000, np.nan])
# print(np.isnan(salary))
#-----------------------------------------------------------

# Q3. Create a NumPy array:
# [100, 200, 300, np.nan, 500]
#
# Use np.isnan() and print the result.

# import numpy as np
# num = np.array([100, 200, 300, np.nan, 500])
# result = np.isnan(num)
# print(result)
#--------------------------------------------------------------

#==================================
# 3. Basic Missing-Value Operations
#==================================

# Ab hum practical part par aate hain: np.nan mil gaya aur 
# np.isnan() se identify bhi kar liya. 
# Ab missing values ke saath kya karna hai.

# Data Analysis mein generally 3 basic kaam important hain:

# Missing values count karna
# Missing values ko ignore karke calculation karna
# Missing values ko replace karna
# 1. Missing values count karna

# np.isnan() Boolean array deta hai:

# import numpy as np

# data = np.array([10, np.nan, 30, np.nan, 50])

# missing = np.isnan(data)

# print(missing)
# print(np.sum(missing))

# Output:

# [False  True False  True False]
# 2

# Yahan True = 1 aur False = 0 ki tarah count ho sakta hai.

# Isliye:

# np.sum(np.isnan(data))

# → total 2 missing values.

# 2. np.nan ke saath normal calculation

# Agar array mein np.nan hai:

# data = np.array([10, 20, np.nan, 40])
# print(np.mean(data))

# Result:

# nan

# Kyunki normal np.mean() missing value ko handle nahi karta.

# Iske liye NumPy mein nan-aware functions hain:

# print(np.nanmean(data))

# Ye np.nan ko ignore karke mean calculate karega.

# Isi tarah:

# np.nansum()
# np.nanmean()
# np.nanmin()
# np.nanmax()

# Important Data Analyst point hai.

# 3. Missing value ko replace karna

# Example:

# data = np.array([10, 20, np.nan, 40, 50])

# data[np.isnan(data)] = 0

# print(data)

# Output:

# [10. 20.  0. 40. 50.]

# Yahan humne saare np.nan ko 0 se replace kar diya.

# Real-world data mein 0 har situation mein correct replacement nahi hota. 
# Kabhi mean, median ya doosri appropriate value use karni padti hai. 
# Abhi basic concept samajhna important hai.

# Practice
# ==========================================
# NumPy — Basic Missing-Value Operations
# ==========================================

# Q1. Create a NumPy array:
# [10, np.nan, 30, np.nan, 50, np.nan]
#
# Count and print the total number of missing values.

# import numpy as np
# num = np.array([10, np.nan, 30, np.nan, 50, np.nan])
# missing = np.isnan(num)
# print(missing)
# print(np.sum(missing))

#-----------------------------------

# Q2. Create a NumPy array:
# [10, 20, np.nan, 40, 50]
#
# Calculate and print the mean while ignoring the missing value.

# import numpy as np
# num = np.array([10, np.nan, 30, np.nan, 50, np.nan])
# print(np.mean(num))
#---------------------------------------------

# Q3. Create a NumPy array:
# [100, np.nan, 300, np.nan, 500]
#
# Replace all missing values with 0.
#
# Print the updated array.

data = np.array([10, 20, np.nan, 40, 50])

data[np.isnan(data)] = 0

print(data)
