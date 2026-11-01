# ========================================
# CODE NUMBERING BY:-

# 1 pivot_table()          [27 TO 422]       
# 2 Rows & Columns         [427 TO 753]
# 3 Values & aggfunc       [758 TO 878]
# 4 Multiple Aggregations  [882 TO 1023]
# 5 pd.crosstab()          [1027 TO 1203]
# =========================================

#========================================
# Complete Topic Overview
#========================================

# | No. | Topic                 | Kya seekhenge?                                                        |
# | --: | --------------------- | --------------------------------------------------------------------- |
# |   1 | `pivot_table()`       | Rows aur columns ke basis par summarized report banana                |
# |   2 | `index` & `columns`   | Report mein rows aur columns decide karna                             |
# |   3 | `values` & `aggfunc`  | Kis column ka calculation karna hai aur kaunsa function use karna hai |
# |   4 | Multiple Aggregations | Ek hi report mein sum, mean, count jaise calculations                 |
# |   5 | `crosstab()`          | Do categorical columns ke beech frequency table banana                |


#=====================================
# Section 19. Pivot Tables & Crosstab
#-------------------------------------
#Topic 1 — pivot_table()
#=====================================

# 1. Pivot Table ki zarurat kyun padti hai?

# Maan lo tum ek company mein Data Analyst ho aur tumhare paas ye sales data hai:

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000]
# })

# print(df)

# Original Data:

# Index	City	Product	Sales
# 0	Kolkata	Laptop	50000
# 1	Delhi	Mobile	30000
# 2	Kolkata	Mobile	20000
# 3	Delhi	Laptop	40000
# 4	Mumbai	Laptop	60000
# 5	Mumbai	Mobile	25000

# Ye raw data hai. Ismein har transaction ki details hain.

# Ab manager tumse poochta hai:

# Kolkata ki total sales kitni hain?
# Delhi ki total sales kitni hain?
# Mumbai ki total sales kitni hain?

# Tum manually calculate kar sakte ho, lekin large dataset mein ye practical nahi hai.

# Isi tarah ke data ko summarize karne ke liye hum pivot_table() use karte hain.

# 2. Pehla Pivot Table — City-wise Total Sales

# Code:

# result = pd.pivot_table(
#     df,
#     index="City",
#     values="Sales",
#     aggfunc="sum"
# )

# print(result)

# Output:

# City	Sales
# Delhi	70000
# Kolkata	70000
# Mumbai	85000

# Ab samjho calculation kaise hui:

# Delhi = 30000 + 40000 = 70000
# Kolkata = 50000 + 20000 = 70000
# Mumbai = 60000 + 25000 = 85000

# Yaani 6 transaction rows ko summarize karke 3 city-wise rows bana di gayi.

# Yehi Pivot Table ka main kaam hai: raw data ko summarized report mein convert karna.

# 3. Ab pivot_table() ke parameters samjho

# Is code ko dekho:

# pd.pivot_table(
#     df,
#     index="City",
#     values="Sales",
#     aggfunc="sum"
# )
# A. df
# df

# Ye tumhara original DataFrame hai. Pandas ko batana padta hai ki kis data par calculation karni hai.

# B. index="City"
# index="City"

# Iska matlab hai ki City ke basis par rows banao.

# Pandas same city wale records ko ek group mein rakhega.

# C. values="Sales"
# values="Sales"

# Iska matlab hai ki Sales column par calculation karni hai.

# D. aggfunc="sum"
# aggfunc="sum"

# Iska matlab hai ki har city ki Sales ko add karna hai.

# aggfunc mein tum alag-alag functions use kar sakte ho:

# aggfunc	Kaam
# "sum"	Total
# "mean"	Average
# "count"	Number of records
# "max"	Maximum value
# "min"	Minimum value
# 4. Same data, different calculation

# Ab maan lo manager total sales nahi, balki average sales per city poochta hai.

# Sirf aggfunc change karo:

# result = pd.pivot_table(
#     df,
#     index="City",
#     values="Sales",
#     aggfunc="mean"
# )

# print(result)

# Output:

# City	Sales
# Delhi	35000
# Kolkata	35000
# Mumbai	42500

# Calculation:

# Delhi = (30000 + 40000) / 2 = 35000
# Kolkata = (50000 + 20000) / 2 = 35000
# Mumbai = (60000 + 25000) / 2 = 42500

# Dhyan do: Original data same hai. Sirf calculation change hui hai.

# 5. Ab ek important example — City aur Product dono ke basis par report

# Manager ab poochta hai:

# Har city mein Laptop aur Mobile ki kitni sales hui?

# Ab humein sirf city-wise report nahi chahiye. Humein city ke saath product-wise breakdown bhi chahiye.

# Code:

# result = pd.pivot_table(
#     df,
#     index="City",
#     columns="Product",
#     values="Sales",
#     aggfunc="sum"
# )

# print(result)

# Output:

# City	Laptop	Mobile
# Delhi	40000	30000
# Kolkata	50000	20000
# Mumbai	60000	25000

# Is report ko samjho:

# Delhi: Laptop ki sales 40000, Mobile ki sales 30000.
# Kolkata: Laptop ki sales 50000, Mobile ki sales 20000.
# Mumbai: Laptop ki sales 60000, Mobile ki sales 25000.

# Yahan ek naya parameter aaya:

# columns="Product"

# Iska matlab Product ki unique values ko report ke alag-alag columns mein dikhao.

# Ab tak ke parameters:

# Parameter	Kaam
# index	Rows decide karta hai
# columns	Columns decide karta hai
# values	Calculation kis column par hogi
# aggfunc	Kaunsi calculation hogi
# Ek baat achhe se samjho

# groupby() aur pivot_table() mein difference dekho:

# GroupBy:

# df.groupby("City")["Sales"].sum()

# Pivot Table:

# pd.pivot_table(
#     df,
#     index="City",
#     values="Sales",
#     aggfunc="sum"
# )

# Dono se city-wise total sales mil sakti hain.

# Lekin jab tumhe City ko rows mein aur Product ko columns mein dikhakar report banani ho, 
# tab pivot_table() bahut useful hota hai.

# Abhi ke liye itna yaad rakho
# index = Rows
# columns = Columns
# values = Calculation wala column
# aggfunc = Calculation ka function

#=========================================================
# fill_value=0 in pivot_table()
#==========================================================
# fill_value=0 ka use Pivot Table mein aane wali missing values 
# (NaN) ko 0 se replace karne ke liye hota hai.

# 1. Example dekho
# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop"],
#     "Sales": [50000, 30000, 20000, 60000]
# })

# Ab Pivot Table banao:

# result = pd.pivot_table(
#     df,
#     index="City",
#     columns="Product",
#     values="Sales",
#     aggfunc="sum"
# )

# print(result)

# Output:

# City	Laptop	Mobile
# Delhi	NaN	30000
# Kolkata	50000	20000
# Mumbai	60000	NaN
# 2. NaN kyun aaya?
# Delhi mein Laptop ki koi sale record nahi hai.
# Mumbai mein Mobile ki koi sale record nahi hai.

# Isliye Pandas ne un combinations ke liye NaN dikhaya.

# 3. Ab fill_value=0 use karo
# result = pd.pivot_table(
#     df,
#     index="City",
#     columns="Product",
#     values="Sales",
#     aggfunc="sum",
#     fill_value=0
# )

# print(result)

# Output:

# City	Laptop	Mobile
# Delhi	0	30000
# Kolkata	50000	20000
# Mumbai	60000	0

# Ab NaN ki jagah 0 aa gaya.

# Yaad rakho
# fill_value=0

# Matlab Pivot Table ke result mein missing values ko zero se fill karna.

# Important: Zero ka matlab hai ki available data mein us 
# City-Product combination ki koi recorded sale nahi mili. 
# Iska matlab zaroori nahi ki real world mein sales bilkul zero hi thi.

# Ab tum apne 5 practice questions mein zarurat ke hisaab se fill_value=0 bhi use kar sakte ho.

# Agla step: In parameters ko samajhne ke baad hum fill_value=0 bhi 
# seekhenge, jisse pivot table mein missing combinations ko 0 se replace kar sakte hain.

# ==========================================
# Pandas Section 19 — Pivot Tables & Crosstab
# Topic 1: pivot_table()
# ==========================================

# Use the following DataFrame for all questions.

# Q1.
# Create a Pivot Table showing total Sales for each City.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000]
# })

# result = pd.pivot_table(
#     df,
#     index="City",
#     values="Sales",
#     aggfunc="sum"
# )

# print(result)
#----------------------------------------------------
# Q2.
# Create a Pivot Table showing average Sales for each City.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000]
# })

# result = pd.pivot_table(
#     df,
#     index = "City",
#     values= "Sales",
#     aggfunc= "mean"
# )
# print(result)
#-----------------------------------------------------------

# Q3.
# Create a Pivot Table showing total Sales for each Product.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000]
# })

# result = pd.pivot_table(
#     df,
#     index="Product",
#     values="Sales",
#     aggfunc="sum"
# )

# print(result)
#------------------------------------------------------------

# Q4.
# Create a Pivot Table showing maximum Sales for each City.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000]
# })

# result = pd.pivot_table(
#     df,
#     index= "City",
#     values= "Sales",
#     aggfunc= "max"
# )
# print(result)
#--------------------------------------------------------------

# Q5.
# Create a Pivot Table showing total Sales for each City and Product.
# Display City as rows and Product as columns.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000]
# })

# result = pd.pivot_table(
#     df,
#     index= "City",
#     columns= "Product",
#     values= "Sales",
#     aggfunc= "sum"
# )

# print(result)

#_____________________________________________________________________________________________________

#==============================
# Topic 2 — index & columns
#==============================

# Pichhle topic mein humne index="City" aur columns="Product" use kiya tha. 
# Ab in dono ko detail mein samjhenge.

# 1. index kya karta hai?

# index decide karta hai ki Pivot Table mein rows kis column ke basis par banengi.

# Example:

# result = pd.pivot_table(
#     df,
#     index="City",
#     values="Sales",
#     aggfunc="sum"
# )

# print(result)

# Output:

# City	Sales
# Delhi	70000
# Kolkata	70000
# Mumbai	85000

# Yahan index="City" hone ke karan har City ki ek row bani.

# Agar index="Product" kar doge:

# result = pd.pivot_table(
#     df,
#     index="Product",
#     values="Sales",
#     aggfunc="sum"
# )

# print(result)

# Output:

# Product	Sales
# Laptop	150000
# Mobile	75000

# Ab har Product ki ek row ban gayi.

# Matlab index badalne se report ki rows badal jaati hain.

# 2. columns kya karta hai?

# columns decide karta hai ki kisi column ki unique values 
# Pivot Table mein alag-alag columns ke roop mein dikhen.

# Example:

# result = pd.pivot_table(
#     df,
#     index="City",
#     columns="Product",
#     values="Sales",
#     aggfunc="sum"
# )

# print(result)

# Output:

# City	Laptop	Mobile
# Delhi	40000	30000
# Kolkata	50000	20000
# Mumbai	60000	25000

# Yahan:

# index="City" → City rows mein.
# columns="Product" → Laptop aur Mobile alag columns mein.
# 3. index aur columns ka difference
# Parameter	Kaam
# index	Rows banata hai
# columns	Alag-alag columns banata hai

# Ek simple trick:

# index = Vertical direction (rows)
# columns = Horizontal direction (columns)
# 4. Kya multiple columns ko index mein de sakte hain?

# Haan! Example:

# result = pd.pivot_table(
#     df,
#     index=["City", "Product"],
#     values="Sales",
#     aggfunc="sum"
# )

# print(result)

# Ismein pehle City aur uske andar Product ke basis par rows group hongi. 
# Is tarah multi-level index banega.

# Practice Questions — 3 Questions
# ==========================================
# Pandas Section 19 — Pivot Tables & Crosstab
# Topic 2: index & columns
# ==========================================

# Use the following DataFrame for all questions.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000]
# })


# Q1.
# Create a Pivot Table showing total Sales.
# Display Product as rows.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000]
# })

# result = pd.pivot_table(
#     df,
#     index= "Product",
#     values= "Sales",
#     aggfunc= "sum"
# )

# print(result)
#--------------------------------------------
# Q2.
# Create a Pivot Table showing total Sales.
# Display City as rows and Product as columns.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000]
# })

# result = pd.pivot_table(
#     df,
#     index= "City",
#     columns= "Product",
#     values= "Sales",
#     aggfunc= "sum",
#     fill_value= 0
# )
# print(result)
#-----------------------------------------
# Q3.
# Create a Pivot Table showing total Sales.
# Use both City and Product as index.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000]
# })

# result = pd.pivot_table(
#     df,
#     index=[ "City","Product"],
#     values= "Sales",
#     aggfunc= "sum"
# )

# print(result)

#_____________________________________________________________________________________________________

#==============================
# Topic 3 — values & aggfunc,
#==============================

# Is topic mein hum samjhenge ki Pivot Table mein:

# Kis column par calculation karni hai (values)?
# Kaunsi calculation karni hai (aggfunc)?
# 1. values kya karta hai?

# Maan lo hamare paas ye DataFrame hai:

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000],
#     "Quantity": [2, 3, 4, 2, 5, 3]
# })

# Ab manager poochta hai: har City mein total Sales kitni hain?

# result = pd.pivot_table(
#     df,
#     index="City",
#     values="Sales",
#     aggfunc="sum"
# )

# print(result)

# Yahan:

# values="Sales"

# Iska matlab hai ki calculation Sales column par hogi.

# Agar manager total Quantity poochta hai, toh:

# values="Quantity"

# Yaad rakho: values decide karta hai ki kis column ki values calculate hongi.

# 2. aggfunc kya karta hai?

# aggfunc decide karta hai ki selected column par kaunsi calculation karni hai.

# Maan lo:

# result = pd.pivot_table(
#     df,
#     index="City",
#     values="Sales",
#     aggfunc="sum"
# )

# Yahan aggfunc="sum" ka matlab hai har City ki Sales ko add karna.

# Ab aggfunc badal kar alag calculations kar sakte hain:

# aggfunc	Meaning
# "sum"	Total
# "mean"	Average
# "count"	Non-missing values ki count
# "max"	Maximum value
# "min"	Minimum value
# 3. Ek hi DataFrame par examples

# Total Sales:

# pd.pivot_table(df, index="City", values="Sales", aggfunc="sum")

# Average Sales:

# pd.pivot_table(df, index="City", values="Sales", aggfunc="mean")

# Maximum Sales:

# pd.pivot_table(df, index="City", values="Sales", aggfunc="max")

# Minimum Sales:

# pd.pivot_table(df, index="City", values="Sales", aggfunc="min")

# Notice karo: index aur values same hain. Sirf aggfunc change hua hai, isliye calculation badal gayi.

# 4. Multiple columns in values

# Tum ek se zyada columns bhi select kar sakte ho:

# result = pd.pivot_table(
#     df,
#     index="City",
#     values=["Sales", "Quantity"],
#     aggfunc="sum"
# )

# print(result)

# Isse har City ki total Sales aur total Quantity dono milengi.

# 5. Multiple functions in aggfunc

# Ek hi column par multiple calculations bhi kar sakte ho:

# result = pd.pivot_table(
#     df,
#     index="City",
#     values="Sales",
#     aggfunc=["sum", "mean", "max"]
# )

# print(result)

# Isse har City ke liye:

# Total Sales
# Average Sales
# Maximum Sales

# teenon calculations milengi.

# Quick Revision
# Parameter	Kaam
# index	Rows decide karta hai
# columns	Columns decide karta hai
# values	Calculation wala column select karta hai
# aggfunc	Calculation ka function select karta hai

# Ek simple example yaad rakho:

# pd.pivot_table(
#     df,
#     index="City",
#     values="Sales",
#     aggfunc="sum"
# )

# City ke basis par rows banao, Sales column lo aur uska total calculate karo.


# ==========================================
# Pandas Section 19 — Pivot Tables & Crosstab
# Topic 3: values & aggfunc
# ==========================================

# Use the following DataFrame for all questions.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000],
#     "Quantity": [2, 3, 4, 2, 5, 3]
# })


# Q1.
# Create a Pivot Table showing total Quantity for each City.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000],
#     "Quantity": [2, 3, 4, 2, 5, 3]
# })

# result = pd.pivot_table(
#     df,
#     index= "City",
#     values= "Quantity",
#     aggfunc= "sum"
# )
# print(result)
#------------------------------------------------------------

# Q2.
# Create a Pivot Table showing average Sales for each Product.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000],
#     "Quantity": [2, 3, 4, 2, 5, 3]
# })

# result = pd.pivot_table(
#     df,
#     index= "Product",
#     values= "Sales",
#     aggfunc= "mean"
# )
# print(result)
#-------------------------------------------------------------

# Q3.
# Create a Pivot Table showing total Sales and total Quantity
# for each City.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000],
#     "Quantity": [2, 3, 4, 2, 5, 3]
# })

# result = pd.pivot_table(
#     df,
#     index= "City",
#     values= ["Sales", "Quantity"],
#     aggfunc= "sum"
# )
# print(result)
#---------------------------------------------------

# Q4.
# Create a Pivot Table showing minimum and maximum Sales
# for each City.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000],
#     "Quantity": [2, 3, 4, 2, 5, 3]
# })

# result = pd.pivot_table(
#     df,
#     index= "City",
#     values= "Sales",
#     aggfunc= ["min","max"]
# )
# print(result)
#------------------------------------------------------------

# Q5.
# Create a Pivot Table showing total, average and maximum Sales
# for each City.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000],
#     "Quantity": [2, 3, 4, 2, 5, 3]
# })

# result = pd.pivot_table(
#     df,
#     index= "City",
#     values= "Sales",
#     aggfunc= ["sum","mean","max"]
# )
# print(result)
#_____________________________________________________________________________________________________

#================================
# Topic 4 — Multiple Aggregations
#================================

# Multiple Aggregations ka matlab hai ek hi Pivot Table mein multiple calculations perform karna.

# Iske do common methods hain:

# 1. Multiple Aggregations on One Column

# Jab ek hi column par multiple calculations karni hon, tab aggfunc mein list use karte hain.

# Example: City-wise Sales ka total, average aur maximum nikalna.

# result = pd.pivot_table(
#     df,
#     index="City",
#     values="Sales",
#     aggfunc=["sum", "mean", "max"]
# )

# print(result)

# Yahan:

# sum → Total Sales
# mean → Average Sales
# max → Maximum Sales
# 2. Different Aggregations on Different Columns

# Jab alag-alag columns par alag calculations karni hon, tab dictionary use karte hain.

# Example:

# Sales ka total
# Quantity ka average
# result = pd.pivot_table(
#     df,
#     index="City",
#     aggfunc={
#         "Sales": "sum",
#         "Quantity": "mean"
#     }
# )

# print(result)

# Yahan:

# Sales par sum apply hoga.
# Quantity par mean apply hoga.
# Difference
# Requirement	Method
# One column, multiple calculations	List
# Different columns, different calculations	Dictionary

# Important: values specify karna zaroori nahi hai jab aap dictionary 
# mein columns aur unke aggregation functions specify kar rahe ho.

# Practice Questions — Topic 4: Multiple Aggregations
# ==========================================
# Pandas Section 19 — Multiple Aggregations
# ==========================================

# Use the following DataFrame for all questions.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000],
#     "Quantity": [2, 3, 4, 2, 5, 3]
# })


# Q1.
# Create a Pivot Table showing total, average and minimum
# Sales for each City.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000],
#     "Quantity": [2, 3, 4, 2, 5, 3]
# })
# result = pd.pivot_table(
#     df,
#     index= "City",
#     values= "Sales",
#     aggfunc= ["sum","mean","min"]
# )
# print(result)
#----------------------------------------------

# Q2.
# Create a Pivot Table showing:
# Average Sales and maximum Quantity for each Product.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000],
#     "Quantity": [2, 3, 4, 2, 5, 3]
# })

# result = pd.pivot_table(
#     df,
#     index="Product",
#     aggfunc={
#         "Sales": "mean",
#         "Quantity": "max"
#     }
# )

# print(result)
#--------------------------------------------------

# Q3.
# Create a Pivot Table showing:
# Maximum Sales and total Quantity for each City.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Sales": [50000, 30000, 20000, 40000, 60000, 25000],
#     "Quantity": [2, 3, 4, 2, 5, 3]
# })
# result = pd.pivot_table(
#    df,
#    index= "City",
#    aggfunc= {
#     "Sales" : "max",
#     "Quantity" : "sum"
#    }
# )
# print(result)
#_____________________________________________________________________________________________________

#==============================
# Topic 5 — crosstab()
#==============================

# pd.crosstab() ka use do categorical columns ke beech frequency table banane ke liye hota hai.

# Isse pata chalta hai ki kisi category ka combination kitni baar occur hua.

# 1. Basic crosstab()

# Example DataFrame:

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"]
# })

# Ab City aur Product ke beech frequency table banate hain:

# result = pd.crosstab(
#     df["City"],
#     df["Product"]
# )

# print(result)

# Output:

# City	Laptop	Mobile
# Delhi	1	1
# Kolkata	1	1
# Mumbai	1	1
# 2. index aur columns

# crosstab() mein:

# First argument (index) rows decide karta hai.
# Second argument (columns) columns decide karta hai.
# Values automatically combinations ki frequency count karti hain.

# Example:

# pd.crosstab(
#     df["Product"],
#     df["City"]
# )

# Ab Products rows mein aur Cities columns mein honge.

# 3. margins=True

# Agar row aur column totals bhi chahiye, toh margins=True use karte hain.

# result = pd.crosstab(
#     df["City"],
#     df["Product"],
#     margins=True
# )

# print(result)

# Isse All naam ki row aur column add ho jayegi, jisme totals honge.

# 4. normalize

# Agar frequency ke badle percentage chahiye, toh normalize use kar sakte hain.

# pd.crosstab(
#     df["City"],
#     df["Product"],
#     normalize="index"
# )

# normalize="index" har City ki row ka percentage 100% banata hai.

# normalize="columns" → Har Product column ka percentage 100%.
# normalize="all" → Puri table ka percentage 100%.

# Important difference:

# pivot_table()	crosstab()
# Numerical data ka sum, mean, max etc.	Category combinations ki frequency
# Aggregation reports	Frequency tables
# Practice Questions — Topic 5: crosstab()
# ==========================================
# Pandas Section 19 — Crosstab
# ==========================================

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Gender": ["Male", "Female", "Female", "Male", "Male", "Female"]
# })


# Q1.
# Create a frequency table showing City and Product.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Gender": ["Male", "Female", "Female", "Male", "Male", "Female"]
# })

# result = pd.crosstab(
#     df["City"],
#     df["Product"]
# )

# print(result)
#-------------------------------------------

# Q2.
# Create a frequency table showing Product as rows
# and Gender as columns.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Gender": ["Male", "Female", "Female", "Male", "Male", "Female"]
# })

# result = pd.crosstab(
#     df["Product"],
#     df["Gender"]
# )

# print(result)
#------------------------------------------------

# Q3.
# Create a frequency table showing City and Product
# with row and column totals.

# import pandas as pd

# df = pd.DataFrame({
#     "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
#     "Gender": ["Male", "Female", "Female", "Male", "Male", "Female"]
# })

# result = pd.crosstab(
#     df["City"],
#     df["Product"],
#     margins=True
# )

# print(result)
#----------------------------------------------------

# Q4.
# Create a frequency table showing City and Product
# with row-wise percentages.

import pandas as pd

df = pd.DataFrame({
    "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
    "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
    "Gender": ["Male", "Female", "Female", "Male", "Male", "Female"]
})

result = pd.crosstab(
    df["Product"],
    df["City"],
    normalize="index"
)

print(result)