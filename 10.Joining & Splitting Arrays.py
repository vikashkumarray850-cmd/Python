# ==============================
# CODE NUMBERING BY:-

# 12 TO 137 np.concatenate()
# 141 TO 244 np.vstack()
# 248 TO 313 np.hstack()
# 676 TO 876 np.split()
# ==============================

# 10: JOINING & SPLITTING ARRAYS

#==============================
# 1. np.concatenate()
#==============================

# concatenate() ka simple meaning:

# Do ya zyada arrays ko jodna (join karna).

# 1D Example
# import numpy as np

# a = np.array([10, 20, 30])
# b = np.array([40, 50, 60])

# result = np.concatenate((a, b))

# print(result)

# Output:

# [10 20 30 40 50 60]

# Yaani:

# a → [10 20 30]
# b → [40 50 60]

#        ↓ concatenate

#     [10 20 30 40 50 60]
# 2D mein axis important hota hai

# Do arrays:

# a = np.array([
#     [10, 20],
#     [30, 40]
# ])

# b = np.array([
#     [50, 60],
#     [70, 80]
# ])
# axis=0
# np.concatenate((a, b), axis=0)

# Arrays upar-niche join honge:

# [[10 20]
#  [30 40]
#  [50 60]
#  [70 80]]

# Yaani rows add hui.

# axis=1
# np.concatenate((a, b), axis=1)

# Arrays left-right join honge:

# [[10 20 50 60]
#  [30 40 70 80]]

# Yaani columns side mein add hue.

# Simple trick
# axis=0 → ऊपर-नीचे join
# axis=1 → side-by-side join

# Ye axis=0/1 ke concept se connected hai jo tum already kar chuke ho. 👍

# Practice — np.concatenate()
# ==========================================
# NumPy — np.concatenate() Practice
# ==========================================

# Q1. Create two 1D NumPy arrays:
# [10, 20, 30]
# [40, 50, 60]
#
# Join both arrays using np.concatenate().
# Print the result.

# import numpy as np
# a = np.array([10, 20, 30])
# b = np.array([40, 50, 60])
# result = np.concatenate((a,b))
# print(result)
#----------------------------------------

# Q2. Create these two 2D NumPy arrays:
#
# Array A:
# [[10, 20],
#  [30, 40]]
#
# Array B:
# [[50, 60],
#  [70, 80]]
#
# Join them vertically using np.concatenate() with axis=0.
# Print the result.

# import numpy as np
# a = np.array([
#     [10, 20],
#     [30, 40]
# ])
# b = np.array([
#     [50, 60],
#     [70, 80]
# ])
# result = np.concatenate((a,b), axis=0)
# print(result)
#---------------------------------------------------

# Q3. Create the same two 2D NumPy arrays.
#
# Join them horizontally using np.concatenate() with axis=1.
# Print the result.

# import numpy as np
# x = np.array([
#     [10, 20],
#     [30, 40]
# ])
# y = np.array([
#     [50, 60],
#     [70, 80]
# ])
# result = np.concatenate((x,y), axis=1)
# print(result)
#______________________________________________________________________________________________________

#==============================
# 2. np.vstack()
#==============================
# np.vstack() kya karta hai?

# vstack = vertical stack

# Simple meaning:

# Do arrays ko upar-niche (vertically) jodna.

# Example:

# import numpy as np

# a = np.array([
#     [10, 20],
#     [30, 40]
# ])

# b = np.array([
#     [50, 60],
#     [70, 80]
# ])

# result = np.vstack((a, b))

# print(result)

# Output:

# [[10 20]
#  [30 40]
#  [50 60]
#  [70 80]]

# Visual:

# A:
# [10 20]
# [30 40]

#       ↓ vstack

# B:
# [50 60]
# [70 80]

#       ↓

# [10 20]
# [30 40]
# [50 60]
# [70 80]
# concatenate() se relation

# Jo kaam humne pehle kiya tha:

# np.concatenate((a, b), axis=0)

# Uska similar result:

# np.vstack((a, b))

# Dono mein arrays upar-niche join hote hain.

# Important

# vstack() mein axis dene ki zarurat nahi hoti.

# np.vstack((a, b))

# Bas itna.

# Practice
# ==========================================
# NumPy — np.vstack() Practice
# ==========================================

# Q1. Create these two 2D NumPy arrays:
#
# A:
# [[10, 20],
#  [30, 40]]
#
# B:
# [[50, 60],
#  [70, 80]]
#
# Join them vertically using np.vstack().
# Print the result.

# import numpy as np
# a = np.array([
#     [10, 20],
#     [30, 40]
# ])
# b = np.array([
#     [50, 60],
#     [70, 80]
# ])
# result = np.vstack((a,b))
# print(result)
#--------------------------------------------

# Q2. Create these two 2D NumPy arrays:
#
# A:
# [[100, 200, 300]]
#
# B:
# [[400, 500, 600]]
#
# Join them vertically using np.vstack().
# Print the result.

# import numpy as np
# x = np.array([
#     [100, 200, 300]
# ])
# y = np.array([
#     [400, 500, 600]
# ])
# result = np.vstack((x,y))
# print(result)
#------------------------------------

# Q3. Create these two 2D NumPy arrays:
#
# A:
# [[1, 2],
#  [3, 4]]
#
# B:
# [[5, 6],
#  [7, 8]]
#
# Join them vertically using np.vstack().
# Print the result.

# import numpy as np
# x = np.array([
#     [1, 2],
#     [3, 4]
# ])
# y = np.array([
#     [5, 6],
#     [7, 8]
# ])
# result = np.vstack((x,y))
# print(result)
#___________________________________________________________________________________________________

#==============================
# 3. np.hstack()
#==============================
# np.hstack() kya hai?

# hstack = Horizontal Stack

# Matlab arrays ko left-right / side-by-side join karna.

# import numpy as np

# a = np.array([
#     [10, 20],
#     [30, 40]
# ])

# b = np.array([
#     [50, 60],
#     [70, 80]
# ])

# result = np.hstack((a, b))

# print(result)

# Output:

# [[10 20 50 60]
#  [30 40 70 80]]

# Yahan dekho:

# A              B

# 10  20         50  60
# 30  40         70  80

#        ↓ hstack

# 10  20  50  60
# 30  40  70  80
# hstack aur concatenate(axis=1)

# Dono ka result same ho sakta hai:

# np.hstack((a, b))

# same as:

# np.concatenate((a, b), axis=1)

# Simple rule yaad rakho:

# vstack → upar-niche → rows add
# hstack → left-right → columns add
# Practice — np.hstack()
# ==========================================
# NumPy — np.hstack() Practice
# ==========================================

# Q1. Create two 2D NumPy arrays:
# A = [[10, 20],
#      [30, 40]]
#
# B = [[50, 60],
#      [70, 80]]
#
# Use np.hstack() to join them horizontally.
# Print the result.

# import numpy as np
# A = np.array([
#     [10, 20],
#     [30, 40]
# ])

# B = np.array([
#     [50, 60],
#     [70, 80]
# ])
# result = np.hstack((A,B))
# print(result)

#---------------------------------------------

# Q2. Create two 2D NumPy arrays:
# A = [[100, 200, 300],
#      [400, 500, 600]]

# B = [[700, 800],
#      [900, 1000]]
#
# Use np.hstack() to join them horizontally.
# Print the result.

# import numpy as np
# A = np.array([
#     [100, 200, 300],
#     [400, 500, 600]
# ])

# B = np.array([
#     [700, 800],
#     [900, 1000]
# ])
# result = np.hstack((A,B))
# print(result)
#------------------------------------
# Q3. Create two 2D NumPy arrays:
# A = [[1],
#      [2],
#      [3]]
#
# B = [[4],
#      [5],
#      [6]]
#
# Use np.hstack() to join them horizontally.
# Print the result.

# import numpy as np
# A = np.array([
#     [1],
#     [2],
#     [3]
# ])

# B = np.array([
#     [4],
#     [5],
#     [6]
# ])
# result = np.hstack((A,B))
# print(result)
#_____________________________________________________________________________________________________

