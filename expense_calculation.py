date = ["2026-01-01", "2026-01-02", "2026-01-03"]

category = ["Food", "Travel", "Shopping"]

amount = [500, 200, 1200]

description = ["Lunch", "Auto", "Clothes"]


total = sum(amount)

average = total / len(amount)

highest = max(amount)

lowest = min(amount)


print("Total Expense:", total)
print("Average Expense:", average)
print("Highest Expense:", highest)
print("Lowest Expense:", lowest)