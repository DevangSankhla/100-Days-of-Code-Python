rock = '''rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock,paper,scissors]
import random
computerpick = random.choice(list)
option = input("What do you choose? Rock, Paper or Scissors? ")
if option == 'rock' or option == 'Rock':
    print('You chose ' + rock)
    print('Computer chose ' + computerpick)
    if computerpick == rock:
        print("Draw")
    elif computerpick == scissors:
        print("You Winn :)))")
    else:
        print("You Lose :(((")
elif option == 'paper' or option == 'Paper':
    print('You chose ' + paper)
    print('Computer chose ' + computerpick)
    if computerpick == rock:
        print("You Win :)))")
    elif computerpick == scissors:
        print("You Lose :(((")
    else:
        print("Draw")
else:
    print('You chose' + scissors)
    print('Computer chose ' + computerpick)
    if computerpick == rock:
        print("You Lose :(((")
    elif computerpick == scissors:
        print("Draw")
    else:
        print("You Win :)))")
