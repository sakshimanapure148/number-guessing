import random

number = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100: "))

if guess == number:
    print("🎉 Correct! You won!")
else:
    print("❌ Wrong! The number was", number)