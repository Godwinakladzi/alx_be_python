monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

monthly_saving = monthly_income - monthly_expenses
projected_savings = monthly_saving * 12 + monthly_saving * 12 * 0.05

print(f'Your projected savings after a year is ${projected_savings:.2f}')
