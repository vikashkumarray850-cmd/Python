#====================================
#>>>>>>>>>> ABSTRACTION >>>>>>>>>>>>>
#====================================

# Abstraction
# │
# ├── 1. ABC (Abstract Base Class)              🔄
# │      └── ABC ka purpose
# │
# ├── 2. @abstractmethod                        ⏳
# │      └── Method ka rule
# │
# ├── 3. Abstract Class ka Object               ⏳
# │      └── Object kyun nahi bana sakte
# │
# ├── 4. Child Class Implementation             ⏳
# │      └── Abstract method ko implement karna
# │
# └── 5. Small Practical Example                ⏳
#        └── Real-world style example

# Pehle samjho: Abstraction ki zarurat kyun?

# Maan lo hamare paas Animal hai.

# Har animal ki apni sound hoti hai:

# Dog → bark
# Cat → meow
# Cow → moo

# Ab hum chahte hain ki Animal class mein ek rule ho:

# Har Animal ke paas sound() method hona chahiye.

# Lekin Animal khud koi specific sound nahi batayega.

# Yahi Abstraction ka idea hai:

# Animal
#   ↓
# Rule: sound() hona chahiye
#   ↓
# Dog  → apna sound()
# Cat  → apna sound()
# Cow  → apna sound()
# Ab ABC kya hai?

# ABC ka full form hai:

# Abstract Base Class

# Python mein:

# from abc import ABC

# Yahan hum Python ke abc module se ABC le rahe hain.

# Phir:

# class Animal(ABC):

# ka matlab hai:

# Animal ko hum ek abstract base class bana rahe hain.

# Simple language mein, Animal ko hum basic blueprint/rule class ki tarah use kar rahe hain.

# @abstractmethod kya karta hai?

# Ab hum likhte hain:

# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

# Yahan:

# @abstractmethod
# def sound(self):

# ka matlab:

# Jo bhi class Animal se inherit karegi, usko sound() ka apna implementation dena padega.

# Example:

# class Dog(Animal):

#     def sound(self):
#         print("Dog barks")

# Aur:

# class Cat(Animal):

#     def sound(self):
#         print("Cat meows")

# Toh:

# Animal → rule deta hai
#          "sound() hona chahiye"

# Dog    → sound() ka actual implementation
# Cat    → sound() ka actual implementation
# Ek bahut important difference

# Normal class mein:

# class Animal:
#     def sound(self):
#         print("Animal sound")

# Yahan Animal ka actual implementation hai.

# Lekin abstract class mein:

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

# Yahan Animal sirf rule/requirement de raha hai.

# Isi wajah se ABC + @abstractmethod ka use abstraction mein hota hai.

# Abhi sirf ye 3 cheezein yaad rakho
# ABC
# ↓
# Abstract Base Class banane ke liye

# @abstractmethod
# ↓
# Child class ke liye method ka rule banane ke liye

# pass
# ↓
# Parent mein actual implementation nahi hai

# Abhi practice nahi karte. Pehle next step mein main tumhe ye 
# samjhaunga ki abstract class ka object kyun nahi bana sakte, 
# kyunki wahi Abstraction ka sabse important part hai.

#---------------------------------------------------------

# @abstractmethod ka main kaam

# Ye child class ke liye rule banata hai.

# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

# Iska simple meaning:

# Animal class:
# "Jo bhi mujhse inherit karega,
# uske andar sound() method hona chahiye."

# Ab Dog:

# class Dog(Animal):

#     def sound(self):
#         print("Dog barks")

# Dog ne rule follow kiya. ✅

# Cat:

# class Cat(Animal):

#     def sound(self):
#         print("Cat meows")

# Cat ne bhi rule follow kiya. ✅

# Sabse important baat

# @abstractmethod khud sound nahi deta.

# Ye sirf kehta hai:

# "sound() method banana compulsory hai."

# Actual kaam Child class karegi.

# Animal
#   │
#   │ Rule: sound() compulsory
#   ↓
#  ┌─────────┬─────────┐
# Dog       Cat       Cow
#  ↓         ↓         ↓
# sound()   sound()   sound()

# Isliye Abstraction mein hum "what to do" define karte hain,
#  aur child class "how to do it" define karti hai.

# ==========================================
# Abstraction — @abstractmethod Practice
# ==========================================

# Q1. Create an abstract class named Animal.
# Use ABC and @abstractmethod.
# Create an abstract method named sound().
# Create a Dog class that inherits from Animal.
# Implement the sound() method in Dog.
# Create a Dog object and call sound().

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         print("Dog is braking")

# dog1 = Dog()

# dog1.sound()
#---------------------------------------

# Q2. Create an abstract class named Vehicle.
# Use ABC and @abstractmethod.
# Create an abstract method named start().
# Create a Car class that inherits from Vehicle.
# Implement the start() method in Car.
# Create a Car object and call start().

# from abc import ABC, abstractmethod

# class vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         pass

# class Car(vehicle):
#     def start(self):
#         print("Car is started")

# car1 = Car()
# car1.start()
#-----------------------------------------------

# Q3. Create an abstract class named Employee.
# Use ABC and @abstractmethod.
# Create an abstract method named work().
# Create a Manager class that inherits from Employee.
# Implement the work() method in Manager.
# Create a Manager object and call work().

# from abc import ABC, abstractmethod

# class Employee(ABC):

#     @abstractmethod
#     def work(self):
#         pass


# class Manager(Employee):
#     def work(self):
#         print("MANAGER IS NOT AVAILABLE")


# class Supervisor(Employee):
#     def work(self):
#         print("SUPERVISIOR IS WORKING")


# manager1 = Manager()
# supervisor1 = Supervisor()

# manager1.work()
# supervisor1.work()