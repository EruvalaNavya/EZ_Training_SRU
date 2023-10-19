class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        l=[]
        def dfs(start,end,vis):
            if start==end:
                val=vis+[start]
                l.append(val)
                return
            vis.append(start)
            for i in graph[start]:
                if i not in vis:
                    dfs(i,end,vis)
            vis.pop()
        dfs(0,len(graph)-1,[])
        return l
