water = 300
milk = 200
coffee =100
money = 0
Sum = 0
def report():
    print("Water: ", water)
    print("Milk: ", milk)

    print("Coffee: ", coffee)
    print("Money: ", money)
    return

def moneyy():
    print("Please insert coins.")
    quarters = int(input("Quarters: ")) *0.25
    dimes = int(input("Dimes: ")) * 0.10
    nickles = int(input("Nickles: ")) * 0.05
    penny = int(input("Pennies: ")) * 0.01
    global Sum
    Sum  = quarters + dimes + nickles + penny
    return

def count_money():
    print(Sum)
    if drink ==  "espresso":
        if Sum > 1.5:
            print("Here is your change", Sum - 1.5)
            print("Thank you, here is your Espresso.☕️")
            return True
        elif Sum == 1.5:
            print("Thank you, here is your Espresso.☕️")
            return True
        else:
            print("Short on money, sorry")
    if drink == "latte":
        if Sum > 2.5:
            print("Here is your change", Sum - 2.5)
            print("Thank you, here is your Latte.☕️")
            return True

        elif Sum == 2.5:
            print("Thank you, here is your Latte.☕️")
            return True

        else:
            print("Short on money, sorry")

    if drink == "cappuccino":
        if Sum > 3:
            print("Here is your change", Sum - 3)
            print("Thank you, here is your Cappuccino.☕️")
            return True

        elif Sum == 3:
            print("Thank you, here is your Cappuccino.☕️")
            return True

        else:
            print("Short on money, sorry")

def espresso():
    global water
    global coffee
    global money
    if water >= 50 and coffee >= 18:
        water -= 50
        coffee -= 18
        money += 1.5
        return True
    else:
        return False

def cappuccino():
    global water
    global milk
    global coffee
    global money
    if water >= 250 and coffee >= 24 and milk >= 100:
        water -= 250
        coffee -= 24
        milk -= 100
        money += 3
        return True
    else:
        return False


def latte():
    global water
    global milk
    global coffee
    global money
    if water >= 200 and coffee >= 24 and milk >= 150:
        water -= 200
        coffee -= 24
        milk -= 150
        money += 2.5
        return True
    else:
        return False

def run():
    global drink
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink == "espresso":
        if not espresso():
            print("Sorry, not enough resources!")
            return False
        moneyy()
        count_money()
    elif drink == "latte":
        if not latte():
            print("Sorry, not enough resources!")
            return False
        moneyy()
        count_money()
    elif drink == "cappuccino":
        if not cappuccino():
            print("Sorry, not enough resources!")
            return False
        moneyy()
        count_money()
    elif drink == "report":
        report()
    return True

while True:
    if not run():
        break
