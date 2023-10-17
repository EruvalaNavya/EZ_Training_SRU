class node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
q=[]
q.append(root)
while q:
    a=q.pop(0)
    print(a.val,end=" ")
    if a.left:
        q.append(a.left)
    if a.right:
        q.append(a.right)
