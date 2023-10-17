class Solution:
    def isValid(self, s: str) -> bool:
        st=collections.deque()
        if len(s)<=1:
            return False
        for i in s:
            if not st:
                st.append(i)
            elif ((i==')' and st[-1]=='(') or (i==']' and st[-1]=='[') or(i=='}' and st[-1]=='{')):
                st.pop()
            else:
                st.append(i)
        if not st:
            return True
        return False
