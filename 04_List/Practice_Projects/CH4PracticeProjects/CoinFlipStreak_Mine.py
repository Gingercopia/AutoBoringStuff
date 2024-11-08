

#Experiment - How many streak of 6 heads or 6 tails in 10,000 attempts - what % did each occur
import random

flipList =[]
heads = 0
false = 1
headsStreak = 0
tailsStreak = 0

#creates randomly generated 0 or 1 10k times
for experimentNum in range(10001):
    coinFlips = random.randint(0,1)
    flipList.append(coinFlips)

"""for i in range(len(flipList)):
    print(str(i) + ' holds value ' + str(flipList[i]))
    """

def sixSameFlip():
    #GLOBAL updates these local var to the Global var
    global headsStreak, tailsStreak
    #loop through range specified by the length 
    ##of the generated list (stored in flipList)
    ##subtract 5 from the length since 
    ##cannot have 6 in a row if past end
    for i in range(len(flipList) - 5): 
        #i(starting iteration (0):i (ending iteration 0+6 =6)
        ##i:i is same as 0:0
        ##1st iteration = [i:i+6] i.e. [0:(0+6)6]
        ##2nd iteration = [i:i+6] i.e. [1:(1+6)7]
        ##Set range equal to [0]*6 i.e [0,0,0,0,0,0]
        ##SO, if range i:i equals 6 zeros then TRUE and add 1 to headsStreak count
        if flipList[i:i+6]==[0]*6:
            headsStreak +=1
            #return headsStreak  ----CANNOT USE SINCE STOPS LOOP  
        else:
            if flipList[i:i +6] == [1]*6:
                tailsStreak +=1
                #return tailsStreak ----CANNOT USE SINCE STOPS LOOP

sixSameFlip()

print(headsStreak, tailsStreak)

headsPercent = round(((headsStreak/len(flipList)) * 100), 1)
print(str(headsPercent)+'% of attempts resulted Tails occuring 6 times in a row')
#tailsPercent = tailsStreak/
tailsPercent = round(((tailsStreak/(int(len(flipList)))) * 100), 1)
print(str(tailsPercent)+'% of attempts resulted Tails occuring 6 times in a row')


#create a check to see how many have 6 of same per iteration.

#headCheck = [0]*6
#tailCheck = [1]*6

#Check if 6 in a row in coinFlips within 
    
    ### Check if random number occurs in sequence of 6

    ### Count Sequences and Update Streak count

    #if 6@ 0 then update headStreak
    #if 6@ 1 then update tailStreak

    #create list to store random numbers


"""
    if experimentNum ==0:
        heads = True
        experimentNum+=1

    else:
        if experimentNum ==1
        tails = True
        experimentNum+1
""" 

