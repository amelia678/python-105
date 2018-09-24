paragraph = input('Enter a passage to be translated into Leetspeak').upper() #user input

#need to convert A => 4
# E => 3
# G => 6
# # I => 1
# O => 0
# S => 5
# T => 7

leet= ['A', 'E', 'G', 'I', 'O', 'S', 'T']  #letters to be tranlated 
num = ['4', '3', '6', '1', '0', '5', '7'] #leet translation

for c in range(len(paragraph)): #for each letter in paragraph
    for i in range(len(leet)): # for each letter in [leet]
        if leet[i] == paragraph[c]: #comparing paragraph to [leet]
            paragraph = paragraph.replace(paragraph[c], num[i]) #if letter in paragraph matches
                                                                #[leet] replace w [num]
print(paragraph)

        
