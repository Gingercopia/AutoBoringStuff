#this is a guess the number game.
import random #brings in random module
print ('Hello, What is your name?')

#stores your input in name var
name = input()

#ARGUMENTS 1,10 used to generate value and store in var
secretNumber = random.randint(1,10) 
print('Well, ' + name + ', I am thinking of a number b/w 1 and 10')

#for loops to check how many quessesTaken
#If more guesses than range (i.e. 6) skip to global else
for guessesTaken in range (1,7):
    print('Take a guess')
    #converts user input to int type
    guess = int(input()) #Local var holding user input as integer
    
    if guess < secretNumber:
        print('Your guess is too low.')
    
    elif guess > secretNumber: 
        print('Your guess is too high')
    
    else:
        break #condition is correct guess

##CORRECT GUESS so break out of for loop above
#str(guess) returns the last stored value of guess stored in GuessesTaken variable
if guess == secretNumber:
    print('Good Job, ' + name + '! You guessed my number in ' + str(guess)) 
##guessesTaken PAST RANGE so print else
else: 
    print('You are over the limit of 6 guesses')