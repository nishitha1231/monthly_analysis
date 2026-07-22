import matplotlib.pyplot as plt
category = ["Food", "Travel", "Shopping", "Bills", "Entertainment","Healthcare", "Food", "Travel", "Shopping", "Bills"]
amount = [500, 300, 1200, 800, 600, 1500, 450, 700, 900, 1000]
plt.bar(category, amount)
plt.title("Category Wise Expenses")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("bargraph.png", dpi=300)
plt.show()
print("Bar graph created successfully!")