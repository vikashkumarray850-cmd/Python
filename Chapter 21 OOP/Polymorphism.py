# Polymorphism
# │
# ├── Basic Polymorphism                  ✅     start serial no. 85 -> 141
# │
# ├── Polymorphism with Multiple Classes  🔄 Current (start serial no. 146 -> 183)
# │   └── Same function → different objects
# │
# ├── Method Overriding                   ✅ Already done  (start serial no. 146 -> 183)
# │
# └── Practical Example                   ⏳

# Polymorphism start karte hain. Pehle sirf concept samjhenge, practice abhi nahi.

# Polymorphism

# Simple meaning:

# Poly = many
# Morph = forms

# Python mein Polymorphism ka matlab hai:

# Same method/action ka naam, different objects ke liye different behavior.

# Example dekho:

# class Dog:
#     def sound(self):
#         print("Dog barks")


# class Cat:
#     def sound(self):
#         print("Cat meows")


# dog1 = Dog()
# cat1 = Cat()

# dog1.sound()
# cat1.sound()

# Output:

# Dog barks
# Cat meows

# Yahan important cheez:

# dog1.sound()
# cat1.sound()

# Dono mein same method name sound() hai.

# Lekin:

# Dog object → sound() par "Dog barks"
# Cat object → sound() par "Cat meows"

# Isi ko Polymorphism kehte hain.

# Abhi ek important difference

# Inheritance mein humne dekha tha:

# class Animal:
#     def sound(self):
#         print("Animal sound")


# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# Yahan Dog, Animal se inherit kar raha hai aur same method ko change kar raha hai

# Polymorphism mein focus hai:

# same method name → different objects → different behavior

# ==========================================
# Polymorphism — Basic Practice
# ==========================================

# Q1. Create two classes named Dog and Cat.
# Create a method named sound() in both classes.
# Print different sounds for Dog and Cat.
# Create one object of each class and call sound().

# class Dog:
#     def sound(self):
#         print("Dog is barking")

# class Cat:
#     def sound(self):
#         print("Cat mewo")


# dog1 = Dog()
# cat1 = Cat()

# dog1.sound()
# cat1.sound()

# Q2. Create two classes named Car and Bike.
# Create a method named move() in both classes.
# Give different messages for Car and Bike.
# Create objects and call move().

# class Car:
#     def move(self):
#         print("Car is moving")
    
# class Bike:
#     def move(self):
#         print("Bike is moving")

# car1 = Car()
# bike1 = Bike()

# car1.move()
# bike1.move()

# Q3. Create two classes named Employee and Manager.
# Create a method named work() in both classes.
# Print a different work message for each class.
# Create objects and call work().

# class Employee:
#     def work(self):
#         print("emp is not available")

# class Manager:
#     def work(self):
#         print('Manager is available')

# employee1 = Employee()
# manager1 = Manager()

# employee1.work()
# manager1.work()

#❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
#-----------------------------------------------------------------------------------------------------------

# POLYMORPHISM WITH INHERITANCE
# └── PARENT METHOD → CHILD KA DIFFERENT BEHAVIOR

# Jo example maine diya:

# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# Ye Method Overriding hi hai.

# Toh Polymorphism aur Overriding ka relation kya hai?

# Simple way:

# Method Overriding
#       ↓
# Child Parent ke same method ko
# apne according redefine karta hai.

# Polymorphism
#       ↓
# Same method call
#       ↓
# Different objects
#       ↓
# Different behavior

# Isliye Method Overriding = technique, aur Polymorphism = broader concept/behavior.

# Tumne Method Overriding pehle hi properly kar liya hai, isliye usko dobara practice 
# karne ki zarurat nahi.
#❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
#-----------------------------------------------------------------------------------------------------------


#==================================
# POLYMORPHISM WITH MULTIPLE CLASSES
# SAME FUNCTION + DIFFERENT OBJECTS
#==================================

# Yahan hum ek hi function banayenge jo different objects ke saath kaam karega.

# class Dog:
#     def sound(self):
#         print("Dog barks")


# class Cat:
#     def sound(self):
#         print("Cat meows")


# def make_sound(animal):
#     animal.sound()


# dog1 = Dog()
# cat1 = Cat()

# make_sound(dog1)
# make_sound(cat1)

# Output:

# Dog barks
# Cat meows

# Yahan important point hai:

# def make_sound(animal):
#     animal.sound()

# make_sound() ko pata nahi ki animal Dog hai ya Cat.

# Bas usse ye pata hai ki object ke paas sound() method hona chahiye.

# Isliye:

# make_sound(dog1)

# → Dog ka sound() chalega.

# make_sound(cat1)

# → Cat ka sound() chalega.

# Yahi Polymorphism ka important practical use hai:
# same function → different objects → different behavior.

# ==========================================
# Polymorphism with Multiple Classes
# ==========================================

# Q1. Create two classes named Dog and Cat.
# Create a sound() method in both classes.
# Create a function named make_sound().
# Pass an object to make_sound() and call its sound() method.
# Test the function with both Dog and Cat objects.

# class Dog:
#     def sound(self):
#         print("Dog is barking")

# class Cat:
#     def sound(self):
#         print("Cat's Meow")

# def make_sound(animal):
#         animal.sound()

# dog1 = Dog()
# cat1 = Cat()

# make_sound(dog1)
# make_sound(cat1)

#-----------------------------------------------
# Q2. Create two classes named Car and Bike.
# Create a move() method in both classes.
# Create a function named start_move().
# Pass Car and Bike objects to the function.
# Call the move() method inside the function.

# class Car:
#     def move(self):
#         print("car is moving")

# class Bike:
#     def move(self):
#         print("Bike is started")

# def start_move(vechile):
#         vechile.move()

# car1 = Car()
# bike1 = Bike()

# start_move(car1)
# start_move(bike1)
#---------------------------------------------------


# Q3. Create two classes named Employee and Manager.
# Create a work() method in both classes.
# Create a function named show_work().
# Pass Employee and Manager objects to the function.
# Call the work() method inside the function.

# class Employee:
#     def work(self):
#         print("emp not working")

# class Manager:
#     def work(self):
#         print("Manager not available")


# def show_work(Company):
#     Company.work()

# employee1 = Employee()
# manager1 = Manager()

# show_work(employee1)
# show_work(manager1)