import random

high_score = 0


def dice_game(high_score):
    print(f"Current High Score: {high_score}")
    print("1) Roll Dice")
    print("2) Leave Game")
    choice = input("Enter your choice:")
    for i in range(0, 2, 1):
        if choice == "1":
            first_dice = random.randint(1, 6)
            second_dice = random.randint(1, 6)
            last_total_score = first_dice + second_dice
            print(f"You rolled a {first_dice}")
            print(f"You rolled a {second_dice}\n")
            print(f"You have rolled a total of: {last_total_score}\n")
            if last_total_score > high_score:
                print(f"New high score!\n")
                return dice_game(last_total_score)
            return dice_game(high_score)

        elif choice == "2":
            print("Goodbye!")
            break


dice_game(high_score)
