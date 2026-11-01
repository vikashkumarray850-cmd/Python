import pandas as pd

df = pd.DataFrame({
    "City": ["Kolkata", "Delhi", "Kolkata", "Delhi", "Mumbai", "Mumbai"],
    "Product": ["Laptop", "Mobile", "Mobile", "Laptop", "Laptop", "Mobile"],
    "Sales": [50000, 30000, 20000, 40000, 60000, 25000],
    "Quantity": [2, 3, 4, 2, 5, 3]
})

result = pd.pivot_table(
    df,
    index= "City",
    values= ["Sales", "Quantity"],
    aggfunc= "sum"
)
print(result)