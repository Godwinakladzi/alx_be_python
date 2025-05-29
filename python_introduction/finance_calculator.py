monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_saving = monthly_income - monthly_expenses
Projected_Savings = float(monthly_saving * 12) + float(monthly_saving * 12 * 0.05)
print(f'Your project saving after a year is {Projected_Savings}')