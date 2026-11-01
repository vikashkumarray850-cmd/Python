# ========================================
# CODE NUMBERING BY:-

# 1 concat()   [27 TO 165]
# 2 merge()    [169 TO 347]
# 3 Inner Join [351 TO 529] 
# 4 Left Join  [533 TO 699] 
# 5 Right Join [703 TO 878] 
# 6 Outer Join [882 TO 1066] 
# =========================================

#========================================
# Complete Topic Overview
#========================================
# | No. | Topic      | Kya seekhenge?                                 |
# | --- | ---------- | ---------------------------------------------- |
# | 1   | `concat()` | DataFrames ko rows ya columns ke through jodna |
# | 2   | `merge()`  | Common column ke basis par DataFrames jodna    |
# | 3   | Inner Join | Sirf matching records lena                     |
# | 4   | Left Join  | Left DataFrame ke sabhi records rakhna         |
# | 5   | Right Join | Right DataFrame ke sabhi records rakhna        |
# | 6   | Outer Join | Dono DataFrames ke sabhi records rakhna        |

#==================================
# Section 15: Combining DataFrames
#---------------------------------
# Topic 1: concat()
#==================================

# concat() ka use do ya zyada DataFrames ko rows ya 
# columns ke direction mein jodne ke liye hota hai.

# Example: Do alag months ke employee records ko ek DataFrame mein jodna.

# import pandas as pd

# january_data = pd.DataFrame({
#     "Employee": ["Amit", "Neha"],
#     "Salary": [25000, 30000]
# })

# february_data = pd.DataFrame({
#     "Employee": ["Ravi", "Priya"],
#     "Salary": [28000, 32000]
# })

# combined_data = pd.concat(
#     [january_data, february_data],
#     ignore_index=True
# )

# print(combined_data)

# Output:

#   Employee  Salary
# 0     Amit   25000
# 1     Neha   30000
# 2     Ravi   28000
# 3    Priya   32000

# Samjho:

# pd.concat() dono DataFrames ko jodta hai.
# Default mein rows ke direction mein jodta hai (axis=0).
# ignore_index=True naya continuous index 0, 1, 2, 3 banata hai.

# ignore_index=True karta kya hai?

# Iska simple meaning hai:

# “Purane DataFrames ke index ko ignore karo aur combined DataFrame ko naya continuous index do.”

# ignore_index=True → naya index banega: 0, 1, 2, 3
# ignore_index=False → purane index preserve honge; ye default behavior hai.
# Practice Questions — concat()
# ==========================================
# Pandas — Section 15: concat()
# ==========================================

# Q1. Create two DataFrames named morning_shift and evening_shift.
# morning_shift:
# Employee: ["Aman", "Riya"]
# Hours: [4, 5]
#
# evening_shift:
# Employee: ["Karan", "Pooja"]
# Hours: [6, 4]

# Combine both DataFrames row-wise and reset the index.
#-ANS
# import pandas as pd

# morning_shift = pd.DataFrame({
#     "Employee": ["Aman", "Riya"],
#     "Hours": [4, 5]
# })

# evening_shift = pd.DataFrame({
#     "Employee": ["Karan", "Pooja"],
#     "Hours": [6, 4]
# })

# combine_df = pd.concat(
#     [morning_shift, evening_shift],
#     ignore_index=True
# )

# print(combine_df)
#------------------------------------------------------------------

# Q2. Create two DataFrames named online_orders and store_orders.
# online_orders:
# OrderID: [101, 102]
# Amount: [500, 800]

# store_orders:
# OrderID: [103, 104]
# Amount: [650, 900]
#
# Combine both DataFrames row-wise and reset the index.

# import pandas as pd

# online_orders = pd.DataFrame({
#     "OrderID": [101, 102],
#     "Amount": [500, 800]
# })

# store_orders = pd.DataFrame({
#     "OrderID": [103, 104],
#     "Amount": [650, 900]   
# })

# combine_data = pd.concat(
#     [online_orders, store_orders],
#     ignore_index=True
# )
# print(combine_data)
#---------------------------------------------------------------

# Q3. Create two DataFrames named product_names and product_prices.
# product_names:
# Product: ["Mouse", "Keyboard", "Monitor"]
#
# product_prices:
# Price: [500, 1200, 7000]
#
# Combine both DataFrames column-wise.

# import pandas as pd

# product_names = pd.DataFrame({
#     "Product": ["Mouse", "Keyboard", "Monitor"]
# })

# product_prices = pd.DataFrame({
#    "Price": [500, 1200, 7000] 
# })

# both_data = pd.concat(
#     [product_names, product_prices],
#     axis=1
# )
# print(both_data)
#_____________________________________________________________________________________________________

#==============================
# Topic 2: merge()
#==============================

# Pehle ek important difference samjho:

# concat() — DataFrames ko rows ya columns ke through combine karta hai.
# merge() — do DataFrames ko kisi common column ki matching values ke basis par combine karta hai.
# 1. merge() kya hota hai?

# Maan lo tumhare paas do DataFrames hain.

# Employee information:

# import pandas as pd

# employees = pd.DataFrame({
#     "EmployeeID": [101, 102, 103],
#     "Name": ["Aman", "Riya", "Karan"]
# })
# EmployeeID	Name
# 101	Aman
# 102	Riya
# 103	Karan

# Employee salary:

# salaries = pd.DataFrame({
#     "EmployeeID": [101, 102, 103],
#     "Salary": [25000, 30000, 35000]
# })
# EmployeeID	Salary
# 101	25000
# 102	30000
# 103	35000

# Ab tumhe employee ka naam aur salary ek hi DataFrame mein chahiye.

# Dono DataFrames mein EmployeeID common column hai. Hum isi column ke through data combine karenge.

# 2. merge() kaise use karte hain?
# employee_details = pd.merge(
#     employees,
#     salaries,
#     on="EmployeeID"
# )

# print(employee_details)

# Output:

# Index	EmployeeID	Name	Salary
# 0	101	Aman	25000
# 1	102	Riya	30000
# 2	103	Karan	35000
# Code ko samjho
# pd.merge(employees, salaries, on="EmployeeID")
# employees — pehla DataFrame.
# salaries — doosra DataFrame.
# on="EmployeeID" — dono DataFrames mein matching EmployeeID ke basis par combine karna.

# Important: on mein wahi column dena hota hai jo dono DataFrames 
# mein common ho aur jiske basis par tum data match karna chahte ho.

# Agar common column ka naam alag-alag ho, 
# toh left_on aur right_on bhi use kar sakte hain. Woh baad mein dekhenge.

# 3. Data Analyst ke liye merge() kyu important hai?

# Maan lo tumhare paas alag-alag files hain:

# customers.csv — CustomerID, Name, City
# orders.csv — OrderID, CustomerID, Amount

# In dono ko CustomerID ke basis par merge karke tum 
# dekh sakte ho ki kis customer ne kitne amount ka order diya.

# Yahi kaam real-world data analysis mein bahut hota hai.

# Practice Questions — merge() Basic
# ==========================================
# Pandas — Section 15: merge() Basic
# ==========================================

# Q1. Create two DataFrames named employee_info and employee_salary.
#
# employee_info:
# EmployeeID: [101, 102, 103]
# Name: ["Aman", "Riya", "Karan"]
#
# employee_salary:
# EmployeeID: [101, 102, 103]
# Salary: [25000, 30000, 35000]
#
# Merge both DataFrames using EmployeeID.

# import pandas as pd

# employee_info = pd.DataFrame({
#     "EmployeeID": [101, 102, 103],
#     "Name": ["Aman", "Riya", "Karan"]    
# })

# employee_salary = pd.DataFrame({
#     "EmployeeID": [101, 102, 103],
#     "Salary": [25000, 30000, 35000]   
# })

# employee_details = pd.merge(
#     employee_info,
#     employee_salary,
#     on="EmployeeID"
# )

# print(employee_details)
#-----------------------------------------------------------------------]

# Q2. Create two DataFrames named customer_info and customer_orders.
#
# customer_info:
# CustomerID: [1, 2, 3]
# Name: ["Neha", "Rahul", "Priya"]
#
# customer_orders:
# CustomerID: [1, 2, 3]
# Amount: [500, 800, 1200]
#
# Merge both DataFrames using CustomerID.

# import pandas as pd

# customer_info = pd.DataFrame({
#     "CustomerID": [1, 2, 3],
#     "Name": ["Neha", "Rahul", "Priya"]
# })

# customer_orders = pd.DataFrame({
#     "CustomerID": [1, 2, 3],
#     "Amount": [500, 800, 1200]
# })

# merge_data = pd.merge(
#     customer_info,
#     customer_orders,
#     on = "CustomerID"
# )
# print(merge_data)
#-----------------------------------------------------------------

# Q3. Create two DataFrames named product_info and product_stock.
#
# product_info:
# ProductID: [201, 202, 203]
# Product: ["Mouse", "Keyboard", "Monitor"]
#
# product_stock:
# ProductID: [201, 202, 203]
# Stock: [50, 30, 20]
#
# Merge both DataFrames using ProductID.

# import pandas as pd

# product_info = pd.DataFrame({
#     "ProductID": [201, 202, 203],
#     "Product": ["Mouse", "Keyboard", "Monitor"]
# })

# product_stock = pd.DataFrame({
#     "ProductID": [201, 202, 203],
#     "Stock": [50, 30, 20]
# })

# Product_Details = pd.merge(
#     product_info,
#     product_stock,
#     on = "ProductID"
# )

# print(Product_Details)
#_____________________________________________________________________________________________________

#==============================
# Topic 3: Inner Join
#==============================

# 1. Inner Join kya hota hai?

# Inner Join sirf un records ko return karta hai jinki key dono DataFrames mein match karti hai.

# Maan lo hamare paas do DataFrames hain.

# DataFrame 1 — employees

# EmployeeID	Name
# 101	Aman
# 102	Riya
# 103	Karan

# DataFrame 2 — salaries

# EmployeeID	Salary
# 101	25000
# 103	35000
# 104	40000

# Ab IDs ko compare karo:

# EmployeeID	Employees mein?	Salaries mein?	Inner Join mein?
# 101	Haan	Haan	Haan
# 102	Haan	Nahi	Nahi
# 103	Haan	Haan	Haan
# 104	Nahi	Haan	Nahi

# Isliye final result mein sirf 101 aur 103 aayenge.

# 2. Python code
# import pandas as pd

# employees = pd.DataFrame({
#     "EmployeeID": [101, 102, 103],
#     "Name": ["Aman", "Riya", "Karan"]
# })

# salaries = pd.DataFrame({
#     "EmployeeID": [101, 103, 104],
#     "Salary": [25000, 35000, 40000]
# })

# result = pd.merge(
#     employees,
#     salaries,
#     on="EmployeeID",
#     how="inner"
# )

# print(result)

# Output:

# EmployeeID	Name	Salary
# 101	Aman	25000
# 103	Karan	35000
# Code mein kya naya hai?
# how="inner"
# how join ka type select karta hai.
# "inner" ka matlab sirf matching records.
# on="EmployeeID" batata hai ki matching kis column ke basis par karni hai.

# Important: pd.merge() mein how="inner" default hota hai. 
# Isliye tum how likhe bina bhi inner join kar sakte ho.

# 3. Data Analyst mein iska use

# Maan lo tumhare paas customers aur orders ki alag-alag files hain. 
# Tumhe sirf un customers ki details chahiye jinke orders ka record doosri file mein bhi available hai.

# Inner Join aise matching records nikalne mein kaam aata hai.

# Practice Questions — Inner Join
# ==========================================
# Pandas — Section 15: Inner Join
# ==========================================

# Q1. Create two DataFrames named student_info and exam_marks.
#
# student_info:
# StudentID: [1, 2, 3, 4]
# Name: ["Aman", "Riya", "Karan", "Neha"]
#
# exam_marks:
# StudentID: [1, 3, 5]
# Marks: [85, 90, 75]
#
# Perform an inner join using StudentID.

# import pandas as pd

# student_info = pd.DataFrame({
#     "StudentID": [1, 2, 3, 4],
#     "Name": ["Aman", "Riya", "Karan", "Neha"]
# })

# exam_marks = pd.DataFrame({
#     "StudentID": [1, 3, 5],
#     "Marks": [85, 90, 75]
# })

# Details = pd.merge(
#     student_info,
#     exam_marks,
#     on = "StudentID",
#     how = "inner"
# )
# print(Details)
#-----------------------------------------------------------

# Q2. Create two DataFrames named product_info and sales_info.
#
# product_info:
# ProductID: [101, 102, 103]
# Product: ["Mouse", "Keyboard", "Monitor"]
#
# sales_info:
# ProductID: [102, 103, 104]
# Sales: [20, 15, 10]
#
# Perform an inner join using ProductID.

# import pandas as pd

# product_info = pd.DataFrame({
#     "ProductID": [101, 102, 103],
#     "Product": ["Mouse", "Keyboard", "Monitor"]
# })

# sales_info = pd.DataFrame({
#     "ProductID": [102, 103, 104],
#     "Sales": [20, 15, 10]
# })

# Check_Joins = pd.merge(
#     product_info,
#     sales_info,
#     on = "ProductID",
#     how = "inner"
# )
# print(Check_Joins)
#------------------------------------------------------------------------

# Q3. Create two DataFrames named customer_details and payment_details.
#
# customer_details:
# CustomerID: [201, 202, 203, 204]
# Name: ["Amit", "Pooja", "Rahul", "Simran"]
#
# payment_details:
# CustomerID: [202, 204, 205]
# Amount: [1500, 2500, 3000]
#
# Perform an inner join using CustomerID.

# import pandas as pd

# customer_details = pd.DataFrame({
#     "CustomerID": [201, 202, 203, 204],
#     "Name": ["Amit", "Pooja", "Rahul", "Simran"]
# })

# payment_details = pd.DataFrame({
#     "CustomerID": [202, 204, 205],
#     "Amount": [1500, 2500, 3000]
# })

# Info = pd.merge(
#     customer_details,
#     payment_details,
#     on = "CustomerID",
#     how = "inner"
# )

# print(Info)
#_____________________________________________________________________________________________________

#==============================
# Topic 4: Left Join
#==============================

# | Rule                                 | Meaning                               |
# | ------------------------------------ | ------------------------------------- |
# | `how="left"`                         | Left DataFrame ke saare records rakho |
# | Matching record milta hai            | Right DataFrame ki value add hoti hai |
# | Matching record nahi milta           | Missing value ke liye `NaN` aata hai  |
# | Record sirf right DataFrame mein hai | Left Join mein woh record nahi aata   |


# Inner Join mein sirf matching records aaye the. Ab Left Join mein rule badlega.

# Left Join = Left DataFrame ke saare records + Right DataFrame se matching data.

# Example:

# Employees (Left DataFrame)

# EmployeeID	Name
# 101	Aman
# 102	Riya
# 103	Karan

# Salaries (Right DataFrame)

# EmployeeID	Salary
# 101	25000
# 103	35000
# 104	40000

# Code:

# result = pd.merge(
#     employees,
#     salaries,
#     on="EmployeeID",
#     how="left"
# )

# print(result)

# Output:

# EmployeeID	Name	Salary
# 101	Aman	25000
# 102	Riya	NaN
# 103	Karan	35000
# Riya ki salary mein NaN kyu aaya?

# Riya ka EmployeeID = 102 Employees DataFrame mein hai, 
# lekin Salaries DataFrame mein nahi hai.

# Left Join Riya ko remove nahi karta, kyunki woh left DataFrame mein hai. 
# Salary ka matching record nahi milne ke kaaran NaN aata hai.

# Yaad rakhna:

# how="inner" → sirf matching records.
# how="left" → left DataFrame ke sabhi records.

# Ab hum Left Join ke 3 practice questions karenge, phir Right Join par jayenge.

# ==========================================
# Pandas — Section 15: Left Join
# ==========================================

# Q1. Create two DataFrames named employee_info and salary_info.
#
# employee_info:
# EmployeeID: [101, 102, 103, 104]
# Name: ["Aman", "Riya", "Karan", "Neha"]
#
# salary_info:
# EmployeeID: [101, 103]
# Salary: [25000, 35000]
#
# Perform a left join using EmployeeID.

# import pandas as pd

# employee_info = pd.DataFrame({
#     "EmployeeID": [101, 102, 103, 104],
#     "Name": ["Aman", "Riya", "Karan", "Neha"]
# })

# salary_info = pd.DataFrame({
#     "EmployeeID": [101, 103],
#     "Salary": [25000, 35000]
# })

# result = pd.merge(
#     employee_info,
#     salary_info,
#     on="EmployeeID",
#     how="left"
# )

# print(result)
#-------------------------------------------------------------------

# Q2. Create two DataFrames named product_details and stock_details.
#
# product_details:
# ProductID: [201, 202, 203]
# Product: ["Mouse", "Keyboard", "Monitor"]
#
# stock_details:
# ProductID: [202, 203, 204]
# Stock: [30, 20, 10]
#
# Perform a left join using ProductID.

# import pandas as pd

# product_details = pd.DataFrame({
#     "ProductID": [201, 202, 203],
#     "Product": ["Mouse", "Keyboard", "Monitor"]
# })

# stock_details = pd.DataFrame({
#     "ProductID": [202, 203, 204],
#     "Stock": [30, 20, 10]
# })

# result = pd.merge(
#     product_details,
#     stock_details,
#     on="ProductID",
#     how="left"
# )

# print(result)
#----------------------------------------------------------

# Q3. Create two DataFrames named customer_info and order_info.
#
# customer_info:
# CustomerID: [1, 2, 3, 4]
# Name: ["Neha", "Rahul", "Priya", "Amit"]
#
# order_info:
# CustomerID: [1, 3]
# Amount: [500, 1200]
#
# Perform a left join using CustomerID.

# import pandas as pd

# customer_info = pd.DataFrame({
#     "CustomerID": [1, 2, 3, 4],
#     "Name": ["Neha", "Rahul", "Priya", "Amit"]
# })

# order_info = pd.DataFrame({
#     "CustomerID": [1, 3],
#     "Amount": [500, 1200]
# })

# result = pd.merge(
#     customer_info,
#     order_info,
#     on="CustomerID",
#     how="left"
# )

# print(result)
#_____________________________________________________________________________________________________

#==============================
# Topic 5: Right Join
#==============================

# 1. Right Join kya hota hai?

# Right Join mein right-side DataFrame ke saare records output mein aate hain. 
# Left DataFrame se sirf matching records ki information aati hai.

# Maan lo do DataFrames hain.

# Employees (Left DataFrame)

# EmployeeID	Name
# 101	Aman
# 102	Riya
# 103	Karan

# Salaries (Right DataFrame)

# EmployeeID	Salary
# 101	25000
# 103	35000
# 104	40000

# Yahan EmployeeID 104 sirf Salaries DataFrame mein hai.

# Right Join mein 104 ko bhi output mein rakha jayega, kyunki Salaries right-side DataFrame hai.

# 2. Python code
# import pandas as pd

# employees = pd.DataFrame({
#     "EmployeeID": [101, 102, 103],
#     "Name": ["Aman", "Riya", "Karan"]
# })

# salaries = pd.DataFrame({
#     "EmployeeID": [101, 103, 104],
#     "Salary": [25000, 35000, 40000]
# })

# result = pd.merge(
#     employees,
#     salaries,
#     on="EmployeeID",
#     how="right"
# )

# print(result)

# Output:

# EmployeeID	Name	Salary
# 101	Aman	25000
# 103	Karan	35000
# 104	NaN	40000
# Output ko samjho
# 101: Dono DataFrames mein hai, isliye Name aur Salary dono mil gaye.
# 103: Dono DataFrames mein hai, isliye Name aur Salary dono mil gaye.
# 104: Sirf Salaries mein hai, isliye Salary mil gayi lekin Name ke liye NaN aaya.
# 102: Employees mein hai, lekin Salaries mein nahi. Right Join mein woh output se hat gaya.
# 3. Left Join vs Right Join
# Join	Kaunse records preserve hote hain?
# how="left"	Left DataFrame ke saare records
# how="right"	Right DataFrame ke saare records

# Ek simple trick: pd.merge(left_df, right_df, ...) mein 
# how="right" ka matlab hai right_df ke saare records preserve karna.

# Practice Questions — Right Join
# ==========================================
# Pandas — Section 15: Right Join
# ==========================================

# Q1. Create two DataFrames named student_info and exam_results.
#
# student_info:
# StudentID: [1, 2, 3]
# Name: ["Aman", "Riya", "Karan"]
#
# exam_results:
# StudentID: [1, 3, 4]
# Marks: [85, 90, 75]
#
# Perform a right join using StudentID.

# import pandas as pd

# student_info = pd.DataFrame({
#     "StudentID": [1, 2, 3],
#     "Name": ["Aman", "Riya", "Karan"]
# })

# exam_results = pd.DataFrame({
#     "StudentID": [1, 3, 4],
#     "Marks": [85, 90, 75]
# })

# result = pd.merge(
#     student_info,
#     exam_results,
#     on="StudentID",
#     how="right"
# )

# print(result)

#------------------------------------------------------------

# Q2. Create two DataFrames named product_info and stock_info.
#
# product_info:
# ProductID: [101, 102, 103]
# Product: ["Mouse", "Keyboard", "Monitor"]
#
# stock_info:
# ProductID: [102, 103, 104]
# Stock: [30, 20, 10]
#
# Perform a right join using ProductID.

# import pandas as pd

# product_info = pd.DataFrame({
#     "ProductID": [101, 102, 103],
#     "Product": ["Mouse", "Keyboard", "Monitor"]
# })

# stock_info = pd.DataFrame({
#     "ProductID": [102, 103, 104],
#     "Stock": [30, 20, 10]
# })

# result = pd.merge(
#     product_info,
#     stock_info,
#     on="ProductID",
#     how="right"
# )

# print(result)

#------------------------------------------------------------

# Q3. Create two DataFrames named customer_info and payment_info.
#
# customer_info:
# CustomerID: [201, 202, 203]
# Name: ["Neha", "Rahul", "Priya"]
#
# payment_info:
# CustomerID: [201, 203, 204]
# Amount: [500, 1200, 800]
#
# Perform a right join using CustomerID.

# import pandas as pd

# customer_info = pd.DataFrame({
#     "CustomerID": [201, 202, 203],
#     "Name": ["Neha", "Rahul", "Priya"]
# })

# payment_info = pd.DataFrame({
#     "CustomerID": [201, 203, 204],
#     "Amount": [500, 1200, 800]
# })

# result = pd.merge(
#     customer_info,
#     payment_info,
#     on="CustomerID",
#     how="right"
# )

# print(result)
#_____________________________________________________________________________________________________

#==============================
# Topic 6: Outer Join
#==============================

# 1. Outer Join kya hota hai?

# Outer Join dono DataFrames ke saare records ko output mein rakhta hai, 
# chahe unki IDs match karein ya nahi.

# Maan lo hamare paas do DataFrames hain.

# Employees (Left DataFrame)

# EmployeeID	Name
# 101	Aman
# 102	Riya
# 103	Karan

# Salaries (Right DataFrame)

# EmployeeID	Salary
# 101	25000
# 103	35000
# 104	40000

# Ab IDs dekho:

# 101 — dono mein hai.
# 102 — sirf Employees mein hai.
# 103 — dono mein hai.
# 104 — sirf Salaries mein hai.

# Outer Join in chaaron IDs ko output mein rakhega.

# 2. Python code
# import pandas as pd

# employees = pd.DataFrame({
#     "EmployeeID": [101, 102, 103],
#     "Name": ["Aman", "Riya", "Karan"]
# })

# salaries = pd.DataFrame({
#     "EmployeeID": [101, 103, 104],
#     "Salary": [25000, 35000, 40000]
# })

# result = pd.merge(
#     employees,
#     salaries,
#     on="EmployeeID",
#     how="outer"
# )

# print(result)

# Output:

# EmployeeID	Name	Salary
# 101	Aman	25000.0
# 102	Riya	NaN
# 103	Karan	35000.0
# 104	NaN	40000.0
# 3. Output ko samjho
# 101: Dono DataFrames mein hai, isliye Name aur Salary dono mil gaye.
# 102: Sirf Employees mein hai, isliye Salary mein NaN aaya.
# 103: Dono DataFrames mein hai, isliye Name aur Salary dono mil gaye.
# 104: Sirf Salaries mein hai, isliye Name mein NaN aaya.

# how="outer" ka matlab hai ki kisi bhi DataFrame ka non-matching 
# record sirf match na hone ki wajah se remove nahi hoga.

# 4. Chaaron Join Types ka Comparison
# Join Type	Kaunse records preserve hote hain?
# how="inner"	Sirf matching records
# how="left"	Left DataFrame ke saare records
# how="right"	Right DataFrame ke saare records
# how="outer"	Dono DataFrames ke saare records

# Is comparison ko yaad rakho:

# Inner: Matching only
# Left: Left all
# Right: Right all
# Outer: Both all
# Practice Questions — Outer Join
# ==========================================
# Pandas — Section 15: Outer Join
# ==========================================

# Q1. Create two DataFrames named employee_info and department_info.
#
# employee_info:
# EmployeeID: [101, 102, 103]
# Name: ["Aman", "Riya", "Karan"]
#
# department_info:
# EmployeeID: [101, 103, 104]
# Department: ["IT", "Sales", "HR"]
#
# Perform an outer join using EmployeeID.

# import pandas as pd

# employee_info = pd.DataFrame({
#     "EmployeeID": [101, 102, 103],
#     "Name": ["Aman", "Riya", "Karan"]
# })

# department_info = pd.DataFrame({
#     "EmployeeID": [101, 103, 104],
#     "Department": ["IT", "Sales", "HR"]
# })

# result = pd.merge(
#     employee_info,
#     department_info,
#     on="EmployeeID",
#     how="outer"
# )

# print(result)
#----------------------------------------------------------

# Q2. Create two DataFrames named product_info and sales_info.
#
# product_info:
# ProductID: [201, 202, 203]
# Product: ["Mouse", "Keyboard", "Monitor"]
#
# sales_info:
# ProductID: [202, 203, 204]
# Sales: [30, 20, 10]
#
# Perform an outer join using ProductID.

# product_info = pd.DataFrame({
#     "ProductID": [201, 202, 203],
#     "Product": ["Mouse", "Keyboard", "Monitor"]
# })

# sales_info = pd.DataFrame({
#     "ProductID": [202, 203, 204],
#     "Sales": [30, 20, 10]
# })

# result = pd.merge(
#     product_info,
#     sales_info,
#     on="ProductID",
#     how="outer"
# )

# print(result)
#----------------------------------------------------------------

# Q3. Create two DataFrames named customer_info and payment_info.
#
# customer_info:
# CustomerID: [1, 2, 3, 4]
# Name: ["Neha", "Rahul", "Priya", "Amit"]
#
# payment_info:
# CustomerID: [1, 3, 5]
# Amount: [500, 1200, 800]
#
# Perform an outer join using CustomerID.

customer_info = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4],
    "Name": ["Neha", "Rahul", "Priya", "Amit"]
})

payment_info = pd.DataFrame({
    "CustomerID": [1, 3, 5],
    "Amount": [500, 1200, 800]
})

result = pd.merge(
    customer_info,
    payment_info,
    on="CustomerID",
    how="outer"
)

print(result)