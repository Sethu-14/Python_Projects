import random


def main():
    print("Welcome to the Find The Number Game !!!")
    print("""Choose the game you want to play:
                1. User Find the number
                2. System find the Number
        """)
    n = 0

    while True:
        if n == 1 or n == 2:
            break
        else:
            n = int(input("Enter a valid number (1 or 2): "))

    if n == 1:
        game1()
    elif n == 2:
        game2()


def game1():
    range_int = int(input("Enter the Range of the Random number: "))
    number = random.randint(1, range_int)
    print("You have only 5 tries")

    for i in range(5):

        print(f"Try no: {i+1}")
        choice = int(input("Enter your Choice: "))

        if choice == number:
            print("You entered the correct number! YOU WON")
            break
        else:
            if i != 3:
                print("Wrong Choice! Try again")
            else:
                print("Wrong Choice! YOU LOST")

    exit()


def game2():
    range_int = int(input("Enter the Range of the Random number: "))
    x = int(input("Enter the no of Tries you allow: "))

    for i in range(x):

        print(f"Try no: {i+1}")
        print("")
        choice = random.randint(1, range_int)
        print(f"System Choice: {choice}")
        print("")
        print("Is the number in correct: ")
        print("Enter 't' for true")
        print("Enter 'f' for false")
        valid = input("Enter: ").lower()

        if valid == 't':
            print("SYSTEM WON")
            break
        else:
            if i != x-1:
                print("TRYING AGAIN")
            else:
                print("SYSTEM LOST")

    exit()


def exit():
    print("")
    print("Do you wanna play the game again press any key to play, 'q' to quit.")
    key = input().lower()
    if key != 'q':
        main()


main()
