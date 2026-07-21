import pandas as pd

data = {
    "Category": ["Food", "Travel", "Shopping"],
    "Amount": [500, 200, 1200]
}

category = pd.DataFrame(data)

category.to_excel("expense_report.xlsx", index=False)

print("Excel report created!")