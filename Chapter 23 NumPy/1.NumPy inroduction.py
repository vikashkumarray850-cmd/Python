# ==========================================
# NUMPY — INTRODUCTION
# ==========================================

# 1. NumPy kya hai?

# NumPy ka full form hai:

# Numerical Python

# NumPy Python ki ek library hai jo mainly numerical data yani 
# numbers ke saath efficiently kaam karne ke liye use hoti hai.

# Simple example:

# Python mein:

# numbers = [10, 20, 30, 40, 50]

# NumPy mein hum isi numerical data ko array ke form mein rakh sakte hain:

# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(numbers)

# Output:

# [10 20 30 40 50]

# Yahan abhi tumhe sirf itna samajhna hai:

# Python List → [10, 20, 30, 40, 50]

# NumPy Array → np.array([10, 20, 30, 40, 50])

# NumPy ka main focus numbers aur numerical calculations par hai.

# Ek important baat

# Abhi main np.array() ko detail mein explain nahi karunga, kyunki woh tumhare roadmap ka:

# 2. NumPy Array Basics → 3. np.array()

# mein aayega.

# Isi tarah import numpy as np bhi hum 1.4 aur 1.5 mein properly dekhenge.

# Matlab abhi hum sirf:

# 1 → NumPy kya hai?

# itna hi kar rahe hain. 👍

# Chhota sa Practice
# ==========================================
# NumPy — Introduction
# ==========================================

# Q1. Write one line to import NumPy.

# import numpy as np

# Q2. Create a NumPy array containing:
# 10, 20, 30, 40, 50

# number = np.array([10, 20, 30, 40, 50])

# Q3. Print the NumPy array.
# print(number)
#_______________________________________________________

# =================================================
# 2. DATA ANALYST KE LIYE NUMPY KYU IMPORTANT HAI?
# =================================================

# Vikash, abhi sirf ek hi concept samjhenge.

# Data Analyst ke kaam mein hume bahut saara numerical data handle karna padta hai.

# Example:

# sales = [1000, 1500, 2000, 2500, 3000]

# Hume aksar questions milte hain:

# Total sales kitni hai?
# Average sales kitni hai?
# Sabse kam sale kitni hai?
# Sabse zyada sale kitni hai?
# Kaunse values ek condition satisfy karti hain?
# Bahut saare numbers par calculation kaise karein?

# NumPy in numerical operations ko easy aur efficient banata hai.

# Example

# NumPy ke bina:

# sales = [1000, 1500, 2000, 2500, 3000]

# total = 0

# for sale in sales:
#     total += sale

# print(total)

# NumPy ke saath:

# import numpy as np

# sales = np.array([1000, 1500, 2000, 2500, 3000])

# print(np.sum(sales))

# Output:

# 10000

# Yani NumPy mein numerical calculations ke liye ready-made functions milte hain.

# Data Analyst connection
# Raw Numerical Data
#         ↓
#      NumPy
#         ↓
# Calculations / Filtering / Processing
#         ↓
#      Analysis

# Isliye NumPy Data Analysis ke foundation ka important part hai.

# Abhi np.sum() ko detail mein nahi padhenge, kyunki woh roadmap ke 
# 7. NumPy Functions → np.sum() mein aayega.

# Chhoti Practice
# ==========================================
# NumPy — Importance for Data Analyst
# ==========================================

# import numpy as np

# Q1. Create a Python list containing 5 sales values.
# Print the list.

# sales = [1000, 1500, 2000, 2500, 3000]
# print(sales)

# Q2. Convert the sales data into a NumPy array.
# Print the NumPy array.

# sales_array = np.array(sales)
# print(sales_array)

# Q3. Write one sentence as a comment explaining
# why NumPy is useful for a Data Analyst.

# NumPy is useful for a Data Analyst because it makes
# numerical data processing and calculations easier.

#_______________________________________________________________________-

# ==========================================
# 3. NumPy install karna
# ==========================================

# Vikash, is step mein hum sirf NumPy install karna samjhenge.

# NumPy install kyu karna padta hai?

# NumPy Python ki built-in library nahi hai. Isliye agar system mein 
# NumPy installed nahi hai, to pehle install karna padta hai.

# Tum VS Code + PowerShell use kar rahe ho, to PowerShell mein ye
#  command run kar sakte ho:

# pip install numpy

# Agar installation successful hai, to generally aisa message milega:

# Successfully installed numpy
# Check kaise karein?

# Installation ke baad VS Code mein Python file banao:

# import numpy

# Agar koi error nahi aata, to NumPy installed hai. ✅

# Aur version check karna ho:

# import numpy as np

# print(np.__version__)

# Example output:

# 2.x.x

# Version number tumhare system mein different ho sakta hai.

# Important

# Install aur import alag cheezein hain:

# pip install numpy
#         ↓
#    NumPy install
#         ↓
# import numpy as np
#         ↓
# Python program mein NumPy use

# Abhi hum import numpy as np ko detail mein nahi karenge — woh roadmap ka next point hai.

# Chhoti Practice
# ==========================================
# NumPy — Installation
# ==========================================

# Q1. Write the command used to install NumPy using pip.

# pip install numpy

# Q2. Write one line of Python code to check
# whether NumPy can be imported.

# import numpy as np

# print(np.__version__)
#___________________________________________________________________--

# ==========================================
# 4. NUMPY IMPORT KARNA
# 5. IMPORT NUMPY AS NP
# ==========================================

# NumPy install karne ke baad Python program mein use karne ke 
# liye usko import karna padta hai.

# Sabse common syntax:

# import numpy as np

# Isko break karke samjho:

# import       → library ko Python program mein lana
# numpy        → library ka naam
# as           → ek short name dena
# np           → NumPy ka short name

# Isliye:

# import numpy as np

# ke baad hum numpy ki jagah np use karte hain.

# Example:

# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(numbers)

# Yahan:

# np.array()

# NumPy ka array() use kar raha hai.

# Ek aur example
# import numpy as np

# sales = np.array([1000, 2000, 1500, 3000])

# print(sales)

# Output:

# [1000 2000 1500 3000]

# Bas abhi itna yaad rakho:

# import numpy as np
#         ↓
# NumPy ko import kiya
#         ↓
# np = NumPy ka short name
# Practice
# ==========================================
# NumPy — Import Practice
# ==========================================

# Q1. Import NumPy using the alias np.

# import numpy as np

# Q2. Create a NumPy array containing:
# 10, 20, 30, 40, 50
# Print the array.

# number =np.array([10, 20, 30, 40, 50])
# print(number)

# Q3. Create a NumPy array containing:
# 100, 200, 300
# Print the array.

# number = np.array([100, 200, 300])
# print(number)

