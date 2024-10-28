import random
play=True
pick=str(random.randint(10,20))
print("I will pick a number between 10 and 20.You should guess it")
while play:
    guess=str(input("Enter your guess here:"))
    if guess==pick:
        print("You are correct")
        break
    else:
        print("Your guess is not quite right")