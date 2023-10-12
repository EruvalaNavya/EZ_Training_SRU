#to find out longest palindrome in string
def longestPalindrome(s):
        n=len(s)
        def ispalin_rev(i,j):
            while i>=0 and j<n and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j] 
        res=""
        for i in range(len(s)):
            if len(s)==1:
                return s
            pal=ispalin_rev(i,i)
            if len(pal)>len(res):
                res=pal
            pal1=ispalin_rev(i,i+1)
            if len(pal1)>len(res):
                res=pal1
        return res
s=input()
print(longestPalindrome(s))
