                                  # STEP 1
                                    # create a container to hold a message i.e. message. each letter is a different value stored inside of the message container  
message = 'It was a bright cold day in April, and the clocks were striking thirteen.' 
count = {}                        #STEP 2 
                                    # create container to hold count of key value pairs pulled from message container 

for character in message.upper(): #STEP 3 
                                    # Remove a value from message container (1st iteration) that hasn't been used
                                    # 
                                    # name a var to store loop iterations in
                                    # convert message to capital letters.
                                    # look in message for value
                                    # 1st iteration will return letter "I"
                                    # 2nd iteration returns "T"
                                    # 3rd iteration returns " "
                                    # 4th iteration returns "W"  
                            
                                  #STEP 6 store iteration 2 as "T"
    count.setdefault(character, 0) #STEP 4
                                        #Does iteration (i.e. character) exist in count dictionary?
                                        #IF NO - create a key i.e. "I" in the COUNT container and return the value of 0 as default
                                    #STEP 7 
                                        #T doesn't exist so DEFAULT
    count[character] = count[character] + 1 #STEP 5 
                                               #LEFT
                                                    #use character i.e. letter from count (iteration 1 = "I") and assign new value using last assigned set character value in count dictionary to the current iteration (e.g. "I") then adding 1 (i.e. + 1). This updates that characters value.
                                                    #assign iteration to iteration value i.e. character to add 1.
                                                        # "I":0 = "I":0 + 1
                                                        #   "I" = 1
                                                    
                                               #RIGHT 
                                                    #count[character] i.e index/key access - current count(value) of character KEY
                                                    # +1 adds increment of 1
                                               # 
                                               # 5 assign character variable to    
                                                #count dictionary i.e. count and add 1. return value to global count
                                                #count dictionary [place key of 2 with value assigned] = check dictionary for 
                                                ##[key] + 1 add one to create value for key    
                                                #dictionary - add 1 to "I" 
                                            #STEP 8 add 1 to "T"

print(count) #COMPLETED WHEN NO MORE ITERATIONS TO DO FROM MESSAGE
