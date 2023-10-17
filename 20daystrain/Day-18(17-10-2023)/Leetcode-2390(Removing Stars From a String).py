class Solution:
    def removeStars(self, s: str) -> str:
        st=collections.deque()
        for i in s:
            if not st:
                st.append(i)
            elif i=="*":
                st.pop()
            else:
                st.append(i)
        return "".join(st) 
