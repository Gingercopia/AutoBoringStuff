"""
spam = 0 #sets value for spam var
while spam <5: #condition var <5 loop occurs
    print('Hello world!')
    spam = spam + 1 #<5 then this keeps running
    #RESULT is this while loop ITERATING 5x
# """

"""###INPUT VALIDATION
name = ''
while name !='your name': 
#1st name is set to blank so True and prints below
#2nd after type name - prints out again since rechecks condition since it doesn't = the string 'your name'
#enter string your name to get print('Thank you!) to run
    print('Please type your name.')
    name = input() #gives name a value so prints below
print('Thank you!')"""

"""
###INFINITE LOOP and BREAK
name = ''
while True: 
    print('Please type your name.')
    name = input() #gives name a value so prints below
    if name == 'your name': #runs until your name is True
        break #causes execution to break out of program to print Thank you
print('Thank you!')
"""

###CONTINUE to return to loop
spam = 0
while spam <5:
    spam = spam + 1
    if spam == 3:
        continue #doesn't print spam is 3 since condition is true and continue executes jumping back to the start of the while loop so print fx doesn't happend when spam ==3
    print('spam is ' + str(spam))

