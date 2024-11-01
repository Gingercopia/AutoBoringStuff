#var inside a fx (i.e. local var in local scope) can have same name as var outside of fx's (i.e. Global var in global scope)

spam = 42 #global var - value stored and remains. Created when program starts and destroyed when program ends
def eggs():
    spam = 42 #local var - created when function called destroyed after fx returns value. 
print ('some code here.')#part of global since outside function of eggs()
print('some more code')#part of global

#1. Code in global cannot use local var (i.e. eggs)
def spam(): #1 spam is defined
    eggs = 99 #3 eggs value 99 assigned (ONLY LOCALLY)
    #RETURN - returns value of 99 and local scope is destroyed and var in local scope are forgotten
spam() #2 spam is called
spam()
print(eggs) #4 prints eggs

#4 1 Local Scope cannot use another Local Scope Cariable
#each egg var is defined locally so are referring to different local scopes
def spam(): #1 spam defined #4 local scope created when spam called from 3
    eggs = 99 #5 local var assigned 99
    bacon() #6 bacon fx called from spam local scope #10 
    print(eggs) #11 prints out spam's eggs variable

def bacon():#2 bacon defined #7 bacon executes with local scope of own
    ham = 101 #8 local ham assigned 101
    eggs = 0 #9 local eggs assigned 0
    #RETURN - #10 destroys this local ham and eggs var values

spam()#3 spam fx called

#2 Code in a local scope can access Global

def spam(): #1 define spam fx
    eggs = 21 #causes python to run as local var
    print(eggs) #4 prints value of global var since eggs in this instance has NO ASSIGNMENT (=). Otherwise, eggs = 2 would override the global

eggs = 42 #2 assign global var eggs value
spam()#3 call spam fx

#REASSIGNING GLOBAL VAR from LOCAL VAR
def spam(): 
    global eggs #global statement ensures code uses global value even if assignment of local in fx block
    eggs = 'Hello' 
    print(eggs) 

eggs = 42 #change global var to 'hello'
spam()