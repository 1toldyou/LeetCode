# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        q.append(root)
        res = []

        nextLevel = []
        while q:
            level = []
            for node in q:
                if not node:
                    continue
                level.append(node.val)
                nextLevel.append(node.left)
                nextLevel.append(node.right)
            q = nextLevel
            nextLevel = []
            res.append(level)
            level = []

        return res[:-1]