from utils import (
    add_transaction,
    view_summary,
    visualize_expenses,
    monthly_summary
)

def menu():
    while True:
        print("\n--- Budget Expense Tracker ---")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. Visualize Expenses (Pie Chart)")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Category: ")
            amount = float(input("Amount: "))
            trans_type = input("Type (Income/Expense): ")
            description = input("Description: ")

            add_transaction(date, category, amount, trans_type, description)

        elif choice == '2':
            view_summary()

        elif choice == '3':
            visualize_expenses()

        elif choice == '4':
            month = input("Enter month in YYYY-MM format (e.g., 2025-08): ")
            monthly_summary(month)

        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

menu()
