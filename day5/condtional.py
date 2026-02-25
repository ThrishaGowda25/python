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


a=int(input())
b=int(input())
c=int(input())
res=a>100 and b>100 and c>100
if res:
    print("All are greater than 100")
else:
    print("Not all are greater than 100") 

n=input()
word=int(n[1:])
if word<30:
    print("Ground Floor")
else:
    print("Not Ground Floor")

a=int(input())
b=int(input())
c=int(input())
res=(a-b)<25 and (b-c)<25 and (c-a)<25
if res:
    print("Difference is less than 25")
else:
    print("Difference is not less than 25")