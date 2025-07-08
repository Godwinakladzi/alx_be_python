# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount()  # Start with zero balance

    if len(sys.argv) < 2:
        print("Usage: deposit <amount> | withdraw <amount> | balance")
        sys.exit(1)

    operation = sys.argv[1].lower()

    if operation == "deposit" and len(sys.argv) == 3:
        try:
            amount = float(sys.argv[2])
            account.deposit(amount)
            account.display_balance()
        except ValueError:
            print("Please enter a valid number for amount.")
    
    elif operation == "withdraw" and len(sys.argv) == 3:
        try:
            amount = float(sys.argv[2])
            success = account.withdraw(amount)
            if success:
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
            account.display_balance()
        except ValueError:
            print("Please enter a valid number for amount.")

    elif operation == "balance":
        account.display_balance()

    else:
        print("Invalid command or arguments.")
        print("Usage: deposit <amount> | withdraw <amount> | balance")

if __name__ == "__main__":
    main()
