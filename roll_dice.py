import random #importing the random module to the program
roll = random.randint(1,6)#calling the function randint from the random module ,it will return a random number between 1 and 6
guess = int(input('guess the dice roll:\n'))#taking the users input and storing it in guess
if guess == roll:
    print("correct! they rolled a " + str(roll))
else:
    print("wrong! they rolled a " + str(roll)) 
