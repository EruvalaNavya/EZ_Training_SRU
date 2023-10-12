class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[]
        def backtrack(i,curstr):
            if len(digits)==len(curstr):
                res.append(curstr)
                return
            for c in dict[digits[i]]:
                backtrack(i+1,curstr+c)
        if digits:
            backtrack(0,"")
        return res
