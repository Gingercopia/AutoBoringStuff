import random

# Initialize variables
# Generate the flip list in one line. 
# for _ in i.e. loop each iteration but don't store in var like i
###no calculations/operations = no need for iteration variable
flipList = [random.randint(0, 1) for _ in range(10001)]  

#USE VARIABLE ASSIGNMENT SHORTCUT
headsStreak, tailsStreak = 0, 0

# Function to count consecutive streaks of 6
def sixSameFlip():
    #GLOBAL to store values of var GLOBALLY
    global headsStreak, tailsStreak 
    
    #use flipList length - 5 (6consectutive cannot occur full range!)
    for i in range(len(flipList) - 5): 
        #i:i+6 i.e. 1st iteration[0:6], 2nd [1,7]...
        #== [0]* 6 i.e. [0,0,0,0,0,0]
        ##IF range = 6 occurences in a row add 1 to global var 
        if flipList[i:i + 6] == [0] * 6:   # Check for six consecutive heads (0)
            headsStreak += 1
        elif flipList[i:i + 6] == [1] * 6: # Check for six consecutive tails (1)
            tailsStreak += 1

sixSameFlip()

# Calculate and print percentages
headsPercent = round((headsStreak / len(flipList)) * 100, 1)
tailsPercent = round((tailsStreak / len(flipList)) * 100, 1)

print(f"{headsStreak} heads streaks, {tailsStreak} tails streaks")
print(f"{headsPercent}% of attempts resulted in 6 heads in a row")
print(f"{tailsPercent}% of attempts resulted in 6 tails in a row")
