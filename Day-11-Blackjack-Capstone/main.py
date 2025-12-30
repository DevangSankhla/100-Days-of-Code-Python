import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
yourcards = []
computercards = []

gamestart = input("Do you want to play a game of Blackjack? type 'y' for yes and 'n' for no:\n").lower()

if gamestart == "y":
    print(art.logo)
    yourcards.append(random.choice(cards))
    yourcards.append(random.choice(cards))
    computercards.append(random.choice(cards))
    print(f"Your cards are :\n{yourcards}")
    print(f"Computer's card is :\n{computercards}")

    morecard = input("Type 'y' to get another card, type n to pass:\n").lower()
    if morecard == "y":
        yourcards.append(random.choice(cards))
        computercards.append(random.choice(cards))
        print(f"Your final cards are :\n{yourcards}")
        print(f"Computer's final cards are :\n{computercards}")

        num1 = sum(yourcards)
        num2 = sum(computercards)

        def closestto21(num1, num2):

            if abs(21 - num1) < abs(21 - num2):
                return num1
            elif abs(21 - num1) == abs(21- num2):
                return num1, num2
            else:
                return num2

        if num1> 21:
            print(f"You Lose :(\nYour sum = {num1} (greater than 21)\nComputer's Sum = {num2}")
        elif closestto21(num1, num2) == num1:
            print(f"YOU WIN!!!\nYour sum = {num1}\nComputer's Sum = {num2}")
        elif closestto21(num1,num2) == num2:
            print(f"You Lose :(\nYour sum = {num1}\nComputer's Sum = {num2}")
        else:
            print(f"It's a Draw.\nYour sum = {num1}\nComputer's Sum = {num2}")
    else:
        computercards.append(random.choice(cards))
        print(f"Your final cards are :\n{yourcards}")
        print(f"Computer's final cards are :\n{computercards}")

        num1 = sum(yourcards)
        num2 = sum(computercards)

        def closestto21(num1, num2):

            if abs(21 - num1) < abs(21 - num2):
                return num1
            elif abs(21 - num1) == abs(21 - num2):
                return num1, num2
            else:
                return num2

        if closestto21(num1, num2) == num1:
            print(f"YOU WIN!!!\nYour sum = {num1}\nComputer's Sum = {num2}")
        elif closestto21(num1, num2) == num2:
            print(f"You Lose :(\nYour sum = {num1}\nComputer's Sum = {num2}")
        else:
            print(f"It's a Draw.\nYour sum = {num1}\nComputer's Sum = {num2}")
elif gamestart == "n":
    print("Thank you! Visit Again.")

else:
    print("Umm, what? pls restart.")
