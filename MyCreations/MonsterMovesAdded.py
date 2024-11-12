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

########## MONSTER TYPE and SPEED
monsterStat = ''
def monsterInfo():
    global monsterStat
    monsterType = ['Demon', 'Undead', 'Elemental', 'Djinn', 'Fey', 'Beast', 'Dragon', 'Giant']
    monsterSpeed = [2.0,0.5,3.0, 2.0, 6.0]
    ###Create Dictionary to store key:value pair
    monsterStat = {}
    ###Create key value pairs from 2 lists
    for i in range(len(monsterType)):
        if i < len(monsterSpeed):
            monsterStat[monsterType[i]] = monsterSpeed[i]
        else:
            monsterStat[monsterType[i]] = 1.0
    return monsterStat
monsterInfo()
print(monsterStat)
"""
monsterTiny =[]
monsterSmall=[]
monsterMedium=[]
monsterLarge=[]
monsterHuge=[]
monsterGargantuan=[]

demonPowers = []
undeadPowers = []
elementalPowers = []
djinnPowers = []
feyPowers = []
bestPowers = []
"""

########## WHAT MONSTER IS SEEKING YOU
input('Press Enter to see which monster is hunting you')
# var = tuple (i.e. key value pair) created since using .items
randomMonster = random.choice(list(monsterStat.items()))

#var key, var value = var name with tuple (key val pair)
monsterType, monsterSpeed = randomMonster

#monsterName = 'Slimer'
print('A '+ str(monsterType) +' has sensed your presence and is ready to find you. If you are able to stay hidden from them for 6 turns you win' + '. A '+str(monsterType) + ' can check '+ str(monsterSpeed)+ ' spaces each turn!')

input('press enter to start the hunt')

######### SET THE AREA & HOW MANY ATTEMPTS TO SEEK YOU OUT 
seekRange = pHidingRange #found in player section above

maxAttempts = 6  #use maxAttempt variable to set range so nested if will run

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
        
        print(f'{monsterType} is seeking....This is attempt number {seek + 1})')
        
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
                print(monsterType + " You Idiot! You couln't find me...naner naner naner")
                break #EXITS THE LOOP IF no more attempts remaining
        
            
playerFound() #need to call function for it to run
 

###GPT Solution to Speed and movement in turns
import random

# Global variable
monsterStat = ''

def monsterInfo():
    global monsterStat
    monsterType = ['Demon', 'Undead', 'Elemental', 'Djinn', 'Fey', 'Beast', 'Dragon', 'Giant']
    monsterSpeed = [2.0, 0.5, 3.0, 2.0, 6.0]
    # Create dictionary to store key:value pairs
    monsterStat = {}
    for i in range(len(monsterType)):
        if i < len(monsterSpeed):
            monsterStat[monsterType[i]] = monsterSpeed[i]
        else:
            monsterStat[monsterType[i]] = 1.0
    return monsterStat

# Call the function to populate the global variable
monsterInfo()

# Select a random monster from the dictionary
randomMonster = random.choice(list(monsterStat.items()))
randomType, randomSpeed = randomMonster  # Unpack the tuple into type and speed

# Function to simulate the monster's search
def monsterSearch(turns, speed):
    checked_spaces = set()
    for turn in range(1, turns + 1):  # Loop for each turn
        print(f"Turn {turn}:")
        for move in range(int(speed)):  # Loop for each move within the turn
            while True:
                space = random.randint(1, 10)  # Assuming spaces are numbered 1 to 10
                if space not in checked_spaces:
                    checked_spaces.add(space)
                    print(f"Monster checks space {space}.")
                    break  # Exit the loop when a new space is found
        if len(checked_spaces) >= 10:
            print("All spaces have been checked.")
            break  # Exit if all spaces have been checked
    if player_found(checked_spaces):
        print("The monster has found you!")
    else:
        print("You managed to stay hidden!")

# Dummy function to simulate player being found
def player_found(checked_spaces):
    player_location = random.choice(list(checked_spaces))
    return True  # For simplicity, assume the player is found if the space is checked

# Simulate the monster's 6-turn search with its specific speed
print(f"{randomType} with speed {randomSpeed} is searching for you.")
monsterSearch(6, randomSpeed)  # Pass the randomSpeed to the function







   