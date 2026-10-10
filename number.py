import random

number = random.randint(1, 100)
attempts = 0

print("🎮 Welcome to Guess the Number Game!")
print("I have selected a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try a bigger number.")
    elif guess > number:
        print("Too high! Try a smaller number.")
    else:
        print("🎉 Congratulations! You guessed the number!")
        print("The number was:", number)
        print("Total attempts:", attempts)
        break