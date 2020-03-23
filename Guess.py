import random
user = input('To end game enter "-10". Press Enter key to begin.')
while user != "Exit":
    rand = random.randint(0, 20)
    user = int(input("Guess a number between 0 and 20."))
    cnt = 0
    streak = 0
    if user == rand:
        print("Correct!")
        cnt += 1
        streak += 1
        if streak == 4:
            print("You're amazing!")
    elif user == -10:
        break
    else:
        print("Incorrect! " + str(rand) + " was the correct answer.")
        streak = 0
print("Finish!")
print("You guessed correctly " + str(cnt) + " times!")
    