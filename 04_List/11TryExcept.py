def div42by (divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError: #SPECIFY error type to receive exception or leave blank so any error returns the print below
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0)) #runs except which returns NONE value
print(div42by(1))

###INPUT VALIDATION
print('How many cats do you have?')
numCats = input()#currently input could be anything
try:
    if int(numCats) >=4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')
except ValueError: #outputs message for wrong data type being used
    print('You did not enter a valid number type')



##INPUT VALIDATION w/NESTED IF
while True:  # Start an infinite loop
    print('How many cats do you have?')
    numCats = input()  # Get user input

    try:
        numCats = int(numCats)  # Try to convert input to an integer
        if numCats < 0:  # Check if the number is negative
            print('Please enter a positive number.')
        else:  # If numCats is a positive integer
            if numCats >= 4:
                print('That is a lot of cats.')
            else:
                print('That is not that many cats.')
            break  # Exit the loop since valid input is provided
    except ValueError:  # Handle non-integer inputs
        print('You did not enter a valid number type.')



##CHALLENGE LOOP WITH RANGE
while True:  # Start an infinite loop
    print('How many cats do you have? (Enter a number between 1 and 20)')
    numCats = input()  # Get user input

    try:
        numCats = int(numCats)  # Try to convert input to an integer
        if numCats in range(1, 21):  # Check if numCats is within the range of 1 to 20
            if numCats >= 4:
                print('That is a lot of cats.')
            else:
                print('That is not that many cats.')
            break  # Exit the loop since valid input is provided
        else:
            print('Wrong! Please enter a number between 1 and 20.')  # Handle out-of-range input
    except ValueError:  # Handle non-integer inputs
        print('You did not enter a valid number type.')