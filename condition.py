age = int(input("Enter your age: "))

# agar > 100 : "Invalid Age"
# agar > 18 : "You can vote"
# else : "You cann't vote"

if age > 100:
    print("Invalid age")
elif age > 18:
    print("You can vote")
else:
    print("You can't vote")


print("Invalid age") if age > 100 else  print("You can vote") if age > 18 else print("You can't vote")



# Nested Condition

# agar aj barish hua:
    # agar bijli vi hai:
        # mummy vi bahar gayi:
            # 1. "party mode on"
        # 2. sirf game khelenge
    # so jayenge
# nhi to:
    # ofiice....

# barish = bool(int(input("Barish ho raha hai? [0/1]:  ")))
# if barish:
#     bijli_available = bool(int(input("bijli hai? [0/1]:  ")))
#     if bijli_available:
#         mummy_available = bool(int(input("mummy hai? [0/1]:  ")))
#         if mummy_available:
#             print("Pura din game mode on")
#         else:
#             print("Party mode on")
#     else:
#         print("so jaunga")
# else:
#     print("Office jao.........")



# marks= int(input("Enter your marks: "))
# attendence = int(input("Enter attendence %: "))
# family_income = float(input("Enter Family income: "))

# if marks >= 90:
#     if attendence >= 85 and family_income < 300000:
#         print("Full Scholarship")
#     else:
#         print("50% Scholarship")
# elif marks > 80:
#     if attendence >= 90 and family_income < 200000:
#         print("25% Scholarship")
#     else:
#         print("5% Scholarship")
# else:
#     print("Not Eligible!")


