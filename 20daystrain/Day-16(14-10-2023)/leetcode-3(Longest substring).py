class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        j,length=0,0
        res=set()
        for i in range(n):
            while s[i] in res:
                res.remove(s[j])
                j+=1
            res.add(s[i])
            length=max(length,(i-j+1))
        return length
