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
        output = [[root.val]]
        miniQ = root

        while queue:
            n = len(queue)
            sub = []
            for i in range(n):
                x = queue.pop(0)
                l = x.left
                r = x.right
                if l:
                    queue.append(l)
                    sub.append(l.val)

                if r:
                    queue.append(r)
                    sub.append(r.val)
            if sub:
                output.append(sub)

        return output
