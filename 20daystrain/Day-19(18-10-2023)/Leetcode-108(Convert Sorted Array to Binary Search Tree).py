# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def tree(i,j):
            if i<=j:
                mid=(i+j)//2
                root=TreeNode(nums[mid])
                root.left=tree(i,mid-1)
                root.right=tree(mid+1,j)
                return root
        return tree(0,len(nums)-1)        
