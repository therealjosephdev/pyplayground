import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

plain_text = input("Enter a text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    
print(f"\n🔐 Original message: {plain_text}")
print(f"🔒 Encrypted message: {cipher_text}")

decrypted_text = ""

for letter in cipher_text:
    index = key.index(letter)
    decrypted_text += chars[index]
    
print(f"\n🔓 Decrypted message: {decrypted_text}")