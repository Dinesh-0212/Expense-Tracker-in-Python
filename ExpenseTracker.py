import csv
import os
from datetime import datetime

# File to store expenses
EXPENSE_FILE = "expenses.csv"

# Ensure file exists with headers
if not os.path.exists(EXPENSE_FILE):
    with open(EXPENSE_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Description"])

# Function to add a new expense
def add_expense():
    try:
        amount = float(input("Enter amount spent: "))
        category = input("Enter category (Food, Transport, Entertainment, etc.): ").strip()
        description = input("Enter a brief description: ").strip()
        date = datetime.now().strftime("%Y-%m-%d")

        with open(EXPENSE_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, amount, category, description])
        
        print("Expense added successfully!\n")

    except ValueError:
        print("Invalid input. Please enter a valid number for amount.")

# Function to display all expenses
def view_expenses():
    try:
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.reader(file)
            expenses = list(reader)

            if len(expenses) == 1:
                print("No expenses recorded yet.\n")
                return
            
            print("\nExpense List:")
            print("-" * 50)
            for row in expenses[1:]:
                print(f"Date: {row[0]}, Amount: {row[1]}, Category: {row[2]}, Description: {row[3]}")
            print("-" * 50)
    
    except Exception as e:
        print(f"Error reading file: {e}")

# Function to show total and category-wise spending
def analyze_expenses():
    try:
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.reader(file)
            expenses = list(reader)

            if len(expenses) == 1:
                print("No expenses recorded yet.\n")
                return

            total = 0
            category_totals = {}

            for row in expenses[1:]:
                amount = float(row[1])
                category = row[2]
                total += amount
                category_totals[category] = category_totals.get(category, 0) + amount

            print(f"\nTotal Spending: ₹{total:.2f}")
            print("\nCategory-wise Spending:")
            for category, amount in category_totals.items():
                print(f"{category}: ₹{amount:.2f}")
            print()
    
    except Exception as e:
        print(f"Error processing expenses: {e}")

# Function to show monthly summary
def monthly_summary():
    try:
        month = input("Enter month (YYYY-MM): ").strip()

        with open(EXPENSE_FILE, "r") as file:
            reader = csv.reader(file)
            expenses = list(reader)

            monthly_total = 0
            monthly_expenses = []

            for row in expenses[1:]:
                if row[0].startswith(month):
                    monthly_total += float(row[1])
                    monthly_expenses.append(row)

            if not monthly_expenses:
                print("No expenses found for this month.\n")
                return

            print(f"\nExpenses for {month}:")
            print("-" * 50)
            for row in monthly_expenses:
                print(f"Date: {row[0]}, Amount: {row[1]}, Category: {row[2]}, Description: {row[3]}")
            print("-" * 50)
            print(f"Total for {month}: ₹{monthly_total:.2f}\n")

    except Exception as e:
        print(f"Error generating summary: {e}")

# Main menu
def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            analyze_expenses()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
