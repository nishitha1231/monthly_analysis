import matplotlib.pyplot as plt

category = {
    "Food": 500,
    "Travel": 200,
    "Shopping": 1200
}

names = list(category.keys())
amounts = list(category.values())

plt.bar(names, amounts)

plt.title("Category Wise Expenses")
plt.xlabel("Category")
plt.ylabel("Amount")

plt.tight_layout()

plt.savefig("bargraph.png", dpi=300)

plt.show()


print("Bar graph created!")