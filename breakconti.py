# break
# continue
# pass
# enumerate
# zip

for i in range(1, 11):
    pass

user1 = "vikas"
user2 = "ramesj"
user3 = "suresh"

user = ["vikas", "ramesh", "suresh"]
for ind , name in enumerate(user):
    print(ind, name)


a = range(20, 31)
for idx, value in enumerate(a):
    if value == 27:
        break
    if value == 23:
        continue
    print(idx, value)



python12 = ("ramesh", "suresh", "ganesh")
python13 = ("vikash", "prakash", "akash")

python1213 = zip(python12, python13)
for i in python1213:
    print(i)


x = range(10, 21)
y = range(20, 41)
z = zip(x, y)
# print(z)
for value in z:
    print(value)




my_name = input("Enter your name: ")
my_age = input("Enter your age: ")
my_email = input("Enter your email: ")

print("my name is ", my_name)
print("my age is ", my_age)
print("my email is ", my_email) 
