# given a word W and an integer N,write a program to print the character present at the index N in the word W
# INPUT: Chocolate
#      :  2
w=str(input())
n=int(input())
res=w[n]
print(res)

""" given a word and a number N,write a program to print the given word,N number of times in a single line"""
w=str(input())
N=int(input())
res=w*N
print(res)
"""program to read a single line input n print the first 3 characters of the input"""
a=input()
print(a[:3])