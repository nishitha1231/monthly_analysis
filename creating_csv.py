import pandas as pd
data = {
    "Date": ["2026-01-01", "2026-01-03", "2026-01-05", "2026-01-08", "2026-01-10", "2026-01-13", "2026-01-16", "2026-01-20", "2026-01-24", "2026-01-29"],
    "Category": ["Food","Travel","Shopping","Bills","Entertainment","Healthcare","Food","Travel","Shopping","Bills"],
    "Amount": [250,180,1500,1200,600,850,450,320,900,2000],
    "Description": ["Breakfast","Bus Fare","Clothes","Electricity Bill","Movie Ticket","Medicines","Dinner","Cab Fare","Groceries","House Rent"]
}
df = pd.DataFrame(data)
df.to_csv("data/expenses.csv", index=False)
print (df)
print("CSV file created successfully!")