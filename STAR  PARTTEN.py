# ==========================================
# STAR PATTERNS - PRACTICE QUESTIONS
# ==========================================


# Q1. Basic Triangle
# Print the following pattern:
#
# *
# **
# ***
# ****
# *****
#
# Use nested loops.

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end = "")
#     print()
#----------------------------------------------------------
# Q2. Inverted Triangle
# Print the following pattern:
#
# *****
# ****
# ***
# **
# *
#
# Use nested loops.

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()
#--------------------------------------------------------
# Q3. Square Pattern
# Print a 5 × 5 square:
#
# *****
# *****
# *****
# *****
# *****
#
# Use nested loops

# for i in range (5):
#     for j in range(5):
#         print("*", end="")
#     print()
#-----------------------------------------------------------------------
# Q4.
# Print the following pattern:
#
# 1
# 12
# 123
# 1234
# 12345
#
# Use nested loops.

# for i in range (1, 6):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
#----------------------------------------------------------------------
# Q5. Increasing Star Pattern
# Take the number of rows from the user.
# Print a star triangle based on that number.
#
# Example:
# Input: 4
#
# Output:
# *
# **
# ***
# ****
#
# Input: 6
#
# Output:
# *
# **
# ***
# ****
# *****

# rows = int(input("Enter number of rows: "))

# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()

# ==========================================
# STAR PATTERNS - PRACTICE SET 2
# ==========================================


# Q6. Right-Aligned Triangle
# Take the number of rows from the user.
# Print a right-aligned star triangle.
#
# Example:
# Input: 5
#
# Output:
#     *
#    **
#   ***
#  ****
# *****

# rows = int(input("Enter number of rows: "))

# for i in range(1, rows + 1):
#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")
#     # Print stars
#     for j in range(i):
#         print("*", end="")
#-------------------------------------------------------------------------
# Q7.
# Take the number of rows from the user.
# Print an inverted right-aligned triangle.
#
# Example:
# Input: 5
#
# Output:
# *****
#  ****
#   ***
#    **
#     *

# rows = int(input("Enter number of rows: "))

# for i in range(rows, 0, -1):

#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")

#     # Print stars
#     for j in range(i):
#         print("*", end="")

#     print()
#--------------------------------------------------------------------

# Q8. Pyramid Pattern
# Take the number of rows from the user.
# Print a centered pyramid.
#
# Example:
# Input: 5
#
# Output:
#     *
#    ***
#   *****
#  *******
# *********
# rows = int(input("Enter number of rows: "))

# for i in range(1, rows + 1):

#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")

#     # Print stars
#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()

# Q9.
# Take the number of rows from the user.
# Print an inverted centered pyramid.
#
# Example:
# Input: 5
#
# Output:
# *********
#  *******
#   *****
#    ***
#     *

# rows = int(input("Enter number of rows: "))

# for i in range(rows, 0, -1):

#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")

#     # Print stars
#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()


# Q10.
# Take the number of rows from the user.
# Print a diamond pattern.
#
# Example:
# Input: 5
#
# Output:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# rows = int(input("Enter number of rows: "))

# # Upper half
# for i in range(1, rows + 1):

#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")

#     # Print stars
#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()

# # Lower half
# for i in range(rows - 1, 0, -1):

#     # Print spaces
#     for j in range(rows - i):
#         print(" ", end="")

#     # Print stars
#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()
