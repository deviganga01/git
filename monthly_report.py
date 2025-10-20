# Monthly Report Feature
print("=== Monthly Report Generator ===")

# Take input for income and expenses
income = float(input("Enter total income for the month: "))
expenses = float(input("Enter total expenses for the month: "))

# Calculate net balance
balance = income - expenses

# Display summary
print("\n--- Monthly Summary ---")
print("Total Income   :", income)
print("Total Expenses :", expenses)
print("Net Balance    :", balance)

# REVIEWER: Suggest adding input validation
