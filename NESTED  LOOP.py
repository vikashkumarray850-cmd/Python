# ==========================================
# NESTED LOOPS - PRACTICE QUESTIONS
# ==========================================


# Q1. Easy
# Use nested loops to print the following:
#
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

# for i in range(1, 4):
#     for j in range(1,4):
#         print(i , j)
#------------------------------------------------------------------------------
# Q2. Easy
# Use nested loops to print a 3 × 4 rectangle
# of stars.
#
# Expected Output:
# * * * *
# * * * *
# * * * *

# for i in range(3):
#     for j in range(4):
#         print("*", end=" ")
#     print()
#-----------------------------------------------------------------

# Q3. Medium
# Use nested loops to print the multiplication
# tables from 2 to 5.
#
# Example:
# 2 * 1 = 2
# 2 * 2 = 4
# ...
# 2 * 10 = 20
#
# Then print the table of 3, 4 and 5.

# for i in range(2, 6):          # Outer loop → 2, 3, 4, 5
#     for j in range(1, 11):     # Inner loop → 1 to 10
#         print(i, "*", j, "=", i * j)
#---------------------------------------------------------------------------

# Q4. Medium
# Use nested loops to print this pattern:
#
# 1
# 12
# 123
# 1234
# 12345

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()

# Q5. Practical
# There are 3 departments.
# Each department has 3 employees.
#
# Use nested loops to print:
#
# Department 1 - Employee 1
# Department 1 - Employee 2
# Department 1 - Employee 3
# Department 2 - Employee 1
# Department 2 - Employee 2
# Department 2 - Employee 3
# Department 3 - Employee 1
# Department 3 - Employee 2
# Department 3 - Employee 3

# for i in range (1,4):
#     for j in range(1,4):
#         print(f"Department {i} - Employee {j}"