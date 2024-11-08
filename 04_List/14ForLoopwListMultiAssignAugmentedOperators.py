#FOR executes certain # times e.g. 4
for i in range(4): #i is var iteration saves to
    print(i)

#FOR repeats code once for each value in list
for i in range(4): #i is var iteration saves to
    print(i)
#RETURNS RANGE OBJECT i.e. LIST
range(4) 

#FOR LIST returns same range
for i in [0,1,2,3]: #assigns 1st item 0 then run code and repeat.
    print (i)

#GETS LIST VALUE OF RANGE
list(range(4))

###CONFIRM RANGE WITH LEN
######for i in range(len(someList))
supplies =['pens','paper', 'stapler', 'eraser']
supplies
['pens', 'paper', 'stapler', 'eraser']
#
### i is the iteration convert to string, pass range fx length of supplies to use i as index in code
###RANGE LEN LETS YOU USE i TO REFER to INDEX & LIST VALUE. use if need integer index and range len variable.
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies(i))




###RETURNING ITERATION and INDEX VALUE FROM LIST
supplies =['pens','paper', 'stapler', 'eraser']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

repeat = supplies*3
print(repeat)

supplies = ['pens','paper', 'stapler', 'eraser']*10

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

###MULTIPLE ASSIGNMENT FROM LIST VALUE TO VAR
cat = ['fat', 'orange', 'loud']
#Single assignment
size = cat[0]
color = cat[1]
disposition = cat[2]
print(color)

#Multiple Assignment
cat = ['tiny', 'black', 'loud']
size, color, disposition = cat
print(color)


####MULTIPLE ASSIGNMENTS OF VAR and LIST
#multi var on left assigned to multi values on right. Assigns multiple var to values in 1 line
size, color, disposition = 'chunky','tan','angry'
print(color)

###SWAPPING VARIABLES
#a gains b's value and b = a's value
a='AAA'
b='BBB'
a,b = b,a
print(a,b)

###AUGMENTED ASSIGNMENT OPERATORS
spam = 42
spam = spam+1
print(spam)
#avoid retyping var name
spam += 1
print(spam)