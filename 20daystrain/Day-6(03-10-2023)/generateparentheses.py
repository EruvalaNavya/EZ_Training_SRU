class Solution:
    def generateParenthesis(n):
        l=[]
        res=[]
        def backtrack(oc=0,cc=0):
            if oc==cc==n:
                res.append("".join(l))
            if oc<n:
                l.append('(')
                backtrack(oc+1,cc)
                l.pop()
            if cc<oc:
                l.append(')')
                backtrack(oc,cc+1)
                l.pop()
            return res
        return backtrack()
n=int(input())
k=Solution.generateParenthesis(n)
for i in k:
    print(i)
