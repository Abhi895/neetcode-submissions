# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        output = []

        while queue:
            n = len(queue)
            sub = []
            for i in range(n):
                x = queue.pop(0)
                sub.append(x.val)
                l = x.left
                r = x.right
                if l:
                    queue.append(l)
                if r:
                    queue.append(r)
            output.append(sub)

        return output
