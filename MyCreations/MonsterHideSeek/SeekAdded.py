#GOALS: 
#   Allow Players to hide and receive bonuses to their hiding based on their skill
#   Have a Monster seek them in their hiding spot


######################    MODULES USED ##############################
import random

######################    PLAYER INFORMATION ################################

#PLAYER INPUT for name and skill level
print('What is your name Traveler?')
playerName = input()
print('What is your skill level for Hiding')
pHideSkill = int(input())


######### DETERMINE MODIFIER FOR HIDING RANGE ######################
def hideModCalculation():
    
    if pHideSkill < 0:
        return 0 #RETURN SAVES VALUE FROM LOCAL TO GLOBAL SCOPE
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

pHideModifier = hideModCalculation() #RETURN VALUE PASSES AS ARGUMENT AND IS STORED
print('Your skill modifier is ' + str(pHideModifier))




###########################  DICE ROLLING ##################################

input('Press Enter to roll your D20 skill check') #HIT ENTER TO ENACT BELOW 
pHideRoll = 1#int(random.randint(1,21)) #CHANGE NUMBER HERE TO TEST 1,20,RANDOM...
print('The number rolled is ' + str(pHideRoll))



def criticalRoll(): # WAS IT A NATURAL 20
    if pHideRoll == 20: 
        return pHideRoll
    
naturalTwenty = criticalRoll() # TRUE = STORES TRUE


def criticalFail():# WAS IT A NATURAL 1
    if pHideRoll == 1:  
        return pHideRoll

naturalOne = criticalFail() # TRUE = STORES TRUE

def hideSkillCheck(): #PROVIDE INSIGHT TO SPACES CAN HIDE IN
    if criticalRoll():
        print("Amazing, you rolled a " +str(pHideRoll)+ ", you gain 10 spaces to hide in")
        
    elif criticalFail():
        print("you rolled a " +str(pHideRoll)+ ", you lose 10 spaces to hide in!")
        
    else:
        print(playerName + ' will have ' + str(pHideModifier) + ' extra spaces to hide in.')
        
hideSkillCheck()#RUNS FX and STORES RESULT TO TERMINAL


def playerSpacesAndLocation(): #CREATES RANGE (HIDING SPACES) AND SPOT(LOCATION) OF YOU BASED ON RANDOM ROLL IN RANGE
                                # MONSTER PULLS THEIR GUESSING RANGE FROM THIS FUNCTION
    if naturalTwenty:
        pHidingRange = (1,31)
        #USE A TUPPLE (*) TO PULL RANGE FROM 
        pHidingSpot = int(random.randint (*pHidingRange)) 
        print('range of 1-30')
    elif naturalOne:
        pHidingRange = (1,11)
        pHidingSpot = int(random.randint(*pHidingRange))
        print('range of 1-10')
    else:
        pHidingRange = (1,21+pHideModifier)
        pHidingSpot = int(random.randint(*pHidingRange))
        print('range of 1-20 ' + ' + mod')
    return pHidingSpot, pHidingRange # STORES VALUES OF EACH TO BE CALLED IN GLOBAL SCOPE

pHidingSpot, pHidingRange = playerSpacesAndLocation() #UNPACKS TUPPLE AND ASSIGNS VALUES TO THEIR GLOBAL VAR

input('press enter to see the spaces you can hide in')
print("Hiding Range: ", pHidingRange)#PRINTS VALUE OF pHidingRange (CONCAT NOT NEEDED)

input('press enter to see where hiding')
print("Hiding Spot: ", pHidingSpot) #PRINTS VALUE OF pHidingRange (CONCAT NOT NEEDED)

print("you are now hidden")


######################    MONSTER INFORMATION ################################

########## MONSTER SEEKING YOU
input('Press Enter to see which monster is hunting you')
monsterName = 'Slimer'
print(monsterName +' has sensed your presence and is ready to find you. If you are able to stay hidden from them for 6 turns you win')

input('press enter to start the hunt')

######### SET THE AREA & HOW MANY ATTEMPTS TO SEEK YOU OUT 
seekRange = pHidingRange #found in player section above

maxAttempts = 6   #use maxAttempt variable to set range so nested if will run

rolledValues = set() #CREATES A SET TO STORE rolledValues so not reused

######### DETERMINE IF SEEKER FOUND HIDER
def playerFound(): 
    for seek in range(maxAttempts): #LOOP THROUGH CODE x6
        seekRoll = int(random.randint(*seekRange)) # RANDOM ROLL OCCURS - based on seekRange stored range from pHidingRange
        
        #f string inserts var directly in str. 
        #seek + 1 adds 1 to the number i.e. iteration stored in seek - needed since starts at seek = 0
        
        while seekRoll in rolledValues: #LOOP UNTIL seekRoll VALUE HAS NOT BEEN USED i.e. STORED IN rolledValues SET
            seekRoll = random.randint(*seekRange)
        
        rolledValues.add(seekRoll) # ADDS top seekRoll VALUE - if it exists in set then it goes to WHILE STATEMENT to find unique value
        
        print(f'{monsterName} is seeking....This is attempt number {seek + 1})')
        
        if seekRoll == pHidingSpot: # FOUND YOU
            print(pHidingSpot)#BUG TEST: confirms pHiding matches seekRoll
            print ('You\'ve been slimed. It took ' +str(seek+1) + ' attempts to find you')
            print ('You are mine now!!!')
            break #EXITS THE LOOP IF monster roll = player hiding spot
        
        else: # TRYING TO FIND YOU
            remainingAttempts = maxAttempts - (seek+1) #Total Attempts can do - i.e. 5 - seek iteration +1 since start at 0
            print ('Come Out Come Out Wherever You Are!!!! ' + 'I have ' + str(remainingAttempts)+ ' more chances to find you')
            print(seekRoll)
            input("Press Enter to start the next turn")
            
            if remainingAttempts == 0: #ANNOUNCES WINNER
                print(monsterName + " You Idiot! You couln't find me...naner naner naner")
                break #EXITS THE LOOP IF no more attempts remaining
        
            
playerFound() #need to call function for it to run
 








   