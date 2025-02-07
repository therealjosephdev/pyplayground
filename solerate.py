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

def generate_wallets():
    try:
        number_of_wallets = int(input("Enter the number of wallets to generate: ").strip())
        
        if number_of_wallets <= 0:
            print("⚠️ Invalid number of wallets. Please enter a positive number.")
            return

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

        print(f"✅ {len(wallets)} wallet(s) generated successfully!")
        for i, (public_key, private_key) in enumerate(wallets, 1):
            print(f"\nWallet {i}:\nPublic Key: {public_key}\nPrivate Key: {private_key}")

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")
    except Exception as e:
        print(f"❌ Error generating wallets: {e}")

def import_wallets():
    private_key = input("Enter the private key: ").strip()

    if not private_key:
        print("⚠️ Private key cannot be empty.")
        return

    try:
        private_key_bytes = base58.b58decode(private_key)
        
        if len(private_key_bytes) != 64:
            print("❌ Invalid private key length! A valid Solana private key must be 64 bytes.")
            return


        keypair = Keypair.from_bytes(private_key_bytes)
        wallet_address = str(keypair.pubkey())

        conn = sqlite3.connect('wallets.db')
        c = conn.cursor()

        c.execute("SELECT private_key FROM wallets WHERE public_key = ?", (wallet_address,))
        existing = c.fetchone()

        if existing:
            if existing[0] == private_key:
                print(f"⚠️ Wallet already exists!\nPublic Key: {wallet_address}")
            else:
                print(f"❌ Conflict: This public key is already in the database, but with a different private key!")
        else:
            c.execute("INSERT INTO wallets (public_key, private_key) VALUES (?, ?)", (wallet_address, private_key))
            conn.commit()
            print(f"✅ Wallet imported successfully!\nPublic Key: {wallet_address}")

        conn.close()

    except ValueError:
        print("❌ Invalid private key format! Make sure it's a valid Base58 string.")
    except Exception as e:
        print(f"❌ Error importing wallet: {e}")

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

def handle_commands():
    while True:
        command = input("Enter a command: ").strip().lower()
        
        if command == "1":
            generate_wallets()
        elif command == "2":
            import_wallets()
        elif command == "3":
            view_wallets()       
        elif command == "4":
            distribute_sol()
        elif command == "5":
            process_batch()
        elif command == "6":
            distribute_to_wallets()
        elif command == "7":
            collect_from_wallet()
        elif command == "8":
            collect_from_all_wallets()
        elif command == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please type 1 (Generate wallets), 2 (Import wallets), 3 (View wallets), 4 (Distribute SOL), 5 (Process batch), 6 (Distribute to wallets), 7 (Collect from wallet), 8 (Collect from all wallets), or 9 (Exit).")

def main():
    initialize_db()
    handle_commands()

if __name__ == "__main__":
    main()
