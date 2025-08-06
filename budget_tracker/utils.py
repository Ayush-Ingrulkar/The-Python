import pandas as pd
import os
import matplotlib.pyplot as plt

def add_transaction(date, category, amount, trans_type, description, file_path='data/expenses.csv'):
    columns = ["Date", "Category", "Amount", "Type", "Description"]

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        df = pd.DataFrame(columns=columns)
        df.to_csv(file_path, index=False)
    else:
        df = pd.read_csv(file_path)

    new_row = {
        "Date": date,
        "Category": category,
        "Amount": amount,
        "Type": trans_type,
        "Description": description
    }

    new_df = pd.DataFrame([new_row])
    new_df = new_df[df.columns]
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv(file_path, index=False)
    print("Transaction added successfully.")

def view_summary(file_path='data/expenses.csv'):
    df = pd.read_csv(file_path)
    income = df[df['Type'] == 'Income']['Amount'].sum()
    expense = df[df['Type'] == 'Expense']['Amount'].sum()
    print(f"Total Income: ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Net Savings: ₹{income - expense}")

def visualize_expenses(file_path='data/expenses.csv'):
    df = pd.read_csv(file_path)

    if df.empty or 'Type' not in df.columns:
        print("No data available to visualize.")
        return

    expense_df = df[df['Type'] == 'Expense']
    if expense_df.empty:
        print("No expense data to visualize.")
        return

    category_sum = expense_df.groupby('Category')['Amount'].sum()
    category_sum.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title("Expense Distribution by Category")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

def monthly_summary(month, file_path='data/expenses.csv'):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[df['Date'].dt.strftime('%Y-%m') == month]

    if df.empty:
        print(f"No data for {month}.")
        return

    income = df[df['Type'] == 'Income']['Amount'].sum()
    expense = df[df['Type'] == 'Expense']['Amount'].sum()

    print(f"\n--- Summary for {month} ---")
    print(f"Income: ₹{income}")
    print(f"Expense: ₹{expense}")
    print(f"Saving: ₹{income - expense}")
