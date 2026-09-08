# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invert(self, n: Optional[TreeNode]):
        if not n:
            return
        n.left, n.right = n.right, n.left

        self.invert(n.left)
        self.invert(n.right)
            
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root
    
    

        