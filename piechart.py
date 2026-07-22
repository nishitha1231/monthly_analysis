import matplotlib.pyplot as plt
categories = ["Food","Travel","Shopping","Bills","Entertainment","Healthcare"]
amounts = [700, 500,2400,3200,600,850]
plt.figure(figsize=(7, 7))
plt.pie(amounts,labels=categories,autopct="%1.1f%%",startangle=90)
plt.title("Category Wise Expense Percentage")
plt.savefig("piechart.png", dpi=300)
plt.show()
print("Pie chart created successfully!")                                                                                                                                                              
