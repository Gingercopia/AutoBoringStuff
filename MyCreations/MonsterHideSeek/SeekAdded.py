#GOALS: 
#   Allow Players to hide and receive bonuses to their hiding based on their skill
#   Have a Monster seek them in their hiding spot


######################    MODULES USED ##############################
import random

######################    PLAYER INFORMATION ################################

#PLAYER INPUT for name and skill
print('What is your name Traveler?')
playerName = input()
print('What is your skill level for Hiding')
pHideSkill = int(input())


######### DETERMINE MODIFIER TO ADD TO RANGE CAN HIDE IN ######################
def hideModCalculation():
    
    #corrected: uses RETURN so value is sent from LOCAL SCOPE to GLOBAL SCOPE
    if pHideSkill < 0:
        return 0 #sends 0 to pHideModifier var if <0 entered
    if pHideSkill > 0 and pHideSkill <= 5:
        return 1
    elif pHideSkill >= 6 and pHideSkill <= 10:
        return 2
    elif pHideSkill > 10 and pHideSkill < 16:
        return 3
    elif pHideSkill > 15 and pHideSkill < 20:
        return 4
    else:
        print('You have entered a number above 20, please try again')

#store result of hideModCalculation()
pHideModifier = hideModCalculation()
print('Your skill modifier is ' + str(pHideModifier))
#ROLL SKILL CHECK

input('Press Enter to roll your D20 skill check')
##stores your hide roll on D20
pHideRoll = int(random.randint(1,21))
print('The number rolled is ' + str(pHideRoll))


#CRITICAL ROLL
def criticalRoll():
    if pHideRoll == 20:
        return pHideRoll

#CRITICAL FAILURE
def criticalFail():
    if pHideRoll == 1:
        return pHideRoll

#WHERE PLAYER HIDING

#DETERMINE WHICH CODE TO RUN BASED ON ROLL

def hideSkillCheck():
    if criticalRoll():
        print("Amazing, you rolled a " +str(pHideRoll)+ " making you essentially invisible thanks to your perfect roll")
        
    elif criticalFail():
        print("you rolled a " +str(pHideRoll)+ " The monster is certain to find you!")
        
    else:
        #pHideModifier = hideModCalculation()
        #totalHide = pHideRoll + pHideModifier
        print(playerName + ' is able to add ' + str(pHideModifier) + ' to their hide roll.')
        

hideSkillCheck()
#print(hideSkillCheck)



#ADDS PLAYER MOD to RANDOM HIDING SPOT NUMBER
#SETS AREA MONSTER NEEDS TO SEEK - making easier or harder to find you
def modifiedHide():
    if criticalRoll == True:
        pHidingRange = (1,31)
        pHidingSpot = int(random.randint (*pHidingRange)) #*makes it a tupple i.e list to pull
        print('range of 1-30')
    elif criticalFail == True:
        pHidingRange = (1,11)
        pHidingSpot = int(random.randint(*pHidingRange))
        print('range of 1-10')
    else:
        pHidingRange = (1,21+pHideModifier)
        pHidingSpot = int(random.randint(*pHidingRange))
        print('range of 1-20 ' + ' + mod')
    return pHidingSpot, pHidingRange

pHidingSpot, pHidingRange = modifiedHide() #unpacks tupple and stores in appropriate variables

input('press enter to see the spaces you can hide in')
print("Hiding Range: ", pHidingRange)

input('press enter to see where hiding')
print("Hiding Spot: ", pHidingSpot)



"""
#BEFORE USE OF TUPPLE
    def modifiedHidingRange():
    if criticalRoll == True:
        pHidingRange = (1,31)
        pHidingSpot = int(random.randint (1, 31))
        print('range of 1-30')
    elif criticalFail == True:
        pHidingRange = (1,11)
        pHidingSpot = int(random.randint(1,11))
        print('range of 1-10')
    else:
        pHidingRange = (1,21+pHideModifier)
        pHidingSpot = int(random.randint(1,21+pHideModifier))
        print('range of 1-20 ' + ' + mod')
    return pHidingRange
"""

"""
#saves your hiding spot number to variable after function run
pHidingSpot = modifiedHidingSpotRange()
pHidingRange = modifiedHidingSpotRange() 
#prints your random hiding spot within the provided range
print(pHidingSpot, pHidingRange)
#print(pHidingRange)
"""

#input('Press Enter to Hide')
print("you are now hidden")


######################    MONSTER INFORMATION ################################
input('Press Enter to see which monster is hunting you')
monsterName = 'Slimer'
print(monsterName +' has sensed your presence and is ready to find you. If you are able to stay hidden from them for 6 turns you win')

input('press enter to start the hunt')

seekRange = pHidingRange


#Checks to see if the monster has found the player
def playerFound():
    #for loops through 5 attempts i.e. range, starting at 0-4
    for seek in range(5): 
        
        #stores what the monster roles each iteration i.e. attempt
        #*seekRange is a tupple - i.e. it sets the range based on the pHidingRange
        seekRoll = int(random.randint(*seekRange))
        
        #f string inserts var directly in str. 
        #seek + 1 adds 1 to the number i.e. iteration stored in seek - needed since starts at seek = 0
        print(f'{monsterName} is seeking....This is attempt number {seek + 1})')
        
        #1st if - did the monster roll the pHidingSpot
        if seekRoll == pHidingSpot:
            print ('You\'ve been slimed. It took ' +str(seek+1) + ' to find you')
            print ('You are mine now!!!')
            break #EXITS THE LOOP IF monster roll = player hiding spot
        else:
            remainingAttempts = 5 - seek #Total Attempts can do - iteration on i.e. seek =1 results in 4 remaining
            print ('Come Out Come Out Wherever You Are!!!! ' + 'I have ' + str(remainingAttempts)+ ' more chances to find you')
            print(seekRoll)
            input("Press Enter to start the next turn")
            if remainingAttempts == 0:
                print(monsterName + " You Idiot! You couln't find me...naner naner naner")
                break #EXITS THE LOOP IF no more attempts remaining
        
            
playerFound() #need to call function for it to run
 








   