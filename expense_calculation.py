def expense_details(data):

    total = data["Amount"].sum()
    average = data["Amount"].mean()
    highest = data["Amount"].max()
    lowest = data["Amount"].min()

    print("Total Expense:", total)
    print("Average Expense:", average)
    print("Highest Expense:", highest)
    print("Lowest Expense:", lowest)
    