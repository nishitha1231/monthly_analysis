from read_data import read_expenses
from expense_calculation import expense_details
from category_analysis import category_expense
from excel_report import create_excel
from charts import create_charts
from monthly_trend import monthly_chart


data = read_expenses()

print(data)


expense_details(data)


category = category_expense(data)


create_excel(category)


create_charts(category)


monthly_chart(data)


print("Expense Analysis Completed!")