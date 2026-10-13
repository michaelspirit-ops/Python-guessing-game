from random import randint

print()
print("Welcome to the Number Guessing Game")

play = True

while play:
    # Choose a difficulty
    while True:
        print()
        print("Choose Difficulty:")
        print("1. Easy", "  2. Medium", "  3. Hard")
        print()

        try:
            pick = int(input("Pick 1, 2 or 3: "))
        except ValueError:
            print()
            print("Pick a number")
        else:
            parameters = [
                {"attempts": 7, "maximum": 20, "used_value": 8},
                {"attempts": 6, "maximum": 50, "used_value": 9},
                {"attempts": 5, "maximum": 100, "used_value": 10},
            ]

            if 1 <= pick <= 3:
                attempts = parameters[pick - 1]["attempts"]
                maximum = parameters[pick - 1]["maximum"]
                used_value = parameters[pick - 1]["used_value"]
                break
            else:
                print("Input is invalid")

    print()
    print(f"You have {attempts} attempts to guess the number between 1 and {maximum}")

    # Guess a number
    secret_number = randint(1, maximum)

    while attempts > 0:
        try:
            print()
            number = int(input("Guess a number: "))
        except ValueError:
            print("You have to input a number")
        else:
            closeness = abs(secret_number - number)

            if number == secret_number:
                print("That's correct!")
                print(f"You used {used_value - attempts} attempts to guess the number")
                break
            elif closeness <= 5:
                print("You are very close!")
            elif closeness <= 10:
                print("Getting close!")
            elif closeness <= 20:
                print("Number not too far!")
            elif closeness >= 21:
                print("You are too far!")

            attempts -= 1

    # Game over
    if attempts == 0:
        print()
        print("Game over!")
        print(f"The number is {secret_number}")

    # Play again?
    while True:
        print()

        again = input("Do you want to play again?(yes/no): ")

        if again.lower() == "yes" or again.lower() == "y":
            break
        elif again.lower() == "no" or again.lower() == "n":
            print("Thanks for playing")
            play = False
            break
        else:
            print("Pick yes or no")
