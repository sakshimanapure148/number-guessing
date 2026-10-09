import random
class Game:
    def __init__(self):
        self.number = random.randint(1,100)
        self.attempts = 0

        def play(self):
            print("Number Gussing Game")
            print("Guess a number between 1 and 100!")


            while True:
                



guess = int(input("Guess a number between 1 and 100: "))

if guess == number:
    print("🎉 Correct! You won!")
else:
    print("❌ Wrong! The number was", number)