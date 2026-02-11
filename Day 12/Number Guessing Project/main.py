import random
import art
print(art.logo)

def make_list(num_list):
    for i in range(1, 101):
        num_list.append(i)

def random_number(num_list):
    random_num = random.choice(num_list)
    return random_num

def look_number(ch_number, my_number):
    if my_number == ch_number:
        return "YOU FOUND IT"
    elif my_number > ch_number:
        return "Too High"
    else:
        return "Too Low"
while True:
    number_list = []
    make_list(number_list)

    print("I'm thinking of a number between 1 and 100!")
    choose_dif = input("Choose a difficulty level: 'easy' or 'hard': ").lower()

    comp_chosen_number = random_number(number_list)

    if choose_dif == "hard":
        attempts = 5
    elif choose_dif == "easy":
        attempts = 10
    else:
        print("Invalid input. Switching default easy mode")
        attempts = 10

    for i in range(1, attempts + 1):
        print(f"Attempt {i}/{attempts}")
        my_chosen_number = int(input("Guess a number: "))
        result = look_number(comp_chosen_number, my_chosen_number)

        if result == "YOU FOUND IT":
            print(f"Congratulations! You found it in {i} attempts!")
            break
        else:
            print(result)
    else:
        print(f"Game Over! The number was {comp_chosen_number}.")
    again = input("Do you want to play again? (y/n): ").lower()
    print("\n" *20)
    if again != "y":
        print("Thanks for playing!")
        break



