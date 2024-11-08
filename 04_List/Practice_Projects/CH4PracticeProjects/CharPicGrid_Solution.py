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
#number of sublists
num_sublists = len(grid)

#number of indices in each sublist
##[0] pulls from the very 1st sublist (i.e. 1st row)
num_index = len(grid[0])

#i CREATES ITERATION OF EACH INDEX
for i in range(num_index):
    #j CREATES ITERATION FOR EACH SUBLIST
    for j in range(num_sublists):
        #PRINTS iterations [sublist#] [index#]. end places each print on new line
        print(grid[j][i], end=' ')
    #PRINTS NEXT LINE AFTER PRINTS EACH INDEX
    print()













    
    
