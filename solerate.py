import sqlite3
from solders.keypair import Keypair
import base58

def initialize_db():
    conn = sqlite3.connect('wallets.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS wallets
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  public_key TEXT NOT NULL,
                  private_key TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def generate_wallets(number_of_wallets):
    wallets = []
    conn = sqlite3.connect('wallets.db')
    c = conn.cursor()
    for _ in range(number_of_wallets):
        keypair = Keypair()
        public_key = str(keypair.pubkey())
        private_key = base58.b58encode(bytes(keypair)).decode()
        c.execute("INSERT INTO wallets (public_key, private_key) VALUES (?, ?)", (public_key, private_key))
        wallets.append((public_key, private_key))
    conn.commit()
    conn.close()
    return wallets

def view_wallets():
    conn = sqlite3.connect('wallets.db')
    c = conn.cursor()
    c.execute("SELECT id, public_key, private_key FROM wallets")
    wallets = c.fetchall()
    conn.close()

    if not wallets:
        print("No wallets found in the database.")
    else:
        print("Wallets in the database:")
        for wallet in wallets:
            print(f"ID: {wallet[0]}\nPublic Key: {wallet[1]}\nPrivate Key: {wallet[2]}\n")

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
    initialize_db()
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
            view_wallets()       
        elif command == "3":
            distribute_sol()
        elif command == "4":
            process_batch()
        elif command == "5":
            distribute_to_wallets()
        elif command == "6":
            collect_from_wallet()
        elif command == "7":
            collect_from_all_wallets()
        elif command == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please type 1 (Generate wallets), 2 (View wallets), 3 (Distribute SOL), 4 (Process batch), 5 (Distribute to wallets), 6 (Collect from wallet), 7 (Collect from all wallets), or 8 (Exit).")
            
if __name__ == "__main__":
    main()