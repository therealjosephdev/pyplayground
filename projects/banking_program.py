# Python Banking Program

# def show_balance(balance):
#     print(f"Your balance is ${balance:.2f}")

# def deposit():
#     amount = float(input("Enter an amount to be deposited: "))
    
#     if amount < 0:
#         print("That's not a valid amount")
#         return 0
#     else:
#         return amount
    
# def withdraw(balance):
#     amount = float(input("Enter an amount to be withdrawn: "))
    
#     if amount > balance:
#         print("Insufficient funds")
#         return 0
#     elif amount < 0:
#         print("Amount must be greater than 0")
#         return 0
#     else:
#         return amount

# def main():
#     balance = 0
#     is_running = True

#     while is_running:
#         print("Banking Program!")
#         print("1. Show Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")
        
#         choice = input("Enter your choice (1-4): ")
        
#         if choice == "1":
#             show_balance(balance)
#         elif choice == "2":
#             balance += deposit()
#         elif choice == "3":
#             balance -= withdraw(balance)
#         elif choice == "4":
#             is_running = False
#         else:
#             print("That is not a valid choice")

#     print("Thank you! Have a nice day!")

# if __name__ == '__main__':
#     main()

# Improved

import time

balance = 0.0
transactions = []
interest_rate = 5.0

def show_balance():
    """Displays the current balance."""
    print(f"\n💰 Your balance is: ${balance:.2f}")

def deposit():
    """Handles deposits and logs transaction."""
    global balance
    amount = float(input("\nEnter an amount to deposit: $"))
    
    if amount <= 0:
        print("❌ Invalid amount. Deposit must be greater than 0.")
        return
    
    balance += amount
    transactions.append(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] +${amount:.2f} (Deposit)")
    print(f"✅ Deposited ${amount:.2f} successfully!")

def withdraw():
    """Handles withdrawals and logs transaction."""
    global balance
    amount = float(input("\nEnter an amount to withdraw: $"))
    
    if amount <= 0:
        print("❌ Invalid amount. Withdrawal must be greater than 0.")
        return
    if amount > balance:
        print("❌ Insufficient funds!")
        return

    balance -= amount
    transactions.append(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] -${amount:.2f} (Withdrawal)")
    print(f"✅ Withdrawn ${amount:.2f} successfully!")

def show_transaction_history():
    """Displays all past transactions."""
    print("\n📜 Transaction History:")
    if not transactions:
        print("No transactions yet!")
    else:
        for transaction in transactions:
            print(transaction)

def apply_interest():
    """Calculates and applies interest over a period of time."""
    global balance
    years = int(input("\nEnter the number of years for interest calculation: "))
    
    if years <= 0:
        print("❌ Enter a valid number of years!")
        return

    final_amount = balance * ((1 + (interest_rate / 100)) ** years)
    interest_earned = final_amount - balance
    balance = final_amount

    transactions.append(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] +${interest_earned:.2f} (Interest Earned)")
    print(f"📈 After {years} years, your balance will be: ${final_amount:.2f} (Interest Earned: ${interest_earned:.2f})")

def banking_menu():
    """Main banking menu."""
    global balance
    while True:
        print("\n🏦 Welcome to Python Bank!")
        print("1️⃣ Show Balance")
        print("2️⃣ Deposit Money")
        print("3️⃣ Withdraw Money")
        print("4️⃣ Show Transaction History")
        print("5️⃣ Apply Interest")
        print("6️⃣ Exit")

        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            show_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            show_transaction_history()
        elif choice == "5":
            apply_interest()
        elif choice == "6":
            print("👋 Thank you for using Python Bank! Have a great day!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    banking_menu()