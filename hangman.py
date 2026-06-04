import random

words = ["python", "java", "apple", "house", "water"]

secret_word = random.choice(words)

guessed_letters = []

attempts = 6

print("Welcome to Hangman!")

while attempts > 0:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You won!")
        input("Press Enter to exit...")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Attempts Left:", attempts)

if attempts == 0:
    print("\nGame Over!")
    print("The word was:", secret_word)