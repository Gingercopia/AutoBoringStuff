
"""
print ('My name is')
#for auto sets i starting at 0
for i in range(5): #var i is set to 0, range is how many iterations to run
    print('Jimmy Five Times ' + str(i))
"""


"""
total = 0 #initial var value to iterate upon

#num var is defined by for
#first num value in range is 0
#different starting value then do range(start, end)
# Range of 101 loops from 0 to 100 NOT 101
# E.g. Range(3) results in return of 0,1,2
for num in range(5,101): #starts at 5 ends 100 
    #adds the current value of num to the existing value of total.
    #total is updated with the new sum
    total = total + num 
    
print(total)
"""
"""
###FOR loops are Simpler than WHILE loops
print('My name is')
i = 0
while i<5: #WHILE loop so need to set i and increment + 1. FOR loop doesn't need this
    for i in range(5):
        print('Jimmy Five Times ' + str(i))
        i = i + 1
"""
print ('My name is')
for i in range(10,0,-1): #starts at 10 ends at 0, counts down by increments of -1
    print('Jimmy Five Times ' + str(i))