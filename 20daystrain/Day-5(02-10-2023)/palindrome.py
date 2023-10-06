#check whether the string is palindrome or not.i/p=abbba,o/p=true
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
    print("Palindrome")
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

