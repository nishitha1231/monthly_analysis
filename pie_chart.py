import matplotlib.pyplot as plt

category = {
    "Food": 500,
    "Travel": 200,
    "Shopping": 1200
}

names = list(category.keys())
amounts = list(category.values())

plt.pie(amounts,labels=names,autopct="%1.1f%%")

plt.title("Expense Percentage")

plt.savefig("piechart.png", dpi=300)

plt.show()

print("Pie chart created!")