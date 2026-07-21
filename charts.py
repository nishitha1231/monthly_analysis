import matplotlib.pyplot as plt


def create_charts(category):

    # Bar chart
    category.plot(kind="bar")

    plt.title("Category Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.savefig("category_expenses.png")

    plt.close()


    # Pie chart
    plt.pie(
        category,
        labels=category.index,
        autopct="%1.1f%%"
    )

    plt.title("Expense Percentage")

    plt.savefig("expense_percentage.png")

    plt.close()

    print("Charts created!")