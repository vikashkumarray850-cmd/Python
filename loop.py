
# st = 15
# end = 27
# while st <= end:
#     print(st, "Hello World")
#     st += 1
'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

# st = 1
# line = int(input("Enter line no: "))

# while st <= line:
#     print("* " * st)

#     st += 1

#  11 -> 0
# st = 11
# while(st >= 0):
#     print("Hello")
#     st -= 1 # st = st + 1

# for loop
#  range(15) -> 0 -> 14
#  range(1, 15) -> 1 -> 14
#  range(1, 15, 3) -> 1, 4, 7, 10, 13
# for i in range(1, 15, 3):
#     print(i)


# for num in range(1, 13):
#     print(num, "th Month", num, "th Month")
#     print(f"{num} th Month {num} st Month")


# name = "Ramu"
# age = 14
# address = "Kolkata"
# salary = 10000
# print("Hello, My name is", name, "My age is: ", age, "I am from ", address, " My salary is: ", salary)
# # # formated string
# print(f"Hello, My name is {name} My age is {age} Iam from {address} My salary is {salary}")

# # nested loop ☠️

# # for month in range(1, 13): # month
# #     for days in range(1, 31):
# #         print(f"{days}th day of {month} Month")

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(i, end='')
#     print()

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()


# line = 5
# star = 1
# for i in range(1, 6):
#     #  gap
#     for j in range(1, line+1):
#         print("  ", end='')
#     # star
#     for j in range(1, star+1):
#         print("* ", end='')
#     print()
#     line -= 1
#     star += 2



# for i in range(1, 6):
#     for j in range(1, 6):
#         print(j, end=' ')

#     print()

#Q1. 1 se 10 tak numbers print karo.
# for i in range(11):
#    print(i)

#Q2. 10 se 1 tak reverse order me print karo.

# for i in range(10, 0, -1):
#    print(i)

# Q3. 1 se 20 tak sirf even numbers print karo.
# for i in range(2, 21, 2):
#     print(i)

# Q4. 1 se 20 tak sirf odd numbers print karo.
# for i in range(1, 21, 2):
#     print(i)

# Q5. 1 se 10 tak ke numbers ka square print karo.
# for i in range(1, 11):
#     print(i ** 2)

# Q6. 1 se 10 tak ke numbers ka cube print karo.
# for i in range(1, 11):
#     print(i ** 3)

# Q7. User se ek number input lo aur uska table (1 se 10 tak) print karo.

# Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50
# num =int(input("enter your number"))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# aise bhi ho skta hai

# num = int(input("Enter a Number: "))

# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")


#Q7. 1 se 10 tak ke numbers ka square aur cube ek saath print karo.
# Number = 1, Square = 1, Cube = 1
# Number = 2, Square = 4, Cube = 8
# Number = 3, Square = 9, Cube = 27
# ...
# Number = 10, Square = 100, Cube = 1000

# for i in range(1, 11):
#     print(f"number{i}, square{i ** 2}, {i ** 3}")

# Q8. 1 se 100 tak ke sabhi numbers ka sum nikalo.

# Expected Output:
# 5050

total = 0

for i in range(1, 101):
    total = total + i

print("Sum =", total)