import matplotlib.pyplot as plt
dates = [ "Jan-01", "Jan-03", "Jan-05", "Jan-08", "Jan-10","Jan-13", "Jan-16", "Jan-20", "Jan-24", "Jan-29"]
amounts = [250, 180, 1500, 1200, 600,850, 450, 320, 900, 2000]
plt.plot(dates, amounts, marker="o")
plt.title("Monthly Expense")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.grid()
plt.savefig("linegraph.png")
plt.show()
print("Line graph created!")