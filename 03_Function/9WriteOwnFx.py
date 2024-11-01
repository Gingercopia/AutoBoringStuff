"""
###CREATE A FUNCTION
def hello(): #def defines fx
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

hello()#EACH calls the created fx
hello()
hello()
"""

"""
#ADD ARGUMENTS FOR name PARAMETER
def hello(name): #name is PARAMETER of hello fx
    print('Howdy! ' + name)

hello('Alice')#Alice is ARGUMENT passed to PARAMETER when hello fx called
hello('Bob')#Bob is ARGUMENT passed to PARAMETER when hello fx called
hello()
len('hello')

"""

###RETURN STATEMENTS

#number param holds argument passed in
def plusOne(number): 
    #value of number + 1 is the RETURN VALUE of plusOne function
    return number + 1
#create new var to store fx value
#pass argument (5) to plusOne parameter
newNumber = plusOne(5)
#output is result of number i.e. 5 + 1
print(newNumber)

#KEYWORD ARGUMENTS (end, sep)
#print adds new line character after run
print('Hello')
#end removes new line
print('World', end='')
print('Domination')
# , adds spaces between str
print('cat', 'dog', 'mouse')
# sep keyword adds a seperator type
print('cat', 'dog', 'mouse', sep=',')