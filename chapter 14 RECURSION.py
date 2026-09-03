
# Recursion ka simple meaning hai:

# Ek function apne aap ko hi call karta hai.

# Example:

# def count(n):
#     if n == 0:
#         return

#     print(n)
#     count(n - 1)

# count(5)

# Output:

# 5
# 4
# 3
# 2
# 1

# Yahan:

# count(5)
#    ↓
# count(4)
#    ↓
# count(3)
#    ↓
# count(2)
#    ↓
# count(1)
#    ↓
# count(0) → stop
# Recursion mein 2 cheezein important hain

# 1. Base Condition
# Function ko batati hai kab rukna hai.

# if n == 0:
#     return

# 2. Recursive Call
# Function apne aap ko call karta hai.

# count(n - 1)

# Agar base condition nahi hogi, function continuously khud ko call karta rahega.