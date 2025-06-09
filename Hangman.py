import random

# List of sample words
words = ['python', 'hangman', 'electrical', 'engineer', 'algorithm']

# Choose a random word
word = random.choice(words)
guessed_letters = []
attempts = 6  # total wrong guesses allowed

print("🎯 Welcome to Hangman!")
print("_ " * len(word))

while attempts > 0:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠ Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess. Attempts left: {attempts}")

    # Show current state of the word
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '

    print(display_word)

    if '_' not in display_word:
        print("🎉 You won! The word was:", word)
        break
else:
    print("💀 Game Over! The word was:", word)