#given a list of numbers, create new list of positive numbers
positives= [90, 4, -100, -17, 70, -999]

new_list = [] #start with empty list

for i in positives:
    if i > 0: # checks if number is positive
        new_list.append(i) #adds number to new list

print(new_list)        