"""
###TRUTHY and FALSY
print('Enter a name ')
name = input() # returns string input
if name: #name is a string but python recognizes as TRUTHY so can do comparison with if. Blank would be FALSY
    print('Thank you for entering a name')
else:
    print('You did not enter a name')"""

###Avoid TRUTHY and FALSY
print('Enter a name ')
name = input() # returns string input
if name !='': #makes more explicit. name not equal to blank string run this block
    print('Thank you for entering a name')
else:
    print('You did not enter a name')