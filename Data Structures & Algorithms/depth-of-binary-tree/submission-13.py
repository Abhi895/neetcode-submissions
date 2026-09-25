# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        rightDepth = 0
        leftDepth = 0

        if not root:
            return 0

        def dfsFrom(node: Optional(TreeNode)):
            if not node:
                return 0
            # if not node.left and not node.right:
            #     return 1
            leftDepth = dfsFrom(node.left)
            rightDepth = dfsFrom(node.right)
            return 1 + max(leftDepth, rightDepth)


        return dfsFrom(root)







                