from random import randint

print("\nWelcome to the Number Guessing Game")

play = True

while play:
    # Choose a difficulty
    while True:
        print("\nChoose Difficulty:")
        print("1. Easy", "  2. Medium", "  3. Hard\n")

        try:
            pick = int(input("Pick 1, 2 or 3: "))
        except ValueError:
            print("\nPick a number")
        else:
            parameters = [
                {"attempts": 7, "maximum": 20, "used_value": 8},
                {"attempts": 6, "maximum": 50, "used_value": 7},
                {"attempts": 5, "maximum": 100, "used_value": 6},
            ]

            if 1 <= pick <= 3:
                attempts = parameters[pick - 1]["attempts"]
                maximum = parameters[pick - 1]["maximum"]
                used_value = parameters[pick - 1]["used_value"]
                break
            else:
                print("Input is invalid")

    print(f"\nYou have {attempts} attempts to guess the number between 1 and {maximum}\n")

    # Guess a number
    secret_number = randint(1, maximum)

    while attempts > 0:
        try:
            number = int(input("Guess a number: "))
        except ValueError:
            print("You have to input a number")
        else:
            closeness = abs(secret_number - number)

            if number == secret_number:
                print("That's correct!")
                print(f"You used {used_value - attempts} attempts to guess the number\n")
                break
            elif closeness <= 5:
                print("You are very close!\n")
            elif closeness <= 10:
                print("Getting close!\n")
            elif closeness <= 20:
                print("Number not too far!\n")
            elif closeness >= 21:
                print("You are too far!\n")

            attempts -= 1

    # Game over
    if attempts == 0:
        print("\nGame over!")
        print(f"The number is {secret_number}\n")

    # Play again?
    while True:
        again = input("Do you want to play again?(yes/no): ")

        if again.lower() == "yes" or again.lower() == "y":
            break
        elif again.lower() == "no" or again.lower() == "n":
            print("Thanks for playing")
            play = False
            break
        else:
            print("Pick yes or no")
