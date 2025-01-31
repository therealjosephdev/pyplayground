# # Python slot Machine

# import random

# def spin_row():
#     symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    
#     return [random.choice(symbols) for _ in range(3)]

# def print_row(row):
#     print(" | ".join(row))

# def get_payout(row, bet):
#     if row[0] == row[1] == row[2]:
#         if row[0] == '🍒':
#             return bet * 3
#         elif row[0] == '🍉':
#             return bet * 4
#         elif row[0] == '🍋':
#             return bet * 5
#         elif row[0] == '🔔':
#             return bet * 10
#         elif row[0] == '⭐':
#             return bet * 20
#     return 0

# def main():
#     balance = 100
#     print("**************************")
#     print("Welcome to Python Slots!")
#     print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
#     print("**************************")
    
#     while balance > 0:
#         print(f"Current balance: ${balance}")
        
#         bet = input("Place your bet amount: ")
        
#         if not bet.isdigit():
#             print("Please enter a valid number")
#             continue
        
#         bet = int(bet)
        
#         if bet > balance:
#             print("Insufficient funds!")
#             continue
        
#         if bet <= 0:
#             print("Bet must be greater than zero!")
#             continue
        
#         balance -= bet
        
#         row = spin_row()
#         print("Spinning...\n")
#         print_row(row)
        
#         payout = get_payout(row, bet)
        
#         if payout > 0:
#             print(f"You won ${payout}")
#         else:
#             print("Sorry you lost this round")
            
#         balance += payout
        
#         play_again = input("Do you want to spin again? (Y/N): ").upper()
        
#         if play_again != 'Y':
#             break
        
#     print(f"Game over! Your final balance is ${balance}")

# if __name__ == '__main__':
#     main()
    
# Improved

import random
import time

SYMBOLS = {
    '🍒': 3,  # Cherry
    '🍉': 4,  # Watermelon
    '🍋': 5,  # Lemon
    '🔔': 10,  # Bell
    '⭐': 20,  # Star (Jackpot!)
    '💎': 50   # Diamond (Super Rare!)
}

ROWS = 3

def spin_reels():
    return [[random.choice(list(SYMBOLS.keys())) for _ in range(3)] for _ in range(ROWS)]

def print_machine(rows):
    print("\n🎰 Spinning... 🎰")
    time.sleep(1)
    
    for row in rows:
        print(" | ".join(row))
        time.sleep(0.5)
        
def get_payout(rows, bet):
    total_payout = 0
    
    for row in rows:
        if row[0] == row[1] == row[2]:
            total_payout += bet * SYMBOLS[row[0]]
            
    return total_payout

def main():
    balance = 100
    
    print("\n**************************")
    print("🎰 Welcome to Python Slots! 🎰")
    print("Match 3 symbols to win!")
    print("**************************\n")
    
    while balance > 0:
        print(f"💰 Current balance: ${balance}")
        
        try:
            bet = int(input("💵 Place your bet amount: $"))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue
        
        if bet > balance:
            print("❌ Insufficient funds!")
            continue
        if bet <= 0:
            print("❌ Bet must be greater than zero!")
            continue
        
        balance -= bet
        rows = spin_reels()
        print_machine(rows)
        
        payout = get_payout(rows, bet)
        
        if payout > 0:
            print(f"🎉 YOU WON ${payout}! 🎉")
            balance += payout
        else:
            print("😢 No match! Better luck next time.")
            
        if balance <= 0:
            print("💸 You're out of money! Game over.")
            break
        
        play_again = input("\n🔄 Do you want to spin again? (Y/N): ").strip().upper()
        if play_again != 'Y':
            break
        
    print(f"\n🎮 Game Over! Your final balance: ${balance}")
    
if __name__ == "__main__":
    main()