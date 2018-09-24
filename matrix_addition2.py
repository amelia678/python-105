# given two matricies of any given size (as long as they're the same),
# print new matrix with corresponding values

a = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

b = [[5, 8, 1],
    [6, 7, 3],
    [4, 5, 9]]
#new, empty matrix
result = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]    
#use a nested loop
# iterate through rows
for i in range(len(a)):
    #iterate trough columns
    for j in range(len(a[0])):
        result[i][j] = a[i][j] + b[i][j]
#print new matrix
for r in result:
    print(r)
