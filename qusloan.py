# # Input:

# # Salary
# # Credit Score
# # Existing Loan
# # Age
# # Rules:

# # Salary ≥50000
# # Credit Score ≥750
# # Existing Loan = No
# # Age between 21 and 60
# # Loan Approved
# # Else print exact rejection reason.

# salary = float(input("enter your salary:"))
# credit_score = int(input("enter credit score:"))
# existing_loan = input("Existing Loan (Yes/No): ")
# age = int(input("Enter Age: "))

# if salary >= 50000:
#     if credit_score >= 700 and existing_loan == "No":
#         print("Loan Approved")
#     else:
#         print("Loan Approved with Term & Conditions")

# elif salary >= 30000:
#     if credit_score >= 650 and age >= 21:
#         print("Loan Review")
#     else:
#         print("Loan Rejected")

# else:
#     print("Loan Rejected")


# Input:

# City
# Stock Available
# Prime Member
# Weather

# Rules:

# Stock Available
# Same City
# Prime
# Same Day
# Normal
# Next Day
# Different City
# Weather Clear
# 2 Days
# Rain
# 4 Days

# city = input("City (Same/Different): ")
# stock = input("Stock Available (Yes/No): ")
# prime = input("Prime Member (Yes/No): ")
# weather = input("Weather (Clear/Rain): ")

# if stock == "Yes":
#     if city == "Same":
#         if prime == "Yes":
#             print("Delivery: Same Day")
#         else:
#             print("Delivery: Next Day")
#     else:
#         if weather == "Clear":
#             print("Delivery: 2 Days")
#         else:
#             print("Delivery: 4 Days")
# else:
#     print("Out of Stock")

#     Input:

# Ambulance Present
# Vehicle Count
# Rain

# Rules:

# Ambulance
# Green Immediately
# Else
# Vehicles >100
# Rain
# Green 90 sec
# No Rain
# Green 60 sec
# Else Normal Timing

# ambulance = input("Ambulance Present (Yes/No): ")
# vehicle_count = int(input("Vehicle Count: "))
# rain = input("Rain (Yes/No): ")

# if ambulance == "Yes":
#     print("Green Immediately")
# else:
#     if vehicle_count > 100:
#         if rain == "Yes":
#             print("Green 90 sec")
#         else:
#             print("Green 60 sec")
#     else:
#         print("Normal Timing")

# Input:

# Age
# Heart Rate
# Oxygen Level
# Temperature

# Rules:

# Oxygen <90
# Heart Rate >120
# ICU
# Else
# Emergency Ward
# Oxygen 90-95
# Fever >102
# Observation
# Otherwise Normal Ward

age = int(input("Age: "))
heart_rate = int(input("Heart Rate: "))
oxygen = int(input("Oxygen Level: "))
temperature = float(input("Temperature: "))

if oxygen < 90:
    if heart_rate > 120:
        print("ICU")
    else:
        print("Emergency Ward")
elif oxygen >= 90 and oxygen <= 95:
    if temperature > 102:
        print("Observation")
    else:
        print("Normal Ward")
else:
    print("Normal Ward")