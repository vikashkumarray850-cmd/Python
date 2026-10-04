# ==========================================
# CODE NUMBERING BY:-

# 11 TO 86 1D Array Indexing
# 89 TO 165 2D Array Indexing
# 168 TO 288 Row Selection 
# 291 TO 404 Column Selection
# 408 TO 561 Array Slicing
# ==========================================

# ==========================================
# 1. 1D Array Indexing 
# ==========================================

# Indexing ka matlab hai array ke andar kisi specific element ko access karna.

# Python ki tarah NumPy mein bhi indexing 0 se start hoti hai.

# Example:

# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(numbers[0])
# print(numbers[1])
# print(numbers[2])

# Output:

# 10
# 20
# 30

# Array ko index ke saath dekho:

# Value:   10   20   30   40   50
# Index:    0    1    2    3    4
# Last element

# Negative indexing bhi Python jaisi hi hai:

# print(numbers[-1])

# Output:

# 50
# -1 → last value
# -2 → second-last value
# Important
# numbers[0]  → first element
# numbers[1]  → second element
# numbers[2]  → third element
# numbers[-1] → last element

# Ab 3 practice questions:

# ==========================================
# NumPy — 1D Array Indexing
# ==========================================

# Q1. Create a NumPy array:
# [10, 20, 30, 40, 50]
# Print the first element.

# import numpy as np
# number = np.array([10,20,30,40,50])
# print(number[0])
#----------------------------------

# Q2. Create a NumPy array:
# [100, 200, 300, 400, 500]
# Print the third element.

# import numpy as np
# number = np.array([100, 200, 300, 400, 500])
# print(number[2])
#-------------------------------------

# Q3. Create a NumPy array:
# [5, 10, 15, 20, 25]
# Print the last element using negative indexing.

# import numpy as np
# number = np.array([5, 10, 15, 20, 25])
# print(number[-1])
#___________________________________________________________________________________________________

# ==========================================
# 2. 2D Array Indexing 
# ==========================================

# 2D array mein kisi ek value ko access karne ke liye:

# array[row_index, column_index]

# Dono index 0 se start hote hain.

# Example:

# import numpy as np

# numbers = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# print(numbers[0, 0])  # 10
# print(numbers[0, 2])  # 30
# print(numbers[1, 1])  # 50

# Is array ko aise samjho:

#         col0  col1  col2
# row0     10    20    30
# row1     40    50    60

# So numbers[1, 1] ka matlab:

# row 1 → second row
# column 1 → second column
# result → 50

# Practice
# ==========================================
# NumPy — 2D Array Indexing
# ==========================================

# Q1. Create a 2D NumPy array:
# [[10, 20, 30],
#  [40, 50, 60]]
# Print the value 20 using indexing.

# import numpy as np
# number = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])
# print(number[0, 1])
#---------------------------------------

# Q2. Create a 2D NumPy array:
# [[100, 200, 300],
#  [400, 500, 600]]
# Print the value 600 using indexing.

# import numpy as np
# number = np.array([
#     [100, 200, 300],
#     [400, 500, 600]
# ])
# print(number[1,2])
#-------------------------------------

# Q3. Create a 2D NumPy array:
# [[5, 10, 15],
#  [20, 25, 30]]
# Print the value 25 using indexing.

# import numpy as np
# number = np.array([
#     [5, 10, 15],
#     [20, 25, 30]
# ])
# print(number[1,1])
#_________________________________________________________________________________________________

# ====================
# 3. Row Selection
# ====================

# 2D array mein agar humein poori ek row nikalni ho, to hum row ka index dete hain.

# Syntax:

# array[row_index]

# Example:

# import numpy as np

# numbers = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# print(numbers[0])

# Output:

# [10 20 30]

# Yahan:

# row 0 → [10 20 30]
# row 1 → [40 50 60]
# row 2 → [70 80 90]

# Isliye:

# numbers[0]

# ka matlab hai poori first row.

# Second row
# print(numbers[1])

# Output:

# [40 50 60]
# Third row
# print(numbers[2])

# Output:

# [70 80 90]
# Important difference

# Abhi tak humne specific value nikali thi:

# numbers[1, 2]

# Output:

# 60

# Yahan hum poori row nikal rahe hain:

# numbers[1]

# Output:

# [40 50 60]

# So simple rule:

# Specific value → array[row, column]

# Complete row → array[row]
# Practice
# ==========================================
# NumPy — Row Selection
# ==========================================

# Q1. Create a 2D NumPy array:
# [[10, 20, 30],
#  [40, 50, 60],
#  [70, 80, 90]]
# Print the first row.

# import numpy as np
# number = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])
# print(number[0])
#-----------------------------------------

# Q2. Create a 2D NumPy array:
# [[100, 200, 300],
#  [400, 500, 600],
#  [700, 800, 900]]
# Print the second row.

# import numpy as np
# number = np.array([
#     [100, 200, 300],
#     [400, 500, 600],
#     [700, 800, 900]
# ])
# print(number[1])
#___---------------------------

# Q3. Create a 2D NumPy array:
# [[5, 10, 15],
#  [20, 25, 30],
#  [35, 40, 45]]
# Print the third row.

# import numpy as np
# number = np.array([
#     [5, 10, 15],
#     [20, 25, 30],
#     [35, 40, 45]
# ])
# print(number[2])
#_______________________________________________________________________________________________

# ==========================================
# 4. Column Selection
# ==========================================

# 2D NumPy array se poora column nikalne ke liye hum 
# : use karte hain.

# Syntax:

# array[:, column_index]

# Yahan:

# : → saari rows
# column_index → jis column ko select karna hai

# Example:

# import numpy as np

# numbers = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# print(numbers[:, 0])

# Output:

# [10 40 70]

# Kyunki column 0 hai:

#         col0  col1  col2
# row0     10    20    30
# row1     40    50    60
# row2     70    80    90
#          ↑
#        column 0
# Column 1
# print(numbers[:, 1])

# Output:

# [20 50 80]
# Column 2
# print(numbers[:, 2])

# Output:

# [30 60 90]
# Important difference

# Ab tak:

# numbers[1]       # complete row
# numbers[:, 1]    # complete column
# numbers[1, 1]    # one specific value

# Yaad rakhne ka simple rule:

# Row    → [row]
# Column → [:, column]
# Value  → [row, column]

# Practice
# ==========================================
# NumPy — Column Selection
# ==========================================

# Q1. Create a 2D NumPy array:
# [[10, 20, 30],
#  [40, 50, 60],
#  [70, 80, 90]]
# Print the first column.

# import numpy as np
# number = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])
# print(number[:,0])
#----------------------

# Q2. Create a 2D NumPy array:
# [[100, 200, 300],
#  [400, 500, 600],
#  [700, 800, 900]]
# Print the second column.

# import numpy as np
# number = np.array([
#     [100, 200, 300],
#     [400, 500, 600],
#     [700, 800, 900]
# ])
# print(number[:,1])
#------------------------------

# Q3. Create a 2D NumPy array:
# [[5, 10, 15],
#  [20, 25, 30],
#  [35, 40, 45]]
# Print the third column.

# import numpy as np
# number = np.array([
#     [5, 10, 15],
#     [20, 25, 30],
#     [35, 40, 45]
# ])
# print(number[:,2])
#___________________________________________________________________________________________

# ==========================================
# 5. Array Slicing
# ==========================================

# Slicing ka matlab hai array ke ek part/range ko select karna.

# 1D Array mein basic slicing

# Syntax:

# array[start:stop]

# Important:

# start → yahan se start
# stop → yahan tak, lekin stop index include nahi hota

# Example:

# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(numbers[1:4])

# Output:

# [20 30 40]

# Kyun?

# Index:     0   1   2   3   4
# Value:    10  20  30  40  50
#                ↑       ↑
#              start    stop

# 1:4 means index 1, 2, 3.

# Isliye:

# 20, 30, 40
# Start nahi dena
# print(numbers[:3])

# Output:

# [10 20 30]

# Matlab beginning se index 3 se pehle tak.

# Stop nahi dena
# print(numbers[2:])

# Output:

# [30 40 50]

# Matlab index 2 se end tak.

# 2D Array Slicing

# 2D array mein slicing thodi interesting hai.

# Basic syntax:

# array[row_start:row_stop, column_start:column_stop]

# Example:

# import numpy as np

# numbers = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# print(numbers[0:2, 1:3])

# Output:

# [[20 30]
#  [50 60]]

# Yahan:

# 0:2 → row 0 aur row 1
# 1:3 → column 1 aur column 2

# So:

# Original:

#         col0  col1  col2
# row0     10    20    30
# row1     40    50    60
# row2     70    80    90

# Selected:

#               ↓     ↓
# row0          20    30
# row1          50    60
# Sabse important rule
# 1D:
# array[start:stop]

# 2D:
# array[row_start:row_stop, column_start:column_stop]

# Aur stop index include nahi hota.

# Practice
# ==========================================
# NumPy — Array Slicing
# ==========================================

# Q1. Create a 1D NumPy array:
# [10, 20, 30, 40, 50, 60]
# Print the values from index 1 up to index 5.

# import numpy as np
# number =([10, 20, 30, 40, 50, 60])
# print(number[1:5])
#-------------------------------------------

# Q2. Create a 2D NumPy array:
# [[10, 20, 30],
#  [40, 50, 60],
#  [70, 80, 90]]
# Select the first two rows and the last two columns.

# import numpy as np
# number = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# print(number[0:2, 1:3])
#-----------------------------------

# Q3. Create a 2D NumPy array:
# [[100, 200, 300, 400],
#  [500, 600, 700, 800],
#  [900, 1000, 1100, 1200]]
# Select the last two rows and the middle two columns.

# import numpy as np
# number = np.array([
#     [100, 200, 300, 400],
#     [500, 600, 700, 800],
#     [900, 1000, 1100, 1200]
# ])
# print(number[1:3, 1:3 ])