#given a word, print result of exteninding any long vowels to length of 5
word = input('Enter a word')
word_list = list(word)
long_vowels= ['aa', 'ee', 'ii', 'oo', 'uu'] #what i'm looking for in word
long_vowels2 = ['aaa', 'eee', 'iii', 'ooo', 'uuu']
# word_list = list(word) #break down word into indiviual letters
# print(word_list.count(long_vowels)) 
for i in range(len(word)):
    for c in range(len(long_vowels)):
        if word_list[i] == long_vowels[c]:
            word = word.extend(long_vowels2[i])
print(word)