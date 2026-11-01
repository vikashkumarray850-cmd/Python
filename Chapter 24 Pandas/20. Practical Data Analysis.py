# Section 20 — Practical Data Analysis

# Ye Pandas ka final section hai. Isme hum alag-alag Pandas methods 
# ko ek real Data Analyst workflow mein use karenge. 
# Ab har method ko alag se nahi padhenge; 
# business problems solve karenge.

# Section Overview

# | No. | Topic                    | Kya seekhenge?                                               |
# | --- | ------------------------ | ------------------------------------------------------------ |
# | 1   | Understanding a Dataset  | Dataset ko samajhna aur business questions identify karna    |
# | 2   | Data Preparation         | Analysis se pehle data ko ready karna                        |
# | 3   | Sales Analysis           | Total sales, average sales aur monthly performance nikalna   |
# | 4   | Product Analysis         | Best-selling products aur product performance identify karna |
# | 5   | Customer & City Analysis | Customer behaviour aur city-wise performance analyse karna   |
# | 6   | Business Insights        | Analysis ke results se meaningful conclusions nikalna        |
# | 7   | Final Practical Project  | Complete retail sales analysis karna                         |


# Topic 1 — Understanding a Dataset

# Data Analyst ko sabse pehle dataset samajhna hota hai. Code likhne se pehle ye clear hona chahiye ki dataset mein kaunsa data hai aur business ko kis question ka answer chahiye.

# Maan lo humein ek retail store ka sales dataset mila hai:

# # import pandas as pd

# # df = pd.DataFrame({
# #     "OrderID": [101, 102, 103, 104, 105, 106],
# #     "Date": ["2026-01-05", "2026-01-07", "2026-01-10",
# #              "2026-02-02", "2026-02-05", "2026-02-10"],
# #     "City": ["Kolkata", "Delhi", "Mumbai",
# #              "Kolkata", "Delhi", "Mumbai"],
# #     "Product": ["Laptop", "Mobile", "Laptop",
# #                 "Mobile", "Laptop", "Mobile"],
# #     "Quantity": [2, 3, 1, 4, 2, 5],
# #     "Price": [50000, 15000, 50000, 15000, 50000, 15000]
# # })

# # df["Sales"] = df["Quantity"] * df["Price"]
# Dataset ko kaise samjhein?
# Column	Meaning
# OrderID	Unique order number
# Date	Order ki date
# City	Jahan se order aaya
# Product	Sold product
# Quantity	Kitne units sell hue
# Price	Ek unit ki price
# Sales	Total sales amount
# Business Questions

# Is dataset se hum ye questions answer kar sakte hain:

# Total sales kitni hui?
# Kis city se sabse zyada sales hui?
# Kaunsa product sabse zyada sell hua?
# January aur February ki sales mein kya difference hai?
# Kis city mein Laptop ki sales zyada hui?

# Important: Data Analyst ka kaam sirf calculations karna nahi hai. 
# Business questions ko data ki help se answer karna hai.

# Pehle dataset ko samajhne ke liye ye commands run karo:

# print(df)
# print(df.shape)
# print(df.info())

# Inka output dekho. Abhi practice questions 
# nahi—pehle dataset aur business questions ko achhe se samajh lo.

# import pandas as pd

# df = pd.DataFrame({
#     "OrderID": [101, 102, 103, 104, 105, 106],
#     "Date": ["2026-01-05", "2026-01-07", "2026-01-10",
#              "2026-02-02", "2026-02-05", "2026-02-10"],
#     "City": ["Kolkata", "Delhi", "Mumbai",
#              "Kolkata", "Delhi", "Mumbai"],
#     "Product": ["Laptop", "Mobile", "Laptop",
#                 "Mobile", "Laptop", "Mobile"],
#     "Quantity": [2, 3, 1, 4, 2, 5],
#     "Price": [50000, 15000, 50000, 15000, 50000, 15000]
# })



# print(df)
# print(df.shape)
# print(df.info())
#_____________________________________________________________________________________________________

#==============================
# Topic 2 — Data Preparation
#==============================

# Data Preparation ka matlab hai analysis shuru karne 
# se pehle dataset ko analysis ke liye ready karna.

# Real-world datasets mein aksar ye problems hoti hain:

# Missing values
# Duplicate records
# Incorrect data types
# Extra spaces in text
# Incorrect date formats

# Hum inhe pehle seekh chuke hain. Ab unhe ek practical workflow mein apply karenge.

# Step 1 — Check Missing Values
# df.isna().sum()

# Isse har column mein missing values ki count pata chalegi.

# Step 2 — Check Duplicate Records
# df.duplicated().sum()

# Duplicate rows check hongi. Agar duplicates remove karne hain:

# df = df.drop_duplicates()
# Step 3 — Correct Data Types

# Date column ko datetime mein convert karo:

# df["Date"] = pd.to_datetime(df["Date"])
# Step 4 — Check Dataset Again
# df.info()
# df.head()

# Isse confirm kar sakte hain ki dataset analysis ke liye ready hai.

# Ek important baat: Har missing value ya duplicate ko blindly 
# remove mat karna. Pehle samjho ki woh data mein kyun hai. 
# Galat cleaning se analysis bhi galat ho sakta hai.

# Topic 2 ka main concept yahi hai: Clean data before analysing it.

# Jab samajh jao, bata dena.
#_____________________________________________________________________________________________________

#==============================
# Topic 3 — Sales Analysis
#==============================

# Sales Analysis mein hum business ki sales performance samajhte hain.

# Pichhle dataset mein Sales column already create kiya tha:

# df["Sales"] = df["Quantity"] * df["Price"]

# Ab isi column se business questions solve karenge.

# 1. Total Sales

# Business ki total revenue kitni hui?

# total_sales = df["Sales"].sum()

# print(total_sales)
# 2. Average Sales

# Har order ki average sales kitni hai?

# average_sales = df["Sales"].mean()

# print(average_sales)
# 3. City-wise Sales

# Har city se kitni sales hui?

# city_sales = df.groupby("City")["Sales"].sum()

# print(city_sales)
# 4. Monthly Sales

# Har month ki total sales kitni hui?

# Pehle Date se month extract karo:

# df["Month"] = df["Date"].dt.month

# Phir month-wise sales calculate karo:

# monthly_sales = df.groupby("Month")["Sales"].sum()

# print(monthly_sales)
# Dataset se calculation samjho
# Month	Total Sales
# January	₹2,00,000
# February	₹1,70,000

# Ye example nahi, hamare dataset ka actual calculation hai.

# Ek important difference:

# sum() — Total sales
# mean() — Average sales
# groupby() — Category ke according sales analysis

# Abhi in concepts ko samjho. Uske baad practice karenge.

#_____________________________________________________________________________________________________

#==============================
# Topic 4 — Product Analysis
#==============================

# Product Analysis mein hum dekhte hain ki kaun-se products 
# achha perform kar rahe hain aur kaun-se products ki sales kam hain.

# Hum wahi retail dataset use karenge.

# 1. Product-wise Total Sales

# Har product se kitni revenue generate hui?

# product_sales = df.groupby("Product")["Sales"].sum()

# print(product_sales)
# 2. Product-wise Quantity Sold

# Har product ke kitne units sell hue?

# product_quantity = df.groupby("Product")["Quantity"].sum()

# print(product_quantity)
# 3. Best-selling Product

# Sabse zyada quantity mein kaunsa product sell hua?

# best_product = df.groupby("Product")["Quantity"].sum().idxmax()

# print(best_product)

# idxmax() maximum value wali row ka index/label return karta hai. 
# Yahan woh product ka naam return karega.

# 4. Product-wise Multiple Calculations

# Ek hi report mein total sales aur total quantity dono nikal sakte hain:

# product_report = df.groupby("Product").agg({
#     "Sales": "sum",
#     "Quantity": "sum"
# })

# print(product_report)

# Is report se pata chalega:

# Har product ki total revenue.
# Har product ke total units sold.

# Yaad rakho: Sabse zyada quantity sell hone wala product zaroori 
# nahi ki sabse zyada revenue bhi generate kare. 
# Dono alag metrics hain

#_____________________________________________________________________________________________________

#===================================
# Topic 5 — Customer & City Analysis
#===================================

# Is topic mein hum samjhenge ki customers aur cities ke basis par
#  business performance kaise analyse karte hain.

# Abhi hamare dataset mein Customer column nahi hai, isliye pehle use add karte hain.

# df["Customer"] = [
#     "Amit", "Rahul", "Priya",
#     "Amit", "Rahul", "Priya"
# ]
# 1. Customer-wise Total Sales

# Har customer ne total kitni shopping ki?

# customer_sales = df.groupby("Customer")["Sales"].sum()

# print(customer_sales)
# 2. Customer-wise Order Count

# Har customer ne kitne orders place kiye?

# customer_orders = df.groupby("Customer")["OrderID"].count()

# print(customer_orders)
# 3. City-wise Product Sales

# Har city mein kis product ki kitni sales hui?

# city_product_sales = df.groupby(
#     ["City", "Product"]
# )["Sales"].sum()

# print(city_product_sales)
# 4. Highest Revenue Customer

# Sabse zyada revenue kis customer ne generate kiya?

# best_customer = df.groupby("Customer")["Sales"].sum().idxmax()

# print(best_customer)
# 5. City-wise Sales Report

# Ek report mein total sales aur total quantity dono:

# city_report = df.groupby("City").agg({
#     "Sales": "sum",
#     "Quantity": "sum"
# })

# print(city_report)

# Important difference:

# Customer Analysis: Kaun kitni shopping kar raha hai?
# City Analysis: Kis location se kitni sales aa rahi hain?
# City + Product Analysis: Kis city mein kaunsa product perform kar raha hai?
#_____________________________________________________________________________________________________

#==============================
# Topic 6 — Business Insights
#==============================

# Ab tak humne Sales, Product, Customer aur City Analysis seekha.

# Ab samjhenge ki in calculations se business ke liye useful conclusions kaise nikalte hain.

# 1. Highest Sales City
# city_sales = df.groupby("City")["Sales"].sum()

# highest_city = city_sales.idxmax()

# print(highest_city)

# Isse pata chalega ki kis city se sabse zyada revenue aa raha hai.

# 2. Lowest Sales City
# lowest_city = city_sales.idxmin()

# print(lowest_city)

# Isse pata chalega ki kis city ki sales sabse kam hai.

# 3. Highest Revenue Product
# product_sales = df.groupby("Product")["Sales"].sum()

# highest_product = product_sales.idxmax()

# print(highest_product)
# 4. Sales Contribution Percentage

# Kisi city ka total business sales mein kitna contribution hai?

# city_contribution = (
#     city_sales / df["Sales"].sum()
# ) * 100

# print(city_contribution)
# 5. Business Insight kaise likhein?

# Maan lo analysis se ye results mile:

# City	Sales
# Kolkata	₹1,30,000
# Delhi	₹1,20,000
# Mumbai	₹1,10,000

# Possible business insights:

# Kolkata generated the highest sales.
# Mumbai generated the lowest sales.
# The business can investigate why Mumbai's sales are lower.
# Marketing strategies can be reviewed city-wise.

# Ek important difference:

# Calculation batata hai kya hua, jabki Business Insight batata hai 
# result ka business ke liye kya meaning hai.

# Dhyan rahe: Sirf sales kam hone se ye prove nahi hota ki marketing weak hai.
# Uske liye additional data chahiye

#_____________________________________________________________________________________________________

#==================================
# Topic 7 — Final Practical Project
#==================================

# Ye Pandas ka final practical project hai. 
# Isme hum ek retail store ka complete sales analysis karenge.

# Project: Retail Store Sales Analysis

# Business Objective: Store ki sales performance, 
# product performance aur customer behaviour ko analyse karna.

# Step 1 — Dataset

# Pichhle topics wala df dataset hi use karenge. Usme ye columns hain:

# OrderID, Date, City, Product, Quantity, Price, Sales, Month, Customer

# Step 2 — Business Questions

# Humein in questions ke answers nikalne hain:

# What is the total revenue generated by the store?
# What is the average sales per order?
# Which city generated the highest revenue?
# Which product sold the highest quantity?
# Which product generated the highest revenue?
# Which customer generated the highest revenue?
# What are the monthly sales figures?
# Which city contributed the highest percentage of total sales?
# Step 3 — Final Report

# Analysis complete hone ke baad ek report banayenge jisme:

# Total revenue
# Average order sales
# Best-performing city
# Best-selling product
# Highest revenue customer
# Monthly sales
# City-wise sales contribution
# Step 4 — Practice

# Ab tum khud analysis karoge. Questions English mein hain, jaise tum prefer karte ho.

# ==========================================
# Final Pandas Project — Retail Sales Analysis
# ==========================================

Q1. Calculate the total revenue generated by the store.

total_revenue = df["Sales"].sum()
print(total_revenue)

Output: 220000

Q2. Calculate the average sales per order.

average_sales = df["Sales"].mean()
print(average_sales)

Output: 36666.67

Q3. Find the city with the highest total sales.

city_sales = df.groupby("City")["Sales"].sum()

highest_city = city_sales.idxmax()
print(highest_city)

Output: Kolkata

Q4. Find the product with the highest total quantity sold.

product_quantity = df.groupby("Product")["Quantity"].sum()

best_product = product_quantity.idxmax()
print(best_product)

Output: Mobile

Q5. Calculate total sales and total quantity for each product.

product_report = df.groupby("Product").agg({
    "Sales": "sum",
    "Quantity": "sum"
})

print(product_report)

Output:

Product	Sales	Quantity
Laptop	200000	5
Mobile	120000	12

Q6. Find the customer who generated the highest revenue.

customer_sales = df.groupby("Customer")["Sales"].sum()

best_customer = customer_sales.idxmax()
print(best_customer)

Output: Amit

Q7. Calculate total sales for each month.

monthly_sales = df.groupby("Month")["Sales"].sum()

print(monthly_sales)

Output:

Month	Sales
1	200000
2	120000

Q8. Calculate the percentage contribution of each city to the store's total sales.

city_sales = df.groupby("City")["Sales"].sum()

city_contribution = (city_sales / df["Sales"].sum()) * 100

print(city_contribution)

Output:

City	Contribution
Kolkata	54.55%
Delhi	27.27%
Mumbai	18.18%
Important correction

Upar ke answers mein Q1 ka revenue ₹3,20,000 hai, ₹2,20,000 nahi. 
Q5 mein Laptop sales ₹1,60,000 aur Mobile sales ₹1,80,000 hain. 
Q7 mein January ₹1,60,000 aur February ₹1,60,000 hain. 
Q8 mein Kolkata 50%, Delhi 25%, Mumbai 25% hain.

Ye corrected figures dataset ke actual calculations hain.



# Note: Ek-ek question solve karne ki zaroorat nahi.
#  Saare questions ek saath solve kar sakte ho. Agar kisi 
#  question mein dikkat aaye, usi question par ruk kar samjhenge.