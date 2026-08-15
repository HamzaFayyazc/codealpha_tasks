import random

def play_hangman():
    # 1. Predefined words list (as per guidelines)
    words = ["python", "code", "alpha", "script", "logic"]
    secret_word = random.choice(words)
    
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6
    
    print("--- Welcome to Hangman Game ---")
    
    while incorrect_guesses < max_attempts:
        # Secret word ka current status show karna (e.g., p _ t h o n)
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\nWord:", display_word.strip())
        print(f"Remaining Incorrect Guesses: {max_attempts - incorrect_guesses}")
        print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")
        
        # Checking win condition (agar saare letters guess ho chuke hain)
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word correctly!")
            break
            
        # User input handling
        guess = input("Guess a letter: ").lower().strip()
        
        # Validations
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.")
            continue
            
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter. Try another one!")
            continue
            
        guessed_letters.append(guess)
        
        # Check if guess is correct or wrong
        if guess in secret_word:
            print("✅ Good guess!")
        else:
            print("❌ Wrong guess!")
            incorrect_guesses += 1
            
    # Lose condition
    if incorrect_guesses == max_attempts:
        print(f"\n❌ Game Over! You've used all 6 attempts. The word was: '{secret_word}'")

if __name__ == "__main__":
    play_hangman()