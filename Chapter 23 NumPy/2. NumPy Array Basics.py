# ==========================================
# CODE NUMBERING BY:-

# 11 TO 84 (NUMPY ARRAY BASICS)
# 88 TO 210 (PYTHON LIST VS NUMPY ARRAY)
# 216 TO 328 ( NP.ARRAY) 
# 332 TO 425 (1D Array)
# 430 T0 530 (2D Array)
# 530 TO 667 (3D ARRAY)
# ==========================================
# ==========================================
# 2. NUMPY ARRAY BASICS
# ==========================================

# 1. Array kya hota hai?

# Simple language mein:

# Array ek container hai jisme multiple values ko ek saath store kar sakte hain.

# Example:

# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(numbers)

# Output:

# [10 20 30 40 50]

# Yahan numbers ek NumPy array hai.

# Array ko simple way mein samjho
# 10   20   30   40   50
# ↓    ↓    ↓    ↓    ↓
# Ek hi NumPy Array

# Abhi hum sirf 1D array ka basic dekh rahe hain.

# Ek important baat:

# numbers = np.array([10, 20, 30])

# np.array() → NumPy array banata hai.

# Data Analyst example

# Maan lo kisi shop ki daily sales:

# sales = np.array([1000, 1500, 1200, 1800, 2000])

# To ye 5 days ki sales ko ek NumPy array mein store kar raha hai.

# Practice — 3 Questions
# ==========================================
# NumPy — Array Basics
# ==========================================

# Q1. Create a NumPy array containing:
# 10, 20, 30, 40, 50
# Print the array.

# import numpy as np
# number = np.array([10, 20, 30, 40, 50])
# print(number)
#--------------

# Q2. Create a NumPy array containing 5 student marks.
# Print the array.

# import numpy as np
# marks = np.array([60, 47, 37, 56, 39])
# print(marks)
#-------------------

# Q3. Create a NumPy array containing 5 daily sales values.
# Print the array.

# import numpy as np
# sales = np.array([2000, 5000, 6389, 4763, 48788])
# print(sales)

#__________________________________________________________________________

# ==========================================
# 2. PYTHON LIST VS NUMPY ARRAY
# ==========================================

# Ab hum Python List aur NumPy Array ka difference samjhenge.

# Python List

# Python mein multiple values store karne ke liye list use karte hain:

# numbers = [10, 20, 30, 40, 50]

# print(numbers)

# Output:

# [10, 20, 30, 40, 50]
# NumPy Array

# NumPy mein:

# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(numbers)

# Output:

# [10 20 30 40 50]

# Ab important difference dekho.

# Multiplication

# Python List:

# numbers = [10, 20, 30]

# print(numbers * 2)

# Output:

# [10, 20, 30, 10, 20, 30]

# List mein * 2 ka matlab list ko repeat karna hai.

# NumPy Array:

# import numpy as np

# numbers = np.array([10, 20, 30])

# print(numbers * 2)

# Output:

# [20 40 60]

# NumPy mein * 2 ka matlab har value ko 2 se multiply karna hai.

# Data Analyst ke liye ye important kyu hai?

# Maan lo sales hain:

# sales = np.array([1000, 2000, 3000])

# Agar sabhi sales values ko 10% increase karna ho:

# sales = sales * 1.10

# print(sales)

# Output:

# [1100. 2200. 3300.]

# Yahi type ke numerical operations Data Analysis mein bahut useful hote hain.

# Short difference
# Python List
# → General-purpose collection
# → Data ko store karne ke liye useful

# NumPy Array
# → Numerical data ke liye specially useful
# → Mathematical operations easily perform kar sakte hain

# Abhi dtype, shape, ndim etc. mein nahi jayenge. Woh roadmap ke 
# 3. Array Properties mein aayega.

# Practice — 3 Questions
# ==========================================
# NumPy — List vs NumPy Array
# ==========================================

# Q1. Create a Python list containing:
# 10, 20, 30
# Multiply the list by 2.
# Print the result.

# number = [10,20,30]
# print(number * 2)

#------------------------

# Q2. Create a NumPy array containing:
# 10, 20, 30
# Multiply the array by 2.
# Print the result.

# import numpy as np
# number = np.array([10,20,30])
# result = number * 2
# print(result)

# Q3. Create a NumPy array containing 5 prices.
# Increase every price by 10%.
# Print the updated prices.

# import numpy as np
# sales = np.array([2000,4477,7770,8000,5000])
# sales = sales * 1.10 
# print(sales)
#_______________________________________________________________________


# ==========================================
# 3. NP.ARRAY()
# ==========================================

# Ab hum sirf np.array() ko samjhenge.

# np.array() kya karta hai?

# np.array() ka use NumPy array create karne ke liye hota hai.

# Syntax:

# np.array(data)

# Example:

# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(numbers)

# Output:

# [10 20 30 40 50]

# Yahan:

# [10, 20, 30, 40, 50]

# data hai, aur:

# np.array()

# us data ko NumPy array mein convert kar raha hai.

# Python List → NumPy Array

# Pehle ek normal Python list:

# numbers = [10, 20, 30, 40, 50]

# Ab usko NumPy array mein convert karo:

# import numpy as np

# numbers = [10, 20, 30, 40, 50]

# numbers = np.array(numbers)

# print(numbers)

# Output:

# [10 20 30 40 50]

# Matlab:

# Python List
#     ↓
# np.array()
#     ↓
# NumPy Array
# Ek aur example
# import numpy as np

# marks = [70, 80, 65, 90, 75]

# marks = np.array(marks)

# print(marks)

# Yahan marks pehle list thi, phir np.array() ki help se NumPy array ban gayi.

# Important

# Abhi hum np.array() ka basic use hi kar rahe hain.

# 1D Array aur 2D Array ko alag se next points mein properly dekhenge.

# Practice — 3 Questions
# ==========================================
# NumPy — np.array()
# ==========================================

# Q1. Create a Python list containing:
# 10, 20, 30, 40
# Convert the list into a NumPy array.
# Print the array.

# import numpy as np
# numbers = [ 10, 20, 30, 40, 50]
# numbers = np.array(numbers)
# print(numbers)
#----------------------------

# Q2. Create a Python list containing 5 student marks.
# Convert the list into a NumPy array.
# Print the array.

# import numpy as np
# marks = [70, 80, 65, 90, 75] 
# marks = np.array(marks)
# print(marks)
#-----------------------------

# Q3. Create a Python list containing 5 product prices.
# Convert the list into a NumPy array.
# Print the array.

# import numpy as np
# price = [5000, 388, 85, 87, 889]
# price = np.array(price)
# print(price)
#_____________________________________________________________________________

# ==========================================
# 4. 1D Array
# ==========================================

# Ab hum 1D Array samjhenge.

# 1D ka matlab kya hai?

# 1D = One Dimensional

# Simple language mein, jab array mein values ek single
# line/sequence mein hoti hain, use 1D array bolte hain.

# Example:

# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(numbers)

# Isko visually aise samjho:

# 10   20   30   40   50

# Ye 1D array hai.

# Ek aur example
# marks = np.array([70, 80, 65, 90, 75])

# print(marks)

# Structure:

# 70   80   65   90   75

# Ye bhi 1D array hai.

# 1D Array ko identify kaise karein?

# Abhi ek simple rule:

# Single sequence → 1D Array

# Example:

# np.array([10, 20, 30])

# ✅ 1D

# Lekin:

# np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# Ye 1D nahi, ye 2D hai.

# 2D ko hum next point mein properly samjhenge.

# Important

# Abhi indexing, .ndim, .shape etc. detail mein nahi jayenge. 
# Woh apne respective roadmap topics mein aayenge.

# Practice — 3 Questions
# ==========================================
# NumPy — 1D Array
# ==========================================

# Q1. Create a 1D NumPy array containing:
# 10, 20, 30, 40, 50
# Print the array.

# import numpy as np
# number = np.array([10, 20, 30, 40, 50])
# print(number)
#---------------------------------

# Q2. Create a 1D NumPy array containing 5 student marks.
# Print the array.

# import numpy as np
# marks = np.array([70, 80, 65, 90, 75]) 
# print(marks)
#-----------------------------------------

# Q3. Create a 1D NumPy array containing 5 product prices.
# Print the array.

# import numpy as np
# price = np.array([5000, 388, 85, 87, 889])
# print(price)

#_________________________________________________________________________________________

# ==========================================
# 5.  2D ARRAY
# ==========================================

# Ab 1D ke baad 2D Array samajhte hain.

# 1D Array kya tha?

# Ek single line/sequence:

# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(numbers)

# Isme values ek hi line mein hain → 1D Array

# 2D Array kya hota hai?

# Jab data rows aur columns mein ho, to use 2D Array kehte hain.

# Example:

# import numpy as np

# numbers = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# print(numbers)

# Output:

# [[10 20 30]
#  [40 50 60]]

# Isko table ki tarah samjho:

# 10   20   30
# 40   50   60

# Yahan:

# 2 rows hain
# 3 columns hain
# Total 6 values hain

# Data Analyst mein 2D arrays ka concept useful hai kyunki 
# tabular data bhi rows aur columns mein hota hai.

# Simple rule
# Single sequence → 1D
# Rows + Columns  → 2D

# Ab isi ko practice karte hain.

# ==========================================
# NumPy — 2D Array
# ==========================================

# Q1. Create a 2D NumPy array with 2 rows and 3 columns.
# Use the values:
# 10, 20, 30
# 40, 50, 60
# Print the array.

# import numpy as np
# number = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])
# print(number)
#------------------------------

# Q2. Create a 2D NumPy array containing marks of 2 students.
# Each student should have marks for 3 subjects.
# Print the array.

# import numpy as np
# marks = np.array([
#     [70, 80, 65],
#     [69,67,89]
# ])
# print(marks)
#-----------------------------

# Q3. Create a 2D NumPy array containing product prices.
# Create 2 rows and 3 columns using any 6 product prices.
# Print the array.

# import numpy as np
# price = np.array([
#     [500,790,900],
#     [477,900,469]
# ])
# print(price)
#___________________________________________________________________________________-

# ==========================================
# 6. 3D ARRAY
# ==========================================

# 3D Array — Basic Idea

# Ab 2D ke baad 3D Array samajhte hain. Isko sirf basic level par samjhenge, 
# kyunki Data Analyst ke liye abhi iska deep use zaroori nahi hai.

# 2D Array tak kya tha?

# 2D mein:

# Row 1 → 10  20  30
# Row 2 → 40  50  60

# Yaani rows + columns.

# 3D Array kya hota hai?

# 3D Array mein multiple 2D arrays/layers hote hain.

# Example:

# import numpy as np

# data = np.array([
#     [
#         [10, 20, 30],
#         [40, 50, 60]
#     ],
#     [
#         [70, 80, 90],
#         [100, 110, 120]
#     ]
# ])

# print(data)

# Isko layers ki tarah socho:

# Layer 1
# 10   20   30
# 40   50   60


# Layer 2
# 70   80   90
# 100  110  120

# Yaani:

# 3D
#  ↓
# Multiple 2D structures
#  ↓
# Layers + Rows + Columns
# Real-life example

# Maan lo tumhare paas 2 students ke marks hain, aur har student ke
# marks 2 subjects ke 3 tests ke hain. Aise data ko 3D 
# structure mein represent kiya ja sakta hai.

# Lekin abhi indexing, shape, ndim etc. nahi karenge — 
# woh hum roadmap ke next sections mein properly seekhenge.

# Simple rule yaad rakho
# 1D → Values ki single line

# 2D → Rows + Columns

# 3D → Multiple 2D structures / Layers

# Ab 3D Array ka basic practice karte hain:

# ==========================================
# NumPy — 3D Array Basic
# ==========================================

# Q1. Create a 3D NumPy array with 2 layers.
# Each layer should contain 2 rows and 3 columns.
# Use 12 numbers of your choice.
# Print the array.

# import numpy as np
# number = np.array([
#     [
#         [10,30,30],
#         [40,50,60]
#     ],
#     [
#         [70,80,90],
#         [100,110,120]
#     ]
# ])

# print(number)

#-----------------------------------------

# Q2. Create a 3D NumPy array to represent marks
# for 2 students.
# Each student should have 2 rows and 3 marks.
# Print the array.

# import numpy as np
# marks = np.array([
#     [
#         [78,89,56],
#         [87,97,89]
#     ],
#     [
#         [78,86,98],
#         [87,56,87]
#     ]
# ])
# print(marks)

#--------------------------------------------

# Q3. Create a 3D NumPy array containing product prices
# for 2 groups.
# Each group should contain 2 rows and 3 prices.
# Print the array.

import numpy as np

price = np.array([
    [
        [30,50,78],
        [67,89,89]
    ],
    [
        [69,90,67],
        [80,56,98]
    ]
])
print(price)