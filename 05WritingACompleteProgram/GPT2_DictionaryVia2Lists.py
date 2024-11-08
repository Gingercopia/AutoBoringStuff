##### PROBLEM 2. Given two lists: one containing names and the other containing ages, create a dictionary where the names are the keys and the ages are the values.

#ATTEMPT 1 - FAIL
name = ['Raptor', 'Ghoul', 'Zombie']
weapon = ['Claws', 'Pyschic', 'Disease']

monsters = dict(name[0]weapon[1]) #fails since need keyword NOT index/positional arguments)

print (monsters)

######ATTEMPT 1 GPT SOLUTIONS
#Dict created via index but only saves once 

#name = ['Raptor', 'Ghoul', 'Zombie']
#weapon = ['Claws', 'Psychic', 'Disease'
# monsterTable = {name[0]: weapon[0]}

###OR nested for loop inside blank dictionary{}
#name = ['Raptor', 'Ghoul', 'Zombie']
#weapon = ['Claws', 'Psychic', 'Disease'
#monsterTable = {name[i]: weapon[i] for i in range(len(name))}

###OR use of ZIP fx to stitch list into key:value. Horse will not return as a key since no matching value in weapon. 
#name = ['Raptor', 'Ghoul', 'Zombie', 'Horse']
#weapon = ['Claws', 'Psychic', 'Disease']
#monsterTable = dict(zip(name, weapon))


### 
# Output: {'Raptor': 'Claws', 'Ghoul': 'Psychic', 'Zombie': 'Disease'}

name = ['Raptor', 'Ghoul', 'Zombie']
weapon = ['Claws', 'Psychic', 'Disease']
monsterTable = {name[i]: weapon[i] for i in range(len(name))}


#Attempt 2 - FAIL
monsterAttributes ={}
name = ['Raptor', 'Ghoul', 'Zombie']
weapon = ['Claws', 'Pyschic', 'Disease']

for monster in name(): #xxxx fail since iterate over list name not name() - range(len(name))
    monsterAttributes.setdefault (name, weapon) #xxxonly use setdefault to create default value for looped through keys if no value.
    monsterAttributes[monster] = monsterAttributes[monster] + weapon#xxxchange to add weapon directly to monster iteration

print(monsterAttributes)


#ATTEMPT 2 - GPT SOLUTION

monsterAttributes = {}
name = ['Raptor', 'Ghoul', 'Zombie']
weapon = ['Claws', 'Psychic', 'Disease']

# Correct the loop to iterate over 'name' list
##range() - makes numbers 0 to n-1 range(10(n-1=9))
##len() - returns number of items in object i.e. 3 for name
##i represents the index value so name is key and i is value. 
for i in range(len(name)): #loops of indexes of 
    #iteration 1 accesses dictionary[name[0]] = weapon[0] - uses list index
    monsterAttributes[name[i]] = weapon[i]

print(monsterAttributes)



#WHAT TO DO IF BLANK VALUE - i.e. LIST LENGTHS DON't MATCH
monsterAttributes = {}
name = ['Raptor', 'Ghoul', 'Zombie', 'Horse']
weapon = ['Claws', 'Psychic', 'Disease']

for i in range(len(name)):
    if i < len(weapon):
        monsterAttributes[name[i]] = weapon[i]
        
    else:
        monsterAttributes [name[i]] = "NA"

print(monsterAttributes)