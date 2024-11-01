#GOAL: DETERMINE HOW WELL A PLAYER IS HIDDEN

import random
pHideRoll = int(1)#random.randint(1,20))


#PLAYER INPUT for name and skill
print('What is your name Traveler?')
playerName = input()

print('What is your hide skill level?')
pHideSkill = int(input())



#DETERMINE hide skill modifier value if not Critical Roll
def hideModCalculation():
    #corrected: uses RETURN so value is sent from LOCAL SCOPE to GLOBAL SCOPE
    if pHideSkill < 0:
        return 0 #sends 0 to pHideModifier var if <0 entered
    elif pHideSkill > 0 and pHideSkill <= 5:
        return 1
    elif pHideSkill >= 6 and pHideSkill <= 10:
        return 2
    elif pHideSkill > 10 and pHideSkill < 16:
        return 3
    elif pHideSkill > 15 and pHideSkill < 20:
        return 4
    else:
        print('You have entered a number above 20, please try again')

#CRITICAL ROLL
def criticalRoll():
    if pHideRoll == 20:
        return pHideRoll

#CRITICAL FAILURE
def criticalFail():
    if pHideRoll == 1:
        return pHideRoll

#DETERMINE WHICH CODE TO RUN BASED ON ROLL
def hideOutcome():
    if criticalRoll():
        print("Amazing, you rolled a " +str(pHideRoll)+ " making you essentially invisible thanks to your perfect roll")
    elif criticalFail():
        print("you rolled a " +str(pHideRoll)+ " The monster is certain to find you!")
    else:
        pHideModifier = hideModCalculation()
        totalHide = pHideRoll + pHideModifier
        print(playerName + ' has a hide skill level of ' + str(pHideSkill) + '. ' +
              playerName + ' has rolled a ' + str(pHideRoll) + ' and is able to add ' +
              str(pHideModifier) + ' to their hide roll. This results in a total hide check of ' + str(totalHide))

hideOutcome()





   