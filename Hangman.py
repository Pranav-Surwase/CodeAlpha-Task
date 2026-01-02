import random

# Step 1: Predefined word list
words = [
    "python", "java", "hangman", "coding", "program",
    "apple", "chair", "table", "water", "bread",
    "light", "mouse", "phone", "clock", "paper",
    "window", "garden", "school", "planet", "forest",
    "bridge", "market", "silver", "travel", "camera",
    "variable", "function", "compile", "syntax", "runtime"
]

# Step 2: Randomly select a word
word = random.choice(words)

# Step 3: Initialize variables
guessed_letters = []
attempts = 6

print("🎯 Welcome to Hangman Game!")
print("Guess the word letter by letter.")
print("You have 6 incorrect guesses allowed.\n")

# Step 4: Game loop
while attempts > 0:
    display_word = ""
    
    # Display current word state
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord:", display_word)
    print("Remaining attempts:", attempts)
    
    # Check if word is fully guessed
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly.")
        break
    
    # Take input
    guess = input("Enter a letter: ").lower()
    
    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet.")
        continue
    
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue
    
    # Add guess to guessed letters
    guessed_letters.append(guess)
    
    # Check guess
    if guess not in word:
        attempts -= 1
        print("❌ Wrong guess!")

# Step 5: Game Over
if attempts == 0:
    print("\n💀 Game Over!")
    print("The word was:", word)