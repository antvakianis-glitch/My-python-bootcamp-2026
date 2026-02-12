import random
import game_data
import art

print(art.logo)

def find_person(data_list):
    random_index = random.randint(0, len(data_list) - 1)
    person = data_list[random_index]

    return [
        person['name'],
        person['description'],
        person['country'],
        person['follower_count']
    ]

sample_b = find_person(game_data.data)
score = 0
game_over = False

while not game_over:
    sample_a = sample_b
    sample_b = find_person(game_data.data)

    print(f"Compare A: {sample_a[0]} a {sample_a[1]} from {sample_a[2]}")
    print(art.vs)
    print(f"Against B: {sample_b[0]} a {sample_b[1]} from {sample_b[2]}")

    my_pick = input("What do you choose? 'A' or 'B': ")
    if my_pick == 'A':
        chosen = sample_a
        other = sample_b
    else:
        chosen = sample_b
        other = sample_a

    if chosen[3] > other[3]:
        score += 1
        print(f"Correct! Current score: {score}")
        print(art.logo)
        sample_b = chosen
        print("\n" * 1)
    else:
        print(f"Wrong! Game Over!")
        print(f"Final score: {score}")
        game_over = True
        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again == 'y':
            score = 0
            game_over = False
            print("\n" * 20)
            print(art.logo)
            sample_b = find_person(game_data.data)



