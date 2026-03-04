# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        def recur(root: Optional[TreeNode]):
            if not root:
                return
            vals.append(root.val)
            recur(root.left)
            recur(root.right)
        recur(root)
        
        vals.sort()
        return vals[k-1]