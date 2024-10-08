import os

import art

# HINT: You can call clear() to clear the output in the console.

print(art.logo)
another_bidder = True
bids = {}

while another_bidder:
    name = input("What is your name? ")
    amount = int(input("What's your bid? $"))
    bids[name] = amount
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    print("\n" * 100)
    if more_bidders == "no":
        another_bidder = False

max_bid = 0
for bidder in bids:
    if bids[bidder] > max_bid:
        max_bid = bids[bidder]
        winner = bidder

print(f"The winner is {winner}.")
