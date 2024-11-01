print('Hello world!')
#print ~ function, (arguments)
print ('What is your name?')
#myName ~ var ; input ~ function; (argument)
myName = input() 
#concat string with var value stored
print('it is good to meet you, ' + myName)
#provides string before providing length
print('The length of your name is: ')
#len ~ fx; ()~ argument; myName ~ parameter passed to method
print(len(myName))
print('What is your age?')
myAge = input() #input always returns a string but cannot do addition to a string so must convert to int then back to str
print('You will be ' + str(int(myAge) + 1) + ' in a year')