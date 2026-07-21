import pandas as pd

def read_expenses():

    data = pd.read_csv("data/expenses.csv")

    return data