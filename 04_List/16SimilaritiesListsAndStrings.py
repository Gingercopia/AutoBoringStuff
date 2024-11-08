list('Hello') #converts to list
#len, in, not in, index, slice, for loop, etc.

name = 'Zophie'
name[0]
name[1:3]
name[-2]
'Zo' in name
'xxx' in name
for letter in name:
    print(letter)

name = 'Zophie the cat'
name[7]
name[7] = 'x'


###PASSING LISTS IN FX CALLS
def eggs(cheese): #cheese var
    cheese.append('Hello')#local scope BUT since appending to the same reference as global spam variable it updates spam outside of the fx
spam = [1,2,3] #SPAM STORES REFERENCE OF LIST
eggs(spam) #spam argument passed to eggs parameter
print(spam)


####CREATE COMPLETE SEPERATE LIST WITH OWN REF
#COPIES NEW LIST FROM COPIED LIST
import copy #NEED IMPORT COPY MODULE
spam = [1,2,3,4]
cheese = copy.deepcopy(spam)#creates new list and ref

###CAN PLACE LIST ITEMS ON OWN LINE
spam = ['apples', 
        'oranges',
        'grapes']
###CONTINUE A LINE WITH \
print('For score and seven' + \
      'years ago'))