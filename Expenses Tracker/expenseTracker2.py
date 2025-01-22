expenses = []
expense1 = {'amount': 100, 'description': 'Coffee', 'category': 'Food'}
expenses.append(expense1)
expense2 = {'amount': 200, 'description': 'Shirt', 'category': 'Clothing'}
expenses.append(expense2)


def printMenu():
    print("Please choose from the follwing:")
    print("1. Add an expense")
    print("2. Remove an expense")
    print("3. View all expenses")
    print("4. Total amaount spent")
    print("5. Total amount spent per category")
    print("6. Exit")

def addExpense(amount, description, category):
    expense = {"amount": amount, "description": description, 'category': category}
    expenses.append(expense)

def removeExpense():
    while True:
        listExpenses()
        print("Please choose the expense you would like to delete:")
        try:
            expenseToDelete = int(input("> "))
            del expenses[expenseToDelete]
            break
        except:
            print("Invalid input. Please try again.")
            continue
        print("\n\n")
        

def listExpenses():
    print("Here are your Expenses:")
    print(".......................")
    counter = 0
    for expense in expenses:
        print("#", counter, "-", expense['amount'], "-", expense['description'], "-", expense['category'])
        counter += 1
    print("\n\n")

def amountSpent():
    total = sum(expense['amount'] for expense in expenses)
    print(f"You have spent a total of {total}")
    print("\n\n")

def amountPerCategory():
    categories = {}
    counter = 0
    for expense in expenses:
        if expense['category'] not in categories:
            categories[expense['category']] = 0
        categories[expense['category']] += expense['amount']
    for category, total in categories.items():
        print(f"You have spent {total} on {category}")
        counter += 1
    print("\n\n")

if __name__ == '__main__':
    while True:
        printMenu()
        choice = input("> ")
        if choice == '1':
            print("How much did you spend?")
            while True:
                try:
                    amountToAdd = float(input("> "))
                    break
                except:
                    print("Invalid input. Please try again.")

            print("What did you buy?")
            while True:
                try:
                    descriptionToAdd = input("> ")
                    break
                except:
                    print("Invalid input. Please try again.")

            print("What category is it from?")
            while True:
                try:
                    categoryToAdd = input("> ")
                    break
                except:
                    print("Invalid input. Please try again.")

            addExpense(amountToAdd, descriptionToAdd, categoryToAdd)
        elif choice == '2':
            removeExpense()
        elif choice == '3':
            listExpenses() 
        elif choice == '4':
            amountSpent()
        elif choice == '5':
            amountPerCategory()
        elif choice == '6':
            break
        else:
            print("Invalid input. Please try again.")
            continue
        