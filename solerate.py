import sqlite3
from solders.keypair import Keypair
import base58

def generate_wallets(number_of_wallets):
    wallets = []
    for _ in range(number_of_wallets):
        keypair = Keypair()
        public_key = str(keypair.pubkey())
        private_key = base58.b58encode(bytes(keypair)).decode()
        wallets.append((public_key, private_key))
    return wallets
    

def distribute_sol():
    pass

def process_batch():
    pass

def distribute_to_wallets():
    pass

def collect_from_wallet():
    pass

def collect_from_all_wallets():
    pass

def main():
    while True:
        command = input("Enter a command: ").strip().lower()
        
        if command == "1":
            
            number_of_wallets = int(input("Enter the number of wallets to generate: "))
            if number_of_wallets <= 0:
                print("Invalid number of wallets")
                return
            wallets = generate_wallets(number_of_wallets)
            for i, (public_key, private_key) in enumerate(wallets):
                print(f"Wallet {i+1}:\nPublic Key: {public_key}\nPrivate Key: {private_key}\n")
                
        elif command == "2":
            pass
        elif command == "3":
            pass
        elif command == "4":
            pass
        elif command == "5":
            pass
        elif command == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please type 1 (Generate wallets), 2 (Distribute SOL), 3 (Process batch), 4 (Distribute to wallets), 5 (Collect from wallet), or 6 (Collect from all wallets).")
            
if __name__ == "__main__":
    main()