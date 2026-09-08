# ==========================================
# Python Functions — Local & Global Scope
# ==========================================


# Q1. Local Variable
# Create a function named show_details().
# Create a variable inside the function.
# Print the variable inside the function.
# Call the function.

# def show_details():

#     name ="vikash"
#     print(name)
# show_details()

# Q2. Global Variable
# Create a variable outside a function.
# Create a function that prints that variable.
# Call the function.
# name = "vikash"
# def show():
#     print(name)

# show()

# Q3. Local vs Global
# Create a variable outside a function.
# Inside the function, create another variable with the same name.
# Print the variable inside the function and then outside the function.
# Observe both outputs.

# name = "vikash"

# def show_deatils():
#     name = "vikash"
#     print(name)

# show_deatils()
# print(name)


# Q4. Global Keyword
# Create a salary variable outside a function.
# Create a function that changes its value.
# Use the appropriate keyword so that the original global variable is changed.
# Call the function and print the salary.

# salary = 25000

# def update():
#     global salary
#     salary = 30000
# update()
# print(salary)

# Q5. Local Calculation
# Create a function that takes price and quantity.
# Create a total variable inside the function.
# Calculate and print the total.
# Try to access total outside the function and observe what happens.

# def details():
#     price = 500
#     quantity = 5

#     total = price * quantity
#     print(total)

# details()

# ==========================================
# Python Functions — Global Update & Calculation Practice
# ==========================================


# Q1. Global Variable Update
# Create a salary variable outside the function.
# Create a function named update_salary().
# Change the salary inside the function.
# Use the required keyword to update the global variable.
# Call the function and print the salary.

# salary = 25000

# def update_salary():
#     global salary
#     salary = 30000

# update_salary()
# print(salary)

# Q2. Global Variable Calculation
# Create price and quantity variables outside the function.
# Create a function named calculate_total().
# Calculate the total inside the function.
# Print the result inside the function.
# Call the function.

# price = 500
# quantity = 5
# def calculate_total():

#     total = price * quantity
#     print(total)

# calculate_total()


# Q3. Update + Calculation
# Create a global salary variable.
# Create a function named update_salary().
# Increase the salary by 5000 inside the function.
# Update the global salary and print the new salary.
# Call the function.

# salary = 30000

# def update_salary():
#     global salary
#     salary = salary + 5000
#     print(salary)

# update_salary()


# Q4. Global Variables + Calculation
# Create global variables price and delivery_charge.
# Create a function named final_amount().
# Calculate the final amount using both variables.
# Print the final amount.
# Call the function.

# price = 500
# delivery_charge = 50

# def final_amount():
#     total = price + delivery_charge

#     print(total)
# final_amount()


# Q5. Update + Calculation
# Create a global variable balance.
# Create a function named withdraw().
# Subtract an amount from the balance.
# Update the global balance.
# Print the updated balance.
# Call the function.

# balance = 10000

# def withdraw():
#     global balance

#     amount = 2500
#     balance = balance - amount

#     print(balance)

# withdraw()