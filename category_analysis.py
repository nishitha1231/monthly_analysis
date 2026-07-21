def category_expense(data):

    category = data.groupby("Category")["Amount"].sum()

    print("\nCategory Expenses:")
    print(category)

    return category