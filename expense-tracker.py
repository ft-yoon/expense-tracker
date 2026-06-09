from datetime import datetime, timedelta

FILE_NAME = "expenses.txt"


# ADD EXPENSES
def add_expenses():
    count = int(input("How many expenses do you want to add? "))

    for i in range(count):
        print(f"\nExpense {i+1}:")
        name = input("Expense name: ")
        amount = float(input("Amount: "))
        category = input("Category (Food/Travel/Shopping/etc): ")

        date = datetime.now().date()

        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{amount},{date},{category}\n")

    print("\n✅ Expenses added successfully!")


# VIEW EXPENSES
def view_expenses():
    print("\n📊 Choose view option:")
    print("1. Today")
    print("2. Last 7 days")
    print("3. Last 1 year")
    print("4. Total")

    option = input("Choose: ")

    today = datetime.now().date()
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

            if not lines:
                print("\n😅 No expenses yet!")
                return

            print("\n💸 Expenses:\n")

            for line in lines:
                parts = line.strip().split(",")

                # safe handling (prevents crash)
                if len(parts) != 4:
                    continue

                name, amount, date_str, category = parts
                amount = float(amount)
                date = datetime.strptime(date_str, "%Y-%m-%d").date()

                show = False

                if option == "1":
                    show = (date == today)

                elif option == "2":
                    show = (date >= today - timedelta(days=7))

                elif option == "3":
                    show = (date >= today - timedelta(days=365))

                elif option == "4":
                    show = True

                if show:
                    print(f"{name} - ₹{amount} | {category} | {date}")
                    total += amount

            print(f"\n💰 Total Spent: ₹{total}")

    except FileNotFoundError:
        print("\n😅 No file found. Add expenses first!")


# \MENU
def menu():
    while True:
        print("\n===== 💸 EXPENSE TRACKER =====")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expenses()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("👋 Bye! Keep tracking your money 💰")
            break

        else:
            print("❌ Invalid option")


menu()
