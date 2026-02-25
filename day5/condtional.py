n=int(input())
if n>10:
    print(n+5)
if n<=10:
    print(n+1)

a=int(input())
b=int(input())
c=int(input())
sum=(a+b+c)==180
if sum:
    print("*")
    print("**")
    print("***")
else:
    print("Not a Valid Triangle")