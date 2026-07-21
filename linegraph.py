import matplotlib.pyplot as plt

months = ["January", "February", "March"]

expenses = [500, 200, 1200]


plt.plot(months, expenses, marker="o")

plt.title("Monthly Expense")

plt.xlabel("Month")
plt.ylabel("Amount")

plt.grid()

plt.savefig("linegraph.png")

plt.show()

print("Line graph created!")