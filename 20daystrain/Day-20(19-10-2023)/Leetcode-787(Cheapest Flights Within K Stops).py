class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        p=[float("inf")]*n
        p[src]=0
        for i in range(k+1):
            temp=p.copy()
            for s,d,w in flights:
                if p[s]!=float("inf") and p[s]+w<temp[d]:
                    temp[d]=p[s]+w
            p=temp
        return -1 if p[dst]==float("inf") else p[dst]
