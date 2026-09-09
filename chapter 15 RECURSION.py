
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

# ============================================
# RECURSION PRACTICE SET - 1
# Rules: Sirf recursion use karna hai, loop (for/while) nahi
# Har function mein base case zaroor hona chahiye
# ============================================


# Q1. Ek function banao print_hi(n) jo n baar "Hi" print kare
# Example: print_hi(4)
# Output:
# Hi
# Hi
# Hi
# Hi

def print_hi(n):
    if n == 0:
        return
    print("hi")
    print_hi(n - 1)
print(5)


# Q2. Ek function banao count_down(n) jo n se 1 tak numbers print kare (ulta)
# phir last mein "Liftoff!" print kare
# Example: count_down(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# Liftoff!


    


# Q3. Ek function banao count_up(n) jo 1 se n tak numbers print kare (seedha order)
# Example: count_up(4)
# Output:
# 1
# 2
# 3
# 4
# Hint: print aur recursive call ka order badalna padega




# Q4. Ek function banao print_even(n) jo 1 se n tak sirf EVEN numbers print kare
# Example: print_even(10)
# Output:
# 2
# 4
# 6
# 8
# 10




# Q5. (Thoda tricky) Ek function banao star_pattern(n) jo yeh pattern print kare
# Example: star_pattern(4)
# Output:
# *
# **
# ***
# ****




# ============================================
# YAHA NEECHE APNE FUNCTIONS KO CALL KARKE TEST KARO
# ============================================

# print("---- Q1 ----")
# print_hi(4)

# print("---- Q2 ----")
# count_down(5)

# print("---- Q3 ----")
# count_up(4)

# print("---- Q4 ----")
# print_even(10)

# print("---- Q5 ----")
# star_pattern(4)















