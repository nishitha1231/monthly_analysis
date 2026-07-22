import pandas as pd
date = ["2026-01-01", "2026-01-03", "2026-01-05","2026-01-08", "2026-01-10", "2026-01-13","2026-01-16", "2026-01-20", "2026-01-24","2026-01-29"]
category = ["Food", "Travel", "Shopping","Bills", "Entertainment", "Healthcare","Food", "Travel", "Shopping", "Bills"]
amount = [500, 300, 1200,800, 600, 1500,450, 700, 900, 1000]
description = ["Lunch", "Bus Ticket", "Clothes","Electricity Bill", "Movie","Doctor Visit", "Dinner","Train Ticket", "Shoes","Internet Bill"]
expense_data = {
    "Date": date,
    "Category": category,
    "Amount": amount,
    "Description": description
}
expense_df = pd.DataFrame(expense_data)
expense_df.to_excel("expense_report.xlsx", index=False)
print("Expense report created successfully!")