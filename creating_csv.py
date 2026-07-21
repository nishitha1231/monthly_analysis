import pandas as pd

df = pd.DataFrame({

    "Date": [
        "2026-01-01",
        "2026-01-02",
        "2026-01-03"
    ],

    "Category": [
        "Food",
        "Travel",
        "Shopping"
    ],

    "Amount": [
        500,
        200,
        1200
    ],

    "Description": [
        "Lunch",
        "Auto",
        "Clothes"
    ]

})

df.to_csv("data/expenses.csv", index=False)

print("CSV file created successfully!")