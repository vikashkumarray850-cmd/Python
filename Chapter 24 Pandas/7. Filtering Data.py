# =====================================================
# CODE NUMBERING BY:-

#  Single Condition                      [13 TO 100]
#  Multiple Conditions (AND & ke saath)  [104 TO 2059]
#  OR (|)                                [209 TO 300]
#  NOT( ~ )                              [304 TO 388] 
#  isin()                                [392 TO 485]
#  between()                             [489 TO 551]
# ======================================================

#==============================
# Topic 1: Single Condition
#==============================

# 1. Filtering kya hoti hai?

# Maan lo tumhare paas products.csv ka data hai:

# ProductName	Category	Price	Stock
# Laptop	Electronics	45000	12
# Mouse	Accessories	600	40
# Keyboard	Accessories	1200	25
# Monitor	Electronics	16000	18
# Tablet	Electronics	22000	15

# Ab tumhe sirf un products ko dekhna hai jinki Price 10,000 se zyada hai.

# Poora DataFrame print karne ke bajaye hum condition laga kar sirf 
# matching rows nikaal sakte hain. 
# Isi ko Filtering kehte hain.

# 2. Single Condition ka syntax
# df[df["ColumnName"] > value]

# Ismein:

# df → DataFrame ka naam
# df["Price"] → Price column
# > 10000 → condition
# df[...] → sirf un rows ko select karega jahan condition True hogi.
# 3. Example
# import pandas as pd

# products_df = pd.read_csv("products.csv")

# result = products_df[products_df["Price"] > 10000]

# print(result)

# Expected output:

# ProductName	Category	Price	Stock
# Laptop	Electronics	45000	12
# Monitor	Electronics	16000	18
# Tablet	Electronics	22000	15

# Mouse aur Keyboard output mein nahi aayenge, kyunki unki prices 10,000 se zyada nahi hain.

# 4. Doosre comparison operators
# Operator	Meaning
# >	Greater than
# <	Less than
# >=	Greater than or equal to
# <=	Less than or equal to
# ==	Equal to
# !=	Not equal to

# Dhyan do: Pandas mein comparison ke liye == use hota hai, jabki = assignment ke liye hota hai.

# Practice Questions — Single Condition
# ==========================================
# Pandas — Single Condition Practice
# ==========================================

# Q1. Read "products.csv" into products_df.
# Display all products whose Price is less than 2000.

# import pandas as pd
# products_df = pd.read_csv("products.csv")
# result = products_df[products_df["Price"] < 2000]
# print(result)
#------------------------------------------------------

# Q2. Read "employees.xlsx" into employees_df.
# Display all employees whose Salary is greater than or equal to 30000.

# import pandas as pd
# employees_df = pd.read_excel("employees.xlsx")
# result = employees_df[employees_df["Salary"]>= 30000]
# print(result)
#--------------------------------------------------------

# Q3. Read "sales.xlsx" into sales_df.
# Display all sales whose Amount is not equal to 2500.

# import pandas as pd
# sales_df = pd.read_excel("sales.xlsx")
# result = sales_df[sales_df["Amount"]!= 2500]
# print(result)
#____________________________________________________________________________________________________

#==============================
# Topic 2: Multiple Conditions
#==============================

# 1. AND (&) kya hota hai?

# Jab humein DataFrame se aisi rows chahiye jo dono conditions 
# ko satisfy karein, tab hum & use karte hain.

# Maan lo products.csv mein ye data hai:

# ProductName	Category	Price	Stock
# Laptop	Electronics	45000	12
# Mouse	Accessories	600	40
# Keyboard	Accessories	1200	25
# Monitor	Electronics	16000	18
# Tablet	Electronics	22000	15
# Webcam	Accessories	1800	20

# Tumhe aise products chahiye:

# Price 2000 se zyada ho.
# Stock 15 se zyada ho.

# Dono conditions true honi chahiye.

# 2. Code samjho
# import pandas as pd

# products_df = pd.read_csv("products.csv")

# result = products_df[
#     (products_df["Price"] > 2000) &
#     (products_df["Stock"] > 15)
# ]

# print(result)
# Output samjho
# ProductName	Price	Stock
# Monitor	16000	18

# Kyun?

# Laptop: Price condition true, lekin Stock 12 hai — false.
# Monitor: Price 16000 aur Stock 18 — dono true.
# Tablet: Price condition true, lekin Stock 15 hai. Humein 15 se zyada chahiye, isliye false.

# Isliye sirf Monitor select hota hai.

# 3. Parentheses () kyun lagate hain?

# Har condition ko alag parentheses mein likhna zaroori hai:

# (products_df["Price"] > 2000) & (products_df["Stock"] > 15)

# Pandas mein multiple conditions ke saath & use karte waqt parentheses lagao. 
# Yahan Python ka and use nahi karna hai.

# Practice Questions — Multiple Conditions (AND)
# ==========================================
# Pandas — Multiple Conditions (AND)
# ==========================================

# Q1. Read "products.csv" into products_df.
# Display products whose Price is greater than 1000
# AND Stock is greater than 20.

# import pandas as pd
# products_df = pd.read_csv("products.csv")
# result = products_df [
#     (products_df["Price"]> 1000) &
#     (products_df["Stock"]> 20)
# ]
# print(result)
#---------------------------------------------

# Q2. Read "employees.xlsx" into employees_df.
# Display employees whose Salary is greater than 25000
# AND Department is "IT".

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx")

# result = employees_df[
#     (employees_df["Salary"]> 25000) &
#     (employees_df["Department"] == "IT")
# ]
# print(result)
#-----------------------------------------------
# Q3. Read "sales.xlsx" into sales_df.
# Display sales whose Quantity is greater than 1
# AND Amount is less than 50000.

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")

# result = sales_df[
#     (sales_df["Quantity"]> 1) &
#     (sales_df["Amount"]< 50000)
# ]
# print(result)
#_____________________________________________________________________________________________________

# ==========================================
# Topic 3 — OR (|)
# ==========================================

# 1. OR (|) ka matlab kya hai?
# OR ka matlab hai: do conditions mein se koi ek bhi True ho, toh row select ho sakti hai.

# Maan lo products.csv mein ye data hai:

# ProductName	Price	Stock
# Laptop	45000	12
# Mouse	600	40
# Keyboard	1200	25
# Monitor	16000	18
# Headphones	2500	10

# Humein aise products chahiye:

# Price 20000 se zyada OR
# Stock 20 se zyada.
# 2. Code
# import pandas as pd

# products_df = pd.read_csv("products.csv")

# result = products_df[
#     (products_df["Price"] > 20000) |
#     (products_df["Stock"] > 20)
# ]

# print(result)
# 3. Output ko samjho
# ProductName	Price	Stock
# Laptop	45000	12
# Mouse	600	40
# Keyboard	1200	25
# Laptop: Price 20,000 se zyada hai, isliye select hoga.
# Mouse: Stock 20 se zyada hai, isliye select hoga.
# Keyboard: Stock 20 se zyada hai, isliye select hoga.
# Monitor: Dono conditions False hain, isliye select nahi hoga.
# Headphones: Dono conditions False hain, isliye select nahi hoga.

# Yaad rakho: | ka matlab hai OR, aur har condition ko parentheses mein likhna hai.

# Practice Questions — OR (|)
# ==========================================
# Pandas — OR Condition Practice
# ==========================================

# Q1. Read "products.csv" into products_df.
# Display products whose Price is less than 1000
# OR Stock is greater than 30. 

# import pandas as pd

# products_df = pd.read_csv("products.csv")

# result = products_df[
#     (products_df["Price"]< 1000) |
#     (products_df["Stock"]> 30)
# ]
# print(result)
#-----------------------------------------------------------

# Read "employees.xlsx" into employees_df.
# Display employees whose Salary is less than 26000
# OR Department is "HR".

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx")

# result = employees_df[
#     (employees_df["Salary"]< 26000) |
#     (employees_df["Department"] == "HR")
# ]
# print(result)
#-----------------------------------------------

# Q3. Read "sales.xlsx" into sales_df.
# Display sales whose Quantity is equal to 1
# OR Amount is greater than 30000.


# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")

# result = sales_df[
#     (sales_df["Quantity"] == 1) |
#     (sales_df["Amount"] > 30000)
# ]
# print(result)
#_____________________________________________________________________________________________________

#==============================
# Topic 4 — Not (~)
#==============================

# 1. NOT (~) ka matlab kya hai?

# Pandas mein ~ operator kisi condition ka result ulta kar deta hai:

# True → False
# False → True

# Maan lo humein un products ko select karna hai jinki price 2000 se zyada nahi hai.

# products.csv ka example:

# ProductName	Price
# Laptop	45000
# Mouse	600
# Keyboard	1200
# Monitor	16000
# Headphones	2500
# 2. Code se samjho

# Pehle normal condition dekho:

# result = products_df[products_df["Price"] > 2000]
# print(result)

# Ismein sirf 2000 se zyada price wale products select honge.

# Ab ~ use karte hain:

# result = products_df[~(products_df["Price"] > 2000)]
# print(result)

# Output:

# ProductName	Price
# Mouse	600
# Keyboard	1200
# 3. Ye kaise kaam karta hai?
# Product	Price > 2000	~ ke baad
# Laptop	True	False
# Mouse	False	True
# Keyboard	False	True
# Monitor	True	False
# Headphones	True	False

# ~ ne condition ka result reverse kar diya. Isliye Mouse aur Keyboard select hue.

# Important: ~ ko condition ke aage lagate hain aur condition ko parentheses mein rakhte hain.

# Practice Questions — NOT (~)
# ==========================================
# Pandas — NOT (~) Practice
# ==========================================

# Q1. Read "products.csv" into products_df.
# Use ~ to display products whose Price is NOT greater than 10000.

# import pandas as pd
# products_df = pd.read_csv("products.csv")
# result = products_df[~(products_df["Price"] > 10000)]
# print(result)
#-------------------------------------------------
# Q2. Read "employees.xlsx" into employees_df.
# Use ~ to display employees whose Department is NOT "IT".

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx")

# result = employees_df[~(employees_df["Department"] == "IT")]

# print(result)
#-----------------------------------------------------------

# Q3. Read "sales.xlsx" into sales_df.
# Use ~ to display sales whose Quantity is NOT equal to 1.

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")

# result = sales_df[~(sales_df["Quantity"]== 1)]
# print(result)
#__________________________________________________________________________________________________________

#==============================
# Topic 5: isin()
#==============================

# 1. isin() kya karta hai?

# Jab humein kisi column mein se kai specific values wali 
# rows select karni hoti hain, tab isin() use karte hain.

# Maan lo products.csv mein tumhe sirf Laptop, Mouse aur Tablet products chahiye.

# ProductName	Category	Price
# Laptop	Electronics	45000
# Mouse	Accessories	600
# Keyboard	Accessories	1200
# Monitor	Electronics	16000
# Tablet	Electronics	22000
# 2. Code se samjho
# import pandas as pd

# products_df = pd.read_csv("products.csv")

# result = products_df[
#     products_df["ProductName"].isin(["Laptop", "Mouse", "Tablet"])
# ]

# print(result)

# Output mein sirf ye products aayenge:

# ProductName	Category	Price
# Laptop	Electronics	45000
# Mouse	Accessories	600
# Tablet	Electronics	22000
# 3. isin() kaise kaam karta hai?
# products_df["ProductName"].isin(["Laptop", "Mouse", "Tablet"])

# Pandas har row ka ProductName check karta hai:

# Laptop → True
# Mouse → True
# Keyboard → False
# Monitor → False
# Tablet → True

# Phir filtering sirf True wali rows ko select karti hai.

# Yaad rakho:

# == ek particular value check karne ke liye use kar sakte ho.
# isin() ek list mein di gayi multiple values check karne ke liye useful hai.
# Practice Questions — isin()
# ==========================================
# Pandas — isin() Practice
# ==========================================

# Q1. Read "products.csv" into products_df.
# Display products whose Category is either
# "Electronics" or "Accessories" using isin().

# import pandas as pd

# products_df = pd.read_csv("products.csv")

# result = products_df[
#     products_df["Category"].isin(["Electronics", "Accessories"])
# ]
# print(result)
#-------------------------------------------------

# Q2. Read "employees.xlsx" into employees_df.
# Display employees whose Department is either
# "IT" or "HR" using isin().

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx")
# result = employees_df[
#     employees_df["Department"].isin(["IT", "HR"])
# ]
# print(result)
#-----------------------------------------------------


# Q3. Read "sales.xlsx" into sales_df.
# Display sales whose SaleID is either 102, 104 or 108
# using isin().

# import pandas as pd

# sales_df = pd.read_excel("sales.xlsx")
# result = sales_df[
#     sales_df["SaleID"].isin([102, 104, 108])
# ]
# print(result)
#_____________________________________________________________________________________________________

#==============================
# topic 6: between()
#==============================

# Ye Section 7 — Filtering Data ka aakhri topic hai.

# between() ka use tab hota hai jab humein kisi column ki values ko ek range ke andar filter karna ho.

# Example:

# result = products_df[
#     products_df["Price"].between(1000, 10000)
# ]

# print(result)

# Iska matlab: un products ko select karo jinki Price 1000 se 10000 ke beech hai.

# Dhyan do: Default mein between() dono limits ko include karta hai. 
# Matlab 1000 aur 10000 ki price wale products bhi select honge.

# Pandas — between() Practice Questions
# Pandas — between() Practice
# ==========================================
# Pandas — between() Practice
# ==========================================

# Q1. Read "products.csv" into products_df.
# Display products whose Price is between 1000 and 10000.

# import pandas as pd

# products_df = pd.read_csv("products.csv")
# result = products_df[
#     products_df["Price"].between(1000 , 10000)
# ]
# print(result)
#--------------------------------------------

# Q2. Read "employees.xlsx" into employees_df.
# Display employees whose Salary is between 25000 and 33000.

# import pandas as pd

# employees_df = pd.read_excel("employees.xlsx")

# result = employees_df[
#     employees_df["Salary"].between(25000,33000 )
# ]
# print(result)
#----------------------------------------------------

# Q3. Read "sales.xlsx" into sales_df.
# Display sales whose Amount is between 2000 and 15000.

import pandas as pd

sales_df = pd.read_excel("sales.xlsx")

result = sales_df[
    sales_df["Amount"].between(2000, 15000)
]

print(result)
