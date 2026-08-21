# function
def sum_of_two_nums(a, b):
    # print(a + b)
    return a + b

# print(sum_of_two_nums(1, 3) * 100)



def greet(name, age, salary=10000,  address="India"): # parametrs
    print(f'Hello {name}, your age is {age}, you r from {address}, your salary is {salary}')

# greet("Harish", 12, 12000, "Kolkata") 
# greet(name="Tushar",age= 20, address="Kolkata") # arguments


# *args/**kwargs
# lambda
# recursion


def addition(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum



print(addition(1, 2, 3, 6))
# print(addition(1, 2))
# print(addition(1, 2, 45))




def me_kon_kon_sub_paratahu(**subs):
    for sub, sub_name in enumerate(subs):
        print(sub_name, sub, subs[sub_name])

me_kon_kon_sub_paratahu(sub1="MERN", sub2="DA", sub3="PYTHON", sub4="PHP")


# lambda
# recursion
# list