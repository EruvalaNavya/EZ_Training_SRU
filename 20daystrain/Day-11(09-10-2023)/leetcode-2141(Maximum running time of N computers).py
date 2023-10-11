class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        total=0
        for i in range(len(batteries)):
            total+=batteries[i]
        while batteries[-1]>total//n:
            total-=batteries[-1]
            batteries.pop()
            n-=1
        return total//n
