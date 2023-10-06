class Prime:
    def Magicprime(self,n):
        rev=0
        c1=0
        while n>0:
            rem=n%10
            rev=rev*10+rem
            n=n//10
        for i in range(2,rev):
            if rev%i==0:
                c1=c1+1
        if c1==0:
            print("Magic prime number")
        else:
            print("Not a Magic prime number")
class Neon:
    def Neonum(self,n1):
        for i in range(1,n1+1):
            sqr=i*i
            su=0
            if sqr>9:
                while sqr>0:
                    rem=sqr%10
                    su=su+rem
                    sqr=sqr//10
            else:
                su=sqr
            if(i==su):
                print(i,"is a neon number")
obj=Prime()
n=int(input())
obj.Magicprime(n)

obj1=Neon()
n1=int(input("Enter a num:"))
obj1.Neonum(n1)
