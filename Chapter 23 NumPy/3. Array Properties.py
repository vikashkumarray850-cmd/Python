# ==========================================
# CODE NUMBERING BY:-

# 10 TO 112 (.ndim)
# 124 TO 228 (.shape)
# 231 TO 326 (.size) 
# 330 TO 407 (.dtype)
# ==========================================

# ==========================================
# 1. NumPy — Array Properties: .ndim
# ==========================================
# Array Properties start karte hain.

# Is section mein hum array ke baare mein information nikalna seekhenge:

# .ndim
# .shape
# .size
# .dtype

# Aaj pehle .ndim samajhte hain.

# .ndim kya karta hai?

# .ndim batata hai ki array mein kitni dimensions hain.

# Example:

# import numpy as np

# numbers = np.array([10, 20, 30, 40])

# print(numbers.ndim)

# Output:

# 1

# Kyuki ye 1D Array hai.

# 2D example
# numbers = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# print(numbers.ndim)

# Output:

# 2

# Kyuki ye 2D Array hai.

# 3D example
# numbers = np.array([
#     [
#         [10, 20, 30],
#         [40, 50, 60]
#     ],
#     [
#         [70, 80, 90],
#         [100, 110, 120]
#     ]
# ])

# print(numbers.ndim)

# Output:

# 3
# Simple rule
# 1D Array → ndim = 1
# 2D Array → ndim = 2
# 3D Array → ndim = 3

# Yaani .ndim ka kaam hai array ki dimension count karna.

# Ab 3 practice questions:

# ==========================================
# NumPy — Array Properties: .ndim
# ==========================================

# Q1. Create a 1D NumPy array with 5 numbers.
# Print the number of dimensions using .ndim.

# import numpy as np
# number = np.array([20,30,40,50,60])
# print(number.ndim)
#----------------------------------------

# Q2. Create a 2D NumPy array with 2 rows and 3 columns.
# Print the number of dimensions using .ndim.

# import numpy as np
# number = np.array([
#     [100,200,300],
#     [400,500,600]
# ])
# print(number.ndim)
#------------------------------------

# Q3. Create a 3D NumPy array with 2 layers,
# 2 rows, and 3 columns.
# Print the number of dimensions using .ndim.

# import numpy as np

# number = np.array([
#     [
#         [300,400,500],
#         [600,700,800]
#     ],
#     [
#         [900,1100,1200],
#         [1300,1400,1500]
#     ]
# ])
# print(number.ndim)
#__________________________________________________________________________________________-

# ==========================================
# # 2 .shape
# ==========================================

# .shape ka use karke hum pata karte hain ki array mein kitni rows aur columns hain.

# Example 2D array:

# import numpy as np

# numbers = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# print(numbers.shape)

# Output:

# (2, 3)

# Iska matlab:

# 2 → rows
# 3 → columns

# So:

# .shape → (rows, columns)

# 1D Array mein
# numbers = np.array([10, 20, 30, 40, 50])

# print(numbers.shape)

# Output:

# (5,)

# Matlab 5 values hain.

# 3D Array mein

# Agar:

# 2 layers
# 2 rows
# 3 columns

# to:

# print(numbers.shape)

# Output hoga:

# (2, 2, 3)

# Yaani:

# 2 → layers
# 2 → rows
# 3 → columns

# Ab practice karo:

# ==========================================
# NumPy — Array Properties: .shape
# ==========================================

# Q1. Create a 1D NumPy array with 5 numbers.
# Print its shape using .shape.

# import numpy as np
# number = np.array([20,30,40,50,60])
# print(number.shape)
#-----------------------------------

# Q2. Create a 2D NumPy array with 3 rows and 4 columns.
# Print its shape using .shape.

# import numpy as np
# number = np.array([
#     [100,200,300],
#     [400,500,600]
# ])
# print(number.shape)
#----------------------------------------

# Q3. Create a 3D NumPy array with 2 layers,
# 2 rows, and 3 columns.
# Print its shape using .shape.

# import numpy as np

# number = np.array([
#     [
#         [300,400,500],
#         [600,700,800]
#     ],
#     [
#         [900,1100,1200],
#         [1300,1400,1500]
#     ]
# ])
# print(number.shape)
#___________________________________________________________________________________________________--

# ==========================================
# 3 .size
# ==========================================

# .size batata hai ki array ke andar total kitni values/elements hain.

# 1D Array
# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(numbers.size)

# Output:

# 5

# Kyuki total 5 values hain.

# 2D Array
# numbers = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])

# print(numbers.size)

# Output:

# 6

# Yahan:

# 2 rows × 3 columns = 6 values
# 3D Array

# Agar array mein:

# 2 layers × 2 rows × 3 columns

# to total values:

# 2 × 2 × 3 = 12
# print(numbers.size)

# Output:

# 12
# Simple difference
# .ndim  → kitni dimensions?
# .shape → structure kya hai?
# .size  → total kitni values?

# Ab 3 practice questions:

# ==========================================
# NumPy — Array Properties: .size
# ==========================================

# Q1. Create a 1D NumPy array with 6 numbers.
# Print the total number of elements using .size.

# import numpy as np
# number = np.array([20,30,40,50,60,70])
# print(number.size)
#-----------------------------------------------

# Q2. Create a 2D NumPy array with 3 rows and 4 columns.
# Print the total number of elements using .size.

# import numpy as np
#number = np.array([
#     [100,200,300,400],
#     [400,500,600,700],
#     [800,900,1000,1100]
# ])
# print(number.size)
#----------------------------------------------

# Q3. Create a 3D NumPy array with 2 layers,
# 2 rows, and 3 columns.
# Print the total number of elements using .size.

# import numpy as np

# number = np.array([
#     [
#         [300,400,500],
#         [600,700,800]
#     ],
#     [
#         [900,1100,1200],
#         [1300,1400,1500]
#     ]
# ])
# print(number.size)

#_____________________________________________________________________________________________

# ==========================================
#4 .dtype
# ==========================================

# .dtype batata hai ki NumPy array ke andar values ka data type kya hai.

# Example:

# import numpy as np

# numbers = np.array([10, 20, 30, 40])

# print(numbers.dtype)

# Output generally:

# int64

# Matlab array ke andar integer values hain.

# Decimal values
# prices = np.array([10.5, 20.5, 30.5])

# print(prices.dtype)

# Output generally:

# float64

# Matlab values decimal/float hain.

# Text values
# names = np.array(["Vikash", "Mohit", "Ravi"])

# print(names.dtype)

# Is case mein NumPy string type dikhayega, jaise:

# <U6

# Exact string dtype output system/version ke according vary kar sakta hai.

# Simple rule
# int values    → integer dtype
# decimal values → float dtype
# text values   → string dtype

# Data Analysis mein .dtype useful hai kyunki data ka 
# type check karna important hota hai.

# Ab practice:

# ==========================================
# NumPy — Array Properties: .dtype
# ==========================================

# Q1. Create a NumPy array containing 5 integer values.
# Print its data type using .dtype.

# import numpy as np
# number = np.array([10, 20, 30, 40, 50])
# print(number.dtype)
#------------------------------------------------

# Q2. Create a NumPy array containing 5 decimal values.
# Print its data type using .dtype.

# import numpy as np
# number = np.array([10.5, 20.5, 30.5, 40.5, 50.5])
# print(number.dtype)
#-------------------------------------------------------

# Q3. Create a NumPy array containing 3 names.
# Print its data type using .dtype.

# import numpy as np
# name = np.array(["Vikash", "Rojit", "Vinit"])
# print(name.dtype)