import random
#skillCheck = random.randint(1,20)
pHideRoll = int(random.randint(1,20))


##INPUT FOR PLAYER NAME and HIDE SKILL LEVEL
print('What is your name Traveler?')
playerName = input()

print('What is your hide skill level?')
pHideSkill = int(input())

##DETERMINES MODIFIER TO ROLL
def hideModCalculation():
    #FAILURE since pHideMod only stored LOCALLY
    if pHideSkill < 0:
        pHideMod = 0
        #print('You receive ' + str(pHideSkill) + ' bonus to hide')
    elif pHideSkill >0 and pHideSkill<=5:
        pHideMod = 1
        #print ('You receive ' + str(pHideSkill) + ' bonus to hide')
    elif pHideSkill >=6 and pHideSkill<=10:
        pHideMod = 2
        #print ('You receive ' + str(pHideSkill) + ' bonus to hide')
    elif pHideSkill >10 and pHideSkill<16:
        pHideMod = 3
        #print ('You receive ' + str(pHideSkill) + ' bonus to hide')
    elif pHideSkill >15 and pHideSkill<20:
        pHideMod = 4
        #print ('You receive ' + str(pHideSkill) + ' bonus to hide')

## IF 20 is rolled skip running hideModCalculation
def criticalRoll():
    if pHideRoll == 20:
        print("Amazing, you are essentially invisible thanks to your perfect roll")
    else:
        hideModCalculation()

##SAVE result of hideModCalculation function
pHideModifier = hideModCalculation() #result of fx stored in pHideModifier

#CALCULATE ROLL + MODIFIER
totalHide = pHideRoll + pHideModifier

#PRINT RESULTS OF ROLL
print(playerName + ' has a hide skill level of ' + str(pHideSkill) + '. '+ str(playerName) + ' has rolled a ' + str(pHideRoll) + ' and is able to add ' + str(pHideModifier) + ' to their hide roll. This results in a total hide check of ' + str(totalHide))
