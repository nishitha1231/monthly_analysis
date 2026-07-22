date = ["2026-01-01", "2026-01-03", "2026-01-05", "2026-01-08", "2026-01-10","2026-01-13", "2026-01-16", "2026-01-20", "2026-01-24", "2026-01-29"]
category = ["Food", "Travel", "Shopping", "Bills", "Entertainment","Healthcare", "Food", "Travel", "Shopping", "Bills"]
amount = [250, 180, 1500, 1200, 600,850, 450, 320, 900, 2000]
description = ["Breakfast", "Bus Fare", "Clothes", "Electricity Bill", "Movie Ticket","Medicines", "Dinner", "Cab Fare", "Groceries", "House Rent"]
total = sum(amount)
average = total / len(amount)
highest = max(amount)
lowest = min(amount)
print("Total Expense:", total)
print("Average Expense:", average)
print("Highest Expense:", highest)
print("Lowest Expense:", lowest)