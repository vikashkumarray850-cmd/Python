#==================================
# Pandas — Section 1: Introduction
#==================================
# 1. Pandas kya hai?

# Pandas Python ki ek library hai jo mainly structured/tabular 
# data ke saath kaam karne ke liye use hoti hai.

# Simple example:

# Name      Age    City
# Vikash    25     Kolkata
# Mohit     24     Delhi
# Ravi      26     Mumbai

# Aise data ko Python mein efficiently handle karne ke liye Pandas bahut useful hai.

# Data Analyst Pandas se:

# Data read karta hai
# Data inspect karta hai
# Data filter karta hai
# Data clean karta hai
# Data sort karta hai
# Calculations karta hai
# Data ko group karta hai
# Different datasets ko combine karta hai
# 2. Pandas aur NumPy mein difference

# Tumne NumPy abhi complete kiya hai, isliye difference samajhna important hai.

# NumPy:

# import numpy as np

# marks = np.array([45, 67, 82, 39, 91])

# NumPy mainly numerical arrays aur numerical calculations ke liye powerful hai.

# Pandas:

# import pandas as pd

# data = pd.DataFrame({
#     "Name": ["Vikash", "Mohit", "Ravi"],
#     "Age": [25, 24, 26],
#     "City": ["Kolkata", "Delhi", "Mumbai"]
# })

# Pandas mainly rows + columns wale tabular data ke liye powerful hai.

# Simple rule:

# NumPy  → Numerical Array
# Pandas → Table / DataFrame
# 3. Pandas import karna

# Normally hum Pandas ko pd naam se import karte hain:

# import pandas as pd

# pd sirf ek short name hai.

# Jaise NumPy mein:

# import numpy as np

# waise Pandas mein:

# import pandas as pd
# 4. Pandas install karna

# Agar VS Code mein Pandas installed nahi hai, PowerShell terminal mein:

# pip install pandas

# Check karne ke liye:

# import pandas as pd

# print(pd.__version__)

# Agar version print ho gaya, Pandas properly installed hai.

# Pehla छोटा practice

# Abhi hum sirf installation/import concept check karenge. 
# Same NumPy ki tarah immediately 3 repetitive questions nahi karenge.

# ==========================================
# Pandas — Introduction Practice
# ==========================================

# Q1. Import the Pandas library using the alias "pd".
# Print the installed Pandas version.

import pandas as pd
print(pd.__version__)