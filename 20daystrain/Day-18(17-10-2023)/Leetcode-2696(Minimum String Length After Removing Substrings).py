class Solution:
    def minLength(self, s: str) -> int:
        st=collections.deque()
        for i in s:
            if not st:
                st.append(i)
            elif (i=="B" and st[-1]=="A") or (i=="D" and st[-1]=="C"):
                st.pop()
            else:
                st.append(i)
        return len("".join(st))