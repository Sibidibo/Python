

# ! Welcoming message for the user using a simple print funtion

def welcome_message():
    # create user name input??
    print("Hello. Welcome to the Expense Tracker!")

expenses = []

def printMenu():
    print("Enter 'log' to log an expense")
    print("Enter 'summary' to view expense summary")
    print("Enter 'exit' to quit the program")

#! Starting point for the interaction between the user and the program. It welcomes and asks the user to select the next step.
# A main function first displays the welcome message using 'welcome_message()' defined earlier. It then goes through a while loop
# with first a multiple choice input followed by specific input requests

def main():
    welcome_message()
    expenses = {
        "Food": [],
        "Clothing": [],
        "Entertainment": [],
        "Transport": [],
        "Rent": [],
        "Utilities": [],
        "Misc": []
    }
    while True:
        action = input("\nEnter 'log' to log an expense, 'summary' to view summary, or 'exit' to quit: ").lower()
        if action == 'log':
            log_expense(expenses)
        elif action == 'summary':
            view_summary(expenses)
        elif action == 'exit':
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

# ! This will start a new entry into the expenses

def log_expense(expenses):
    while True:
        category = input("Enter the expense category: ").strip()
        if category:
            if category not in expenses:
                print("Category not found in expenses. Please add a valid category.")
                continue
            break
        else:
            print("Category cannot be empty.")
    
    while True:
        description = input("Enter a description of the expense: ").strip()
        if description:
            break
        else:
            print("Description cannot be empty.")
    
    while True:
            amount = float(input("Enter the amount spent: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            break
    
# ! If the user selects 'summary' then this function will display all the expenses currently stored in the expenses dictionary

def view_summary(expenses):
    total_spent = 0
    print("\nExpense Summary:")
    for category, expense_list in expenses.items():
        category_total = sum(expense["amount"] for expense in expense_list)
        total_spent += category_total
        print(f"{category}: ${category_total:.2f}")
        for expense in expense_list:
            print(f"  - ${expense['amount']:.2f} on {expense['description']}")
    print(f"\nTotal Amount Spent: ${total_spent:.2f}")

def total_amount_spent(expenses):
    total_spent = sum(expense["amount"] for expense_list in expenses.values() for expense in expense_list)
    print(f"\nTotal Amount Spent: ${total_spent:.2f}")

if __name__ == "__main__":
    main()
