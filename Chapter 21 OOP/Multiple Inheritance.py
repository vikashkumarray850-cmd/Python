# ==========================================
# MULTIPLE INHERITANCE — 
# ==========================================

# Multiple Inheritance

# Isme ek Child class, do Parent classes se inherit karti hai.

# Parent1 ──┐
#           ↓
#         Child
#           ↑
# Parent2 ──┘

# Example:

# class Father:
#     def house(self):
#         print("Father has a house")


# class Mother:
#     def car(self):
#         print("Mother has a car")


# class Child(Father, Mother):
#     pass


# child1 = Child()

# child1.house()
# child1.car()

# Yahan:

# Father → Parent 1
# Mother → Parent 2
# Child(Father, Mother) → Child dono se inherit kar raha hai
# child1.house() → Father ka method
# child1.car() → Mother ka method

# Simple difference:

# Multilevel:
# Grandparent → Parent → Child

# Multiple:
# Parent1 ──→
#            Child
# Parent2 ──→

# Pehle ye concept samajh lo; uske baad practice karenge.

# ==========================================
# Multiple Inheritance — Practice Questions
# ==========================================

# Q1. Create a class named Father.
# Create a method named house().
# Print "Father has a house".

# Create a class named Mother.
# Create a method named car().
# Print "Mother has a car".

# Create a class named Child that inherits from both Father and Mother.

# Create a Child object.
# Call house() and car().

# class Father:
#     def house(self):
#         print("Father has a house")

# class Mother:
#     def car(self):
#         print("Mother has a car")

# class Child(Father, Mother):
#     pass


# child1 = Child()

# child1.house()
# child1.car()
    
# ----------------------------
# Q2. Create a class named Employee.
# Create a method named work().
# Print "Employee is working".

# Create a class named Manager.
# Create a method named manage().
# Print "Manager is managing".

# Create a class named TeamLead that inherits from both Employee and Manager.

# Create a TeamLead object.
# Call work() and manage().


# class Employee:
#     def work(self):
#         print("Employee is working")

# class Manager:
#     def manage(self):
#         print("Manager is managing")

# class TeamLead(Employee, Manager):
#     pass


# teamLead1 = TeamLead()

# teamLead1.work()
# teamLead1.manage()




# Q3. Create a class named Father.
# Create a method named property().
# Print "Father has property".

# Create a class named Mother.
# Create a method named education().
# Print "Mother provides education".

# Create a class named Child that inherits from both Father and Mother.
# Create a method named play().
# Print "Child is playing".

# Create a Child object.
# Call property(), education() and play().


# class Father:
#     def property(self):
#         print("Father has a property")

# class Mother:
#     def education(self):
#         print("Mother provides education")

# class Child(Father, Mother):
#     def play(self):
#         print("Child is playing")


# child1 = Child()

# child1.property()
# child1.education()
# child1.play()