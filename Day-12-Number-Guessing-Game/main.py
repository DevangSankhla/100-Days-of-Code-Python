import random
import art


def get_difficulty():
    while True:
        choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if choice == 'easy':
            return 10
        elif choice == 'hard':
            return 5
        else:
            print("Invalid choice. Please type 'easy' or 'hard'.")


def check_guess(guess, answer):
    if guess > answer:
        return "Too high."
    elif guess < answer:
        return "Too low."
    else:
        return "correct"


def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
  #  print(f"Pssst, the correct answer is {answer}")

    attempts = get_difficulty()

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")

        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        result = check_guess(guess, answer)

        if result == "correct":
            print(f"You got it! The answer was {answer}")
            break
        else:
            print(result)
            attempts -= 1

            if attempts == 0:
                print(f"\nYou've run out of guesses. The answer was {answer}. You lose.")
            else:
                print("Guess again.")


if __name__ == "__main__":
    play_game()
