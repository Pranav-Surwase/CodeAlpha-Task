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

