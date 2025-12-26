import art
print(art.logo)
names = {}

while True:
    name = input("What is your name? ")
    bid = int(input("What's your bid?: $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    names[name] = bid
    print("\n" * 25)

    if other_bidders == "yes":
        print("\n"*25)
    elif other_bidders == "no":
        for bid in names:
            highest_bid = 0
            if names[bid]>= highest_bid:
                highest_bid = names[bid]
                winner_name =bid

        print(f"The winner is {winner_name}")
        print(f"With the bid {highest_bid}. Congratulations!")
        print(art.logo)
        break
