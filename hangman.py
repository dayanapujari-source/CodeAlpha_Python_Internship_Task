import random

words = ["python", "apple", "banana", "computer", "school"]
word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman Game!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)

    letter = input("Enter a letter: ").lower()

    if letter in used_letters:
        print("You already guessed that letter!")
        continue

    used_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong!")

if "_" not in guessed:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)