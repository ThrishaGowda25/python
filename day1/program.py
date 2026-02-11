#program that reads a word and prints stars (*) = the length of the word
word=input()
length=len(word)
print(length*'*')
#print the last character of the word
length=(len(word)-1)
print(word[length])
#reads a word n prints the first letter of the given word n stars(*) instead of the other letters
word1=input()
first=word1[0]
otherwords=len(word1)-1
print(first+'*'*otherwords)
#prints the first n last letter of the given word n stars(*) instead of the other letters
word5=input()
first=word5[0]
last=word5[len(word5)-1]
length=len(word5)-2
print(first+'*'*length+last)
#program that reads a word and prints the word in the given format **** code ****(no of stars = to len og word)
word2=input()
length=len(word2)
print('*'*length+" "+word2 +" "+'*'*length)
#write a program that reads two words w1 and w2.w2 is at the beginning of w1.print the index at which w2 ends in w1
word3=input()
word4=input()
lenght=len(word4)-1
print(lenght)