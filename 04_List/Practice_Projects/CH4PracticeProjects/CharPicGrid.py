grid = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]




# TAKE INDEX 0 of each INDEX 0-8 then Print

def x():
    x=0
    y=0
    for ix in range (9):
        #return value of index 0 in each list
        x1= grid[x+ix][y] #look at list 1, return index 0 etc....
        for iy in range (6):
            y1 = grid[x][y+iy]
    print(x1,y1)
    print(x1,y1)

x()

"""        
        print(x1, end=" ")
        print(x2, end=" ")
        print(x3, end=" ")
        print(x4, end=" ")
        print(x5, end=" ")
        print(x6, end=" ")
        #print(x7, end=" ")
        #print(x8, end=" ")
        #print(x9, end=" ")
    #+''+x2+''+x3+''+x4+''+x5+''+x6+''+x7+''+x8+''+x9)
"""



    
    
