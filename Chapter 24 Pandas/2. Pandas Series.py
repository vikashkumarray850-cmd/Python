# =================================================
# CODE NUMBERING BY:-

# 17 TO 130 Series
# 134 TO 236 pd.Series()
# 240 TO 349 Series Index
# 353 TO 472 Custom Index
# 476 TO 560 Series Values
# 564 TO 644 Series Data Type
#-
# Series Basic Operations	
# 648 TO 723	├─ Arithmetic: +, -, *, /	
# 728 TO 838	├─ Series vs Series Operations
# 842 TO 950	└─ Comparison Operations: >, <, ==
# ===================================================

#==============================
# 1. Series
#==============================

# Pandas Series — 1. Series kya hoti hai?

# Simple language mein:

# Pandas Series ek one-dimensional data structure hai 
# jisme values ke saath index/label bhi hota hai.

# Tum ise abhi ek single column ki tarah samajh sakte ho.

# Example:

# import pandas as pd

# marks = pd.Series([45, 67, 82, 39, 91])

# print(marks)

# Output:

# 0    45
# 1    67
# 2    82
# 3    39
# 4    91
# dtype: int64

# Isko tod kar samjho:

# 0    45
# 1    67
# 2    82
# 3    39
# 4    91

# Left side:

# 0  1  2  3  4

# ye index hai.

# Right side:

# 45  67  82  39  91

# ye values hain.

# Abhi index ko detail mein nahi padhenge. Wo Topic 3 hai.

# Filhaal bas ye relationship yaad rakho:

# Series
#    ↓
# Values + Index
# NumPy se connection

# Tumne NumPy mein kiya tha:

# import numpy as np

# marks = np.array([45, 67, 82, 39, 91])

# Pandas mein:

# import pandas as pd

# marks = pd.Series([45, 67, 82, 39, 91])

# NumPy array mein mainly values hoti hain.

# Pandas Series mein values ke saath index/labels bhi hote hain.

# Ab sirf Topic 1 ki practice

# 3 questions karte hain, lekin sirf Series kya hoti hai wale concept par.

# ==========================================
# Pandas Series — Series Basics
# ==========================================

# Q1. Create a Pandas Series containing:
# [10, 20, 30, 40, 50]
#
# Print the Series.

# import pandas as pd
# marks = pd.Series([10, 20, 30, 40, 50])
# print(marks)
#-------------------------------------------

# Q2. Create a Pandas Series containing:
# [100, 200, 300]
#
# Print the Series and observe
# the index and values.

# import pandas as pd
# num = pd.Series([100, 200, 300])
# print(num)
#------------------------------------------------

# Q3. Create a Pandas Series containing:
# [500, 600, 700, 800]
#
# Print the Series.
#
# Observe which numbers Pandas automatically
# assigns as the index.

# import pandas as pd
# num = pd.Series([500, 600, 700, 800])
# print(num)
#________________________________________________________________________________________________

#==============================
# 2. pd.Series()
#==============================

# pd.Series() Pandas mein Series create karne ka function hai.

# Basic syntax:

# pd.Series(data)

# Example:

# import pandas as pd

# marks = pd.Series([45, 67, 82, 39, 91])

# print(marks)

# Output:

# 0    45
# 1    67
# 2    82
# 3    39
# 4    91
# dtype: int64

# Yahan:

# pd.Series([45, 67, 82, 39, 91])

# ka matlab hai:

# Is list ko Pandas Series mein convert/create karo.

# pd.Series() mein data kya ho sakta hai?

# Abhi basic level par tum list se Series bana rahe ho:

# pd.Series([10, 20, 30])

# Lekin Series mein different types ka data bhi ho sakta hai.

# Numbers:

# numbers = pd.Series([10, 20, 30])

# Strings:

# names = pd.Series(["Vikash", "Mohit", "Ravi"])

# Decimal values:

# prices = pd.Series([10.5, 20.5, 30.5])
# Important point

# pd.Series() data ko Series object mein convert/create karta hai.

# NumPy mein:

# np.array([10, 20, 30])

# Pandas mein:

# pd.Series([10, 20, 30])

# Dono ka purpose related hai, lekin Pandas Series 
# mein index/labels ka concept built-in hota hai.

# Practice — Topic 2 only
# ==========================================
# Pandas Series — pd.Series()
# ==========================================

# Q1. Use pd.Series() to create a Series
# containing:
# [10, 20, 30, 40, 50]
#
# Print the Series.

# import pandas as pd
# num = pd.Series([10, 20, 30, 40, 50])
# print(num)
#--------------------------------------

# Q2. Use pd.Series() to create a Series
# containing these names:
# ["Vikash", "Mohit", "Ravi"]
#
# Print the Series.

# import pandas as pd
# num = pd.Series(["Vikash", "Mohit", "Ravi"])
# print(num)
#---------------------------------------
# Q3. Use pd.Series() to create a Series
# containing these prices:
# [99.5, 149.5, 199.5, 249.5]
#
# Print the Series.

# import pandas as pd
# num = pd.Series([99.5, 149.5, 199.5, 249.5])
# print(num)
#_______________________________________________________________________________________________

# ==========================================
# 3. Series Index
# ==========================================

# Pandas Series — 
# Series mein index har value ki position/label hoti hai.

# Example:

# import pandas as pd

# marks = pd.Series([45, 67, 82, 39])

# print(marks)

# Output:

# 0    45
# 1    67
# 2    82
# 3    39
# dtype: int64

# Yahan:

# Index    Value
#   0       45
#   1       67
#   2       82
#   3       39

# Pandas automatically index deta hai:

# 0
# 1
# 2
# 3
# ...

# Default index 0 se start hota hai.

# Index se value access karna

# Agar humein index 2 ki value chahiye:

# print(marks[2])

# Output:

# 82

# Agar index 0:

# print(marks[0])

# Output:

# 45

# Isliye basic rule:

# marks[index]

# → us index ki value deta hai.

# NumPy se connection

# NumPy mein bhi indexing hoti hai:

# array[2]

# Pandas Series mein bhi:

# series[2]

# Lekin Pandas mein aage chal kar custom labels bhi use kar sakte hain.
# Wo next topic Custom Index mein karenge.

# Practice — Series Index only
# ==========================================
# Pandas Series — Series Index Practice
# ==========================================

# Q1. Create a Series:
# [100, 200, 300, 400, 500]
#
# Print the value 400 by using its index.

# import pandas as pd
# num = pd.Series([100, 200, 300, 400, 500])
# print(num[3])
#---------------------------------------------

# Q2. Create a Series:
# [25, 50, 75, 100]
#
# Print the value 25 by using its index.

# import pandas as pd
# marks = pd.Series([25, 50, 75, 100])
# print(marks[0])
#---------------------------------------------

# Q3. Create a Series:
# [10, 20, 30, 40, 50, 60]
#
# Print the value 60 by using its index.

# import pandas as pd
# num = pd.Series([10, 20, 30, 40, 50, 60])
# print(num[5])
#________________________________________________________________________________________________________

# ==========================================
# 4.  Custom Index
# ==========================================

# Abhi tak Pandas ne index automatically diya:

# import pandas as pd

# marks = pd.Series([45, 67, 82])

# print(marks)

# Output:

# 0    45
# 1    67
# 2    82

# Yahan index 0, 1, 2 hai.

# Custom Index kya hota hai?

# Hum apna index khud bhi de sakte hain.

# Example:

# import pandas as pd

# marks = pd.Series(
#     [45, 67, 82],
#     index=["Vikash", "Mohit", "Ravi"]
# )

# print(marks)

# Output:

# Vikash    45
# Mohit     67
# Ravi      82
# dtype: int64

# Ab:

# Index    Value
# Vikash   45
# Mohit    67
# Ravi     82

# Yaani ab 0, 1, 2 ki jagah names index ban gaye.

# Custom index se value access
# print(marks["Mohit"])

# Output:

# 67

# Yahan "Mohit" index label hai.

# Important:

# marks[1]

# aur

# marks["Mohit"]

# Custom index ke context mein same value ko represent kar sakte hain,
# lekin label-based access ke liye "Mohit" use karna clearer hai.

# Practice — Custom Index
# ==========================================
# Pandas Series — Custom Index Practice
# ==========================================

# Q1. Create a Series with these values:
# [25000, 35000, 50000]
#
# Use these custom indexes:
# ["Vikash", "Mohit", "Ravi"]
# Print the complete Series.

# import pandas as pd
# salary = pd.Series(
#     [25000, 35000, 50000],
#     index =["Vikash", "Mohit", "Ravi"]
# )
# print(salary)
#------------------------------------------------------

# Q2. Create a Series with these values:
# [85, 72, 91, 68]
#
# Use these custom indexes:
# ["Math", "English", "Science", "History"]
#
# Print the marks of Science using its custom index.

# import pandas as pd
# marks = pd.Series(
#     [85, 72, 91, 68],
#     index=["Math", "English", "Science", "History"]
# )
# print(marks["Science"])
# ------------------------------------------------------------------

# Q3. Create a Series with these values:
# [7, 14, 21]
#
# Use these custom indexes:
# ["Egg", "Maggi", "Milk"]
#
# Print the price of Maggi using its custom index.

# import pandas as pd
# price = pd.Series(
#     [7, 14, 21],
#     index=["Egg", "Maggi", "Milk"]
# )
# print(price["Maggi"])
#________________________________________________________________________________________________________

#==============================
# 5. Series Values
#==============================

# Series mein jo actual data hota hai, usse values kehte hain.

# Example:

# import pandas as pd

# marks = pd.Series([45, 67, 82, 39])

# print(marks)

# Output:

# 0    45
# 1    67
# 2    82
# 3    39
# dtype: int64

# Yahan:

# Index →  0   1   2   3
# Value → 45  67  82  39

# Agar hume sirf values chahiye, Pandas mein .values use kar sakte hain:

# print(marks.values)

# Output:

# [45 67 82 39]
# Important difference
# print(marks)

# → Index + Values + dtype

# print(marks.values)

# → Sirf Values

# .values attribute hai, function nahi. Isliye:

# marks.values

# ✅

# marks.values()

# ❌

# Practice
# ==========================================
# Pandas Series — Series Values Practice
# ==========================================

# Q1. Create a Series with:
# [100, 200, 300, 400]
#
# Print only the values of the Series.

# import pandas as pd
# num = pd.Series([100, 200, 300, 400])
# print(num.values)
#--------------------------------------------

# Q2. Create a Series with:
# ["Vikash", "Mohit", "Ravi"]
#
# Print only the values of the Series.

# import pandas as pd
# name = pd.Series(["Vikash", "Mohit", "Ravi"])
# print(name.values)
#------------------------------------------

# Q3. Create a Series with:
# [7, 14, 21, 28, 35]

# Print only the values of the Series.

# import pandas as pd
# num = pd.Series([7, 14, 21, 28, 35])
# print(num.values)
#__________________________________________________________________________________________________

#==============================
# 6. Series Data Type 
#==============================

# Series mein values kis type ki hain, ye jaanne ke liye dtype use karte hain.

# Example 1: Integer values
# import pandas as pd

# marks = pd.Series([45, 67, 82, 39])

# print(marks.dtype)

# Output:

# int64

# int64 ka matlab hai ki values integers hain, jaise 45, 67, 82.

# Example 2: Decimal values
# price = pd.Series([99.5, 149.5, 199.5])

# print(price.dtype)

# Output:

# float64

# float64 ka matlab hai ki values decimal/floating-point numbers hain.

# Example 3: String values
# name = pd.Series(["Vikash", "Mohit", "Ravi"])

# print(name.dtype)

# Output aam taur par:

# object

# Strings ke liye Pandas aksar object dikhata hai.

# Yaad rakho
# Code	Kya batata hai?
# marks.values	Sirf values
# marks.dtype	Values ka data type
# marks.shape	Series mein elements ki sankhya aur dimensions

# Abhi hum sirf dtype par focus karenge.

# Practice — Series Data Type
# ==========================================
# Pandas Series — dtype Practice
# ==========================================

# Q1. Create a Series with:
# [10, 20, 30, 40]
#
# Print the data type of the Series.

# import pandas as pd
# marks = pd.Series([10, 20, 30, 40])
# print(marks.dtype)
#-----------------------------------

# Q2. Create a Series with:
# [12.5, 25.5, 37.5]
#
# Print the data type of the Series.

# import pandas as pd
# marks = pd.Series([12.5, 25.5, 37.5])
# print(marks.dtype)
#--------------------------------------

# Q3. Create a Series with:
# ["Apple", "Mango", "Banana"]
#
# Print the data type of the Series.

# import pandas as pd
# fruits = pd.Series(["Apple", "Mango", "Banana"])
# print(fruits.dtype)
#_______________________________________________________________________________________________________

#==============================
# 7. Series Basic Operations 
#==============================

#======================================
# Series Basic Operations	
# 	├─ Arithmetic: +, -, *, /	
# 	├─ Series vs Series Operations
# 	└─ Comparison Operations: >, <, ==
#======================================

# Is topic mein hum Series par basic calculations aur operations seekhenge. 
# Lekin ek-ek karke shuru karenge.

# Pehla concept: Series mein arithmetic operations.

# import pandas as pd

# prices = pd.Series([10, 20, 30])

# print(prices + 5)

# Output:

# 0    15
# 1    25
# 2    35
# dtype: int64

# Yahan + 5 har value mein 5 add karta hai. Original Series 
# prices apne aap change nahi hoti.

# Isi tarah -, * aur / bhi use kar sakte hain.

# Practice — Arithmetic Operations

# ==========================================
# 1. Addition Practice
# ==========================================

# Q1. Create a Series with:
# [20, 40, 60]
#
# Add 10 to every value and print the result.

# import pandas as pd
# marks = pd.Series([20, 40, 60])
# print(marks + 10)
#--------------------------------------------

# Q2. Create a Series with:
# [100, 150, 200]
#
# sub 25 to every value and print the result.

# import pandas as pd
# num = pd.Series([100, 150, 200])
# result = num - 25
# print(result)
#-----------------------------------------------

# Q3. Create a Series with:
# [5, 15, 25]
#
# Add 5 to every value.
# Store the result in a new variable.
# Print both the original Series and the new Series.

# import pandas as pd
# value = pd.Series([5, 15, 25])
# result = value + 5

# print("original Series")
# print(value)

# print("new series")
# print(result)
#______________________________________________________________________________________________________


#==============================
# 2. Series Basic Operations (Part 2)
#==============================

# Series Basic Operations (Part 2): Series vs Series

# Abhi tak humne Series ki har value par ek fixed number se 
# calculation ki thi, jaise prices + 5.

# Ab dekho, jab do Series ko aapas mein add karte hain, toh kya hota hai.

# 1. Do Series ko add karna
# import pandas as pd

# prices1 = pd.Series([10, 20, 30])
# prices2 = pd.Series([1, 2, 3])

# print(prices1 + prices2)

# Output:

# 0    11
# 1    22
# 2    33
# dtype: int64

# Pandas corresponding index ki values ko add karta hai:

# Index	prices1	prices2	Result
# 0	10	1	11
# 1	20	2	22
# 2	30	3	33

# Yaani:

# Index 0 par: 10 + 1 = 11
# Index 1 par: 20 + 2 = 22
# Index 2 par: 30 + 3 = 33
# 2. Agar dono Series ke indexes alag hon?
# import pandas as pd

# a = pd.Series([10, 20], index=["A", "B"])
# b = pd.Series([5, 7], index=["B", "C"])

# print(a + b)

# Output:

# A     NaN
# B    25.0
# C     NaN
# dtype: float64

# Kyun?

# A: doosri Series mein A nahi hai, isliye NaN.
# B: dono Series mein B hai, isliye 20 + 5 = 25.
# C: pehli Series mein C nahi hai, isliye NaN.

# Important: Pandas Series ko add karte waqt index labels 
# match karta hai, sirf position nahi. Missing matching 
# values ke kaaran result mein NaN aa sakta hai.

# Practice — Series vs Series
# ==========================================
# Pandas Series — Series Operations Practice
# ==========================================

# Q1. Create two Series:
# First Series:  [10, 20, 30]
# Second Series: [5, 10, 15]
#
# Add both Series and print the result.

# import pandas as pd
# First_Series = pd.Series([10, 20, 30])
# Second_Series = pd.Series([40, 50, 60])

# print(First_Series + Second_Series)
#-------------------------------------------------

# Q2. Create two Series:
# First Series:  [100, 200, 300]
# Second Series: [10, 20, 30]
#
# Subtract the second Series from the first Series.
# Print the result.

# import pandas as pd
# First_Series = pd.Series([100, 200, 300])
# Second_Series = pd.Series([10, 20, 30])

# print(First_Series - Second_Series)
#----------------------------------------------

# Q3. Create two Series:
# First Series:
# Values: [10, 20]
# Index:  ["A", "B"]
#
# Second Series:
# Values: [5, 7]
# Index:  ["B", "C"]
#
# Add both Series and print the result.

# import pandas as pd
# First_Series = pd.Series([10, 20], index=["A", "B"])
# Second_Series = pd.Series([5, 7], ["B", "C"])

# result = First_Series + Second_Series
# print(result)
#________________________________________________________________________________________________

#==============================
# 3. Comparison Operations
#==============================

# Comparison ka matlab hai values ko compare karna aur 
# check karna ki koi condition True hai ya False.

# Pandas Series mein hum ye operators use karte hain:

# Operator	Meaning	Example
# >	Greater than (se bada)	marks > 50
# <	Less than (se chhota)	marks < 50
# >=	Greater than or equal to	marks >= 50
# <=	Less than or equal to	marks <= 50
# ==	Equal to (barabar)	marks == 50
# !=	Not equal to (barabar nahi)	marks != 50
# 1. Greater than (>)

# Maan lo students ke marks hain:

# import pandas as pd

# marks = pd.Series([35, 60, 80, 45])

# print(marks > 50)

# Output:

# 0    False
# 1     True
# 2     True
# 3    False
# dtype: bool

# Ab ise step by step samjho:

# Index	Marks	Condition marks > 50	Result
# 0	35	35 > 50	False
# 1	60	60 > 50	True
# 2	80	80 > 50	True
# 3	45	45 > 50	False
# 60 > 50 → True
# 80 > 50 → True
# 35 > 50 → False
# 45 > 50 → False

# Important: Abhi hum sirf condition check kar rahe hain. 
# Humne original Series se koi value delete nahi ki.

# 2. Equal to (==)

# Agar hume check karna ho ki kaun-si value 50 ke barabar hai:

# marks = pd.Series([30, 50, 70, 50])

# print(marks == 50)

# Output:

# 0    False
# 1     True
# 2    False
# 3     True
# dtype: bool

# Dhyan do: == comparison ke liye hai, 
# jabki = variable mein value assign karne ke liye hai.

# x = 50      # Assignment
# x == 50     # Comparison
# Practice — Comparison Operations
# ==========================================
# Pandas Series — Comparison Practice
# ==========================================

# Q1. Create a Series with:
# [25, 55, 75, 40, 90]
#
# Check which values are greater than 60.
# Print the comparison result.

# import pandas as pd
# marks = pd.Series([25, 55, 75, 40, 90])
# result = marks > 60
# print(result)
# --------------------------------------

# Q2. Create a Series with:
# [10, 20, 30, 20, 40]
#
# Check which values are equal to 20.
# Print the comparison result.

# import pandas as pd
# marks = pd.Series([10, 20, 30, 20, 40])
# result = marks == 20
# print(result)
#----------------------------------------

# Q3. Create a Series with:
# [15, 35, 50, 65, 80]
#
# Check which values are less than or equal to 50.
# Print the comparison result.

# import pandas as pd
# marks = pd.Series([15, 35, 50, 65, 80])
# result = marks <= 50
# print(result)
#