import random 
randNumber = random.randint(1, 5)
# print(randNumber)

userGuess = None
guesses = 0
while(userGuess != randNumber):
    userGuess = int(input("Guess a number between 1 and 5: "))
    guesses += 1
    if(userGuess == randNumber):
        print("You guessed correctly!")
    else:
        if(userGuess > randNumber):
            print("Your guess is too high!")
        elif(userGuess < randNumber):
            print("Your guess is too low!")    
        # print("You guessed Wrong!")

print(f"It took you {guesses} guesses to guess the number")

with open('hiScore.txt', 'r') as f:
    hiScore = int(f.read())
    
if(guesses < hiScore):
    with open('hiScore.txt', 'w') as f:
        f.write(str(guesses))
    print("You beat the high score!")   
     
# with open('hiScore.txt', 'w') as f:
#     f.write(f"It took you {guesses} guesses to guess the number")
#     f.close()