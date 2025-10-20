def get_user_input():
    incomes = list(map(int, input("Enter incomes separated by space: ").split()))
    expenses = list(map(int, input("Enter expenses separated by space: ").split()))
    return incomes, expenses

def calculate_summary(income, expenses):
    total_income = sum(income)
    total_expenses = sum(expenses)
    balance = total_income - total_expenses

    print("=== Monthly Summary ===")
    print(f"Total Income: ₹{total_income}")
    print(f"Total Expenses: ₹{total_expenses}")
    print(f"Balance: ₹{balance}")

incomes, expenses = get_user_input()
calculate_summary(incomes, expenses)
