import pandas as pd
import matplotlib.pyplot as plt


def monthly_chart(data):

    data["Date"] = pd.to_datetime(data["Date"])

    monthly = data.groupby(
        data["Date"].dt.month
    )["Amount"].sum()


    plt.plot(
        monthly.index,
        monthly.values,
        marker="o"
    )

    plt.title("Monthly Expense Trend")

    plt.xlabel("Month")
    plt.ylabel("Amount")

    plt.savefig("expense_trend.png")

    plt.close()

    print("Trend chart created!")