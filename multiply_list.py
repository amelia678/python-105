#given a list of numbers and a single factor, create new list consisiting of 
#each of the numbers multiplied by the factor
list_to_multiply = [3, 6, 9, 12, 15, 18]
factor = 2

new_list = []

for i in list_to_multiply:
    z = i * factor
    new_list.append(z)

print(new_list)    