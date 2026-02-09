import art
print(art.logo)
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def give_cards(hand, amount):
    hand.extend(random.choices(cards,  k = amount))
    current_sum = sum(hand)
    if current_sum > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        current_sum = sum(hand)
    return current_sum

my_cards = []
deck_cards = []

sum_my_cards = give_cards(my_cards , 2)
sum_deck_cards = give_cards(deck_cards, 2)

game_over = False
while not game_over:
    print(f"Your cards: {my_cards} your sum: {sum_my_cards}")
    print(f"Deck's first card: {deck_cards[0]}")

    if sum_my_cards > 21 or sum_deck_cards > 21:
         game_over = True
    else:
        continue_hit = input("Do you want to play again? (y/n): ").lower()
        if continue_hit == "y":
            sum_my_cards = give_cards(my_cards, 1)
        else:
            if sum_my_cards <= 21:
                while sum_deck_cards < 17:
                    sum_deck_cards = give_cards(deck_cards, 1)
            game_over = True
print(f"Your Final sum: {sum_my_cards} Deck's Final sum: {sum_deck_cards}")

if sum_my_cards > 21:
    print("YOU LOSE!")
elif sum_deck_cards > 21:
    print("YOU WIN!")
elif sum_my_cards > sum_deck_cards:
    print("YOU WIN!")
elif sum_deck_cards == sum_my_cards:
    print("ITS A DRAW!")
else:
    print("YOU LOSE!")




