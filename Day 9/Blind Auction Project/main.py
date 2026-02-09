# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from time import process_time_ns

import art
print(art.logo)
bid_dictionary = {}

def bid_action(bid_record):
        highest_bid = 0
        winner = ""

        for bids in bid_record:
            bid_amount = bid_record[bids]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bids
        print(f"The winner is {winner} with a bid of ${highest_bid}")
continue_bidding = True
while continue_bidding:

    person = input("What is your name?:")
    price = int(input("What is your bid?:"))
    bid_dictionary[person] = price

    choise = input("Are there any other bidders. Type Yes or No").lower()
    if choise == "no":
        continue_bidding = False
        bid_action(bid_dictionary)
    elif choise == "Yes":
        print("\n" *50)