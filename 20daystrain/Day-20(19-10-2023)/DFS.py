def dfs(start,vis):
    d={1:[2],2:[3,5],3:[5],4:[2,3],5:[]}
    vis.add(start)
    for i in d[start]:
        if i not in vis:
            dfs(i,vis)
    return vis
print(dfs(1,set()))
