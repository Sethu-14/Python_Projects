import random


u_name = input("Enter your name : ")
play = ["stone", "scissor", "paper"]
b = random.choice(play)

while True:
    want2play = input(
    "Press any key to start, 'q' to quit. ").lower()
    if want2play == 'q':
        break
    while True:
        user_choice = input(
            "Enter your choice ('st' for stone), ('p' for paper), ('sc' for scissor). ")
        if user_choice.lower() == "st":
            user_choice = "stone"
            break
        elif user_choice.lower() == "p":
            user_choice = "paper"
            break
        elif user_choice.lower() == "sc":
            user_choice = "scissor"
            break
        else:
            print("Please enter a valid option.")

    a = user_choice
    print(f"Your choice is {user_choice}")
    print(f"System chose is {b}")

    if (a == "stone" and b == "scissor") or (a == "paper" and b == "stone") or (a == "scissor" and b == "paper"):
        print(f"{u_name} Won !!!")
    elif (a == "stone" and b == "stone") or (a == "scissor" and b == "scissor") or (a == "paper" and b == "paper"):
        print("Game Tie ...")
    else:
        print("System Won ...")
