def create_excel(category):

    category.to_excel(
        "expense_report.xlsx"
    )

    print("Excel report created!")