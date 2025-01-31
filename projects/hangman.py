# Hangman in Python
import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

hangman_art = {
    0: """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    
    1: """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    
    2: """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    
    3: """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    
    4: """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    
    5: """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    
    6: """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
}

def display_man(wrong_guesses):
    """Displays the current hangman stage."""
    print(hangman_art[wrong_guesses])

def display_hint(hint):
    """Displays the current hint (word with guessed letters)."""
    print(" ".join(hint))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    
    print("Welcome to Hangman! 🎩")
    
    while wrong_guesses < 6:
        display_man(wrong_guesses)
        display_hint(hint)
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.add(guess)
        
        if guess in answer:
            print("✅ Correct!")
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess
        else:
            print("❌ Wrong guess!")
            wrong_guesses += 1
        
        if "_" not in hint:
            print("\n🎉 Congratulations! You guessed the word!")
            display_hint(hint)
            return
    
    display_man(6)
    print(f"💀 Game over! The word was: {answer}")

if __name__ == "__main__":
    main()
