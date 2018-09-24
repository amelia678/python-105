# given two matricies, add corresponding values in new matrix 

a = [[1, 3],
    [2, 4]]

b = [[5, 2],
    [1, 0]]

result = [[0, 0],
        [0, 0]]

#iterate through rows
for i in range(len(a)):
    #iterate through columns
    for j in range(len(a[0])):
        result[i][j] = a[i][j] + b[i][j]
#prints each result
for r in result:
    print(r)        