import game_data
import random
import art
print(art.logo)
def celeb1():
    global first
    print(first.get('name'), ",", end=" ")
    print(first.get('description'),",", end=" ")
    print(first.get('country'))
    return

def celeb2():
    global second
    while second == first:
        second = random.choice(game_data.data)
    print(second.get('name'), ",", end=" ")
    print(second.get('description'),",", end=" ")
    print(second.get('country'))


def comparison(follow1, follow2):
    follow = input("Who has more followers? A or B? ").lower()

    if follow == 'a':
        return follow1 > follow2
    elif follow == 'b':
        return follow2 > follow1
    else:
        return False

score = 0
first = random.choice(game_data.data)
while True:
    second = random.choice(game_data.data)

    print(f"\nCompare A: ", end="")
    celeb1()
    print(art.vs)
    print(f"Against B: ", end="")
    celeb2()
    follow1 = first.get('follower_count')
    follow2 = second.get('follower_count')

    if comparison(follow1, follow2):
        score += 1
        print(f"You're right! Current score: {score}")
        first = second  # Winner becomes the next comparison
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
