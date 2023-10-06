#for random values
'''import random
a=input('How idiot are you?-')
print(random.randint(1,100),'%')'''
#printing 1 to n using recursion
'''def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n)
n=int(input())
fun(n)'''
#print n to 1
'''def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
n=int(input())
fun(n)'''
#print sum of didgits
'''def fun(n):
    if n<=1:
        return n
    else:
        return n+fun(n-1)
n=int(input())
print(fun(n))'''
#check whether the string is palindrome or not.i/p=abbba,o/p=true
'''
#using conditions
st=input()
i=0
j=len(st)-1
while(i<j):
    if(st[i]!=st[j]):
        print("Not palindrome")
        break
    i+=1
    j-=1
else:
    print("Palindrome")'''
#using recursion
def fun(s,i,j):
    if s[i]!=s[j]:
        print("Not palindrome")
        return 
    elif i>j:
        print("Palindrome")
        return 
    else:
        return fun(s,i+1,j-1)
s=input("Enter string=")
fun(s,0,len(s)-1)


        






