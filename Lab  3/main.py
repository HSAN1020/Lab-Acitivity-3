from bank import Bank
from savingsaccount import SavingsAccount

def main():
    bank = Bank()
    while True:
        print("\nBank Menu:")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Compute interest for all accounts")
        print("5. Display all accounts")
        print("6. Remove account")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            pin = input("Enter PIN: ")
            balance = float(input("Enter initial balance: "))
            account = SavingsAccount(name, pin, balance)
            bank.add(account)
            print("Account created.")
        elif choice == "2":
            name = input("Enter name: ")
            pin = input("Enter PIN: ")
            account = bank.get(name, pin)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
                print("Deposit successful.")
            else:
                print("Account not found.")
        elif choice == "3":
            name = input("Enter name: ")
            pin = input("Enter PIN: ")
            account = bank.get(name, pin)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                result = account.withdraw(amount)
                if result:
                    print(result)
                else:
                    print("Withdrawal successful.")
            else:
                print("Account not found.")
        elif choice == "4":
            total_interest = bank.computeInterest()
            print(f"Total interest computed and deposited: {total_interest:.2f}")
        elif choice == "5":
            print("\nAccounts:")
            print(bank)
        elif choice == "6":
            name = input("Enter name: ")
            pin = input("Enter PIN: ")
            removed = bank.remove(name, pin)
            if removed:
                print("Account removed.")
            else:
                print("Account not found.")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
