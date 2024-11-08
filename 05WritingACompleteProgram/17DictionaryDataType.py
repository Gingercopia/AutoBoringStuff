message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count ={} #key'r': value 12 if appears 12 times

#LOOPS THROUGH EACH CHAR IN MESSAGE (strings = list like value) 
#every iteration of loop, character is assigned single letter from message variable
#.upper uppercases all char in message

#character var is assigned single letter from message
#for the variable character - every iteration of the loop assigns character a new value in message (iteration 1 character = I, 2 =t, etc.)
for character in message.upper(): 
    
    #count={} dictionary is empty
    ##populate using setdefault with key(character): value (default of 0) pair. 
    ### checks index 0 of character and creates a key if it does not exist THEN assigns default value of zero    
    count.setdefault(character, 0)
    
    #ASSIGN INCREMENTED VALUE TO DICTIONARY UNDER SAME CHARCTER KEY i.e. count[character]
    #RETRIEVE CURRENT COUNT(i.e value) of character variable in dictionary add 1.
    #dictionary saving to i.e. count
    #
    count[character] = count[character]+1
print(count)

###RESULTS OF PROGRAM FROM TERMINAL
{'I': 7, 'T': 6, ' ': 13, 'W': 2, 'A': 5, 'S': 3, 'B': 1, 'R': 5, 'G': 2, 'H': 3, 'C': 3, 'O': 2, 'L': 3, 'D': 3, 'Y': 1, 'N': 4, 'P': 1, ',': 1, 'E': 5, 'K': 2, '.': 1}

