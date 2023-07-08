import random
import string

word_list = ['CAMERA', 'LAPTOP', 'PYTHON', 'ANDROID', 'WINDOWS', 'ELEPHANT', 'CHOICE', 'CHANGE',
             'DINOSAUR', 'BLIETOOTH', 'WASHING', 'ORANGE', 'SPOTIFY', 'DISCORD', 'TELEGRAM']

print(f"\nWelcome to the Hangman Game")


def main():
    x = input(f"\nPress any key to start the game, 'q' to quit the game: ")
    if x == 'q':
        return 0
    else:
        game()


def game():

    word_letters = list(random.choice(word_list))
    used_letters = []
    display = list('_'*len(word_letters))
    lives = 7
    while lives > 0:
        print(f"You have {lives} Lives.")
        print(f"\nGuess the letters \t", *display)
        guess = input("Enter your guess: ").upper()
        if guess not in used_letters:
            used_letters.append(guess)
        else:
            print(f"{guess} Letter already used")
        print("Used Letters: ", *used_letters)
        for i in range(len(word_letters)):
            if word_letters[i] == guess:
                display[i] = guess
        if guess not in word_letters:
            lives -= 1
        if word_letters == display:
            print(f"You have found the word, YOU WON")
            main()
    print("The Word is ", *word_letters)
    main()


main()
