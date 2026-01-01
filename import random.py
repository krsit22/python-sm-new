import random

number = random.randint(1, 20)
attempts = 5

print("🎯 Guess the number between 1 and 20")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 You Win!")
        break
    elif guess > number:
        print("📉 Too High!")
    else:
        print("📈 Too Low!")

    attempts -= 1
    print("Attempts left:", attempts)

if attempts == 0:
    print("❌ Game Over! Number was:", number)
