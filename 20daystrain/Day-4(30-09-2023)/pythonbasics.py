'''A-Z=65-90,a-z=97-122'''
#character index positon
var=input()
if(ord(var)>96):
    print(ord(var)-96)
else:
    print(ord(var)-64)
#i.p:h,3 o.p:k
var=input()
n=int(input())
if(ord(var)+n)>122:
    print(chr(ord(var)+n-26))
else:
    print(chr(ord(var)+n))
#i/p:4,o/p:*  ** *** ****
n=int(input())
for i in range(n):
    print("* " * (i+1))
#o/p:pyramid pattern
n=int(input())
for i in range(n):
    print(" "*(n-i)+"* "*(i+1))
for i in range(n):
    print(" "*(i+1)+"* "*(n-i))
#o/p:1 22 333 ...
n=int(input())
for i in range(n):
    print(str(i+1)*(i+1))
#o/p:1 22 333 4444....
n=int(input())
for i in range(1,n+1):
    print(((10**(i))//9)*i)
