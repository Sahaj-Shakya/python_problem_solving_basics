import random

num = random.randint(1, 100)
count = 0
line = "---------------------------"

while True:
    guess = int(input("Guess the number between 1-100: "))

    if guess == num:
        print(f"{line}\nCongratulations you have guessed the correct number.\nCorrect number = {num}\nTotal guesses = {count}")
        break
    elif guess > num:
        print("Your guess is higher than the actual number. Try again.") 
        count += 1
    elif guess < num:
        print("Your guess is lower than the actual number. Try again")
        count += 1
        
