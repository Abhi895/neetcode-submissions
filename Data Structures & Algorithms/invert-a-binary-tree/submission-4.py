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
        temp = n.left
        n.left = n.right
        n.right = temp

        self.invert(n.left)
        self.invert(n.right)
            
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        currNode = root
        self.invert(currNode)
        return currNode
    
    

        