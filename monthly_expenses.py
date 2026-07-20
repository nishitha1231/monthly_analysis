import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/expenses.csv")

print(df)

print("\nFirst 5 Expenses:")
print(df.head())

print("\nInformation about Data:")
print(df.info())

print("\nExpense Summary:")
print(df.describe())
print("\nExpense Calculations:")

total_expense = df["Amount"].sum()
print("Total Expense:", total_expense)

highest_expense = df["Amount"].max()
print("Highest Expense:", highest_expense)

lowest_expense = df["Amount"].min()
print("Lowest Expense:", lowest_expense)

average_expense = df["Amount"].mean()
print("Average Expense:", average_expense)
print("\nCategory Wise Expenses:")

category_expense = df.groupby("Category")["Amount"].sum()

print(category_expense)
print("\nSorted Category Expenses:")

sorted_category = category_expense.sort_values(ascending=False)

print(sorted_category)
print("\nHighest Spending Category:")

highest_category = category_expense.idxmax()

print(highest_category)
print("\nConverting Date Column:")

df["Date"] = pd.to_datetime(df["Date"])

print(df.info())
print("\nAdding Month Column:")

df["Month"] = df["Date"].dt.month

print(df)
print("\nMonthly Expenses:")

monthly_expense = df.groupby("Month")["Amount"].sum()

print(monthly_expense)
print("\nDisplaying Category Expense Chart:")

category_expense.plot(kind="bar")

plt.title("Category Wise Expenses")

plt.xlabel("Category")

plt.ylabel("Amount")

plt.savefig("category_expenses.png")

print("Chart saved successfully!")
import pandas as pd
import matplotlib.pyplot as plt

# Read expense data
df = pd.read_csv("data/expenses.csv")

print("Expense Data:")
print(df)

# Total Expense
total_expense = df["Amount"].sum()

print("\nTotal Expense:")
print(total_expense)
# Category wise expense

category_expense = df.groupby("Category")["Amount"].sum()

print("\nCategory Wise Expense:")
print(category_expense)
# Highest spending category

highest_category = category_expense.idxmax()
highest_amount = category_expense.max()

print("\nHighest Spending Category:")
print(highest_category)

print("Amount Spent:")
print(highest_amount)
# Save category analysis to Excel

category_expense_df = category_expense.reset_index()

category_expense_df.to_excel(
    "expense_report.xlsx",
    index=False
)

print("\nExcel report created successfully!")
# Pie chart for category expenses

plt.figure(figsize=(7,7))

plt.pie(
    category_expense,
    labels=category_expense.index,
    autopct="%1.1f%%"
)

plt.title("Expense Percentage by Category")

plt.savefig("expense_percentage.png")

plt.savefig("expense_percentage.png")

print("Pie chart created successfully!")
# Monthly expense trend chart

df["Date"] = pd.to_datetime(df["Date"])

daily_expense = df.groupby("Date")["Amount"].sum()

plt.figure(figsize=(10,5))

plt.plot(
    daily_expense.index,
    daily_expense.values,
    marker="o"
)

plt.title("Daily Expense Trend")
plt.xlabel("Date")
plt.ylabel("Amount")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("expense_trend.png")

print("Trend chart created successfully!")