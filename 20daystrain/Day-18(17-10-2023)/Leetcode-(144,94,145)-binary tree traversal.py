class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #preorder
        l=[]
        def preord(root):
            if root==None:
                return
            else:
                l.append(root.val)
                preord(root.left)
                preord(root.right)
            return l
        return preord(root)
        #inorder
        l=[]
        def inord(root):
            if root==None:
                return
            else:
                inord(root.left)
                l.append(root.val)
                inord(root.right)
            return l
        return inord(root)
        #postorder
        l=[]
        def postord(root):
            if root==None:
                return
            else:
                postord(root.left)
                postord(root.right)
                l.append(root.val)
            return l
        return postord(root)
