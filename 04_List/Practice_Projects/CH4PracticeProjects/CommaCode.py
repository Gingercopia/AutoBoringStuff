#MAKE STRING FROM A LIST with comma and space, and before last item

produce = ['apples', 'bananas','tofu', 'cats']

def produceList():
    shoppingFor = produce
    print(shoppingFor[0]+', ' + shoppingFor[1] + ', '+shoppingFor[2]+', and '+shoppingFor[3])
    return shoppingFor
produceList()