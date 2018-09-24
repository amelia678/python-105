#given 2 lists of numbers the same length, multiply corresponding
# numbers and print in new list

a = [2, 4, 5]
b = [2, 3, 6]
new_list = []
for i in range(0, len(a)):
    new_list.append(a[i]*b[i])

print(new_list)