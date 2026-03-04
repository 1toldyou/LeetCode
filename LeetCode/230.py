# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1
        i = 0
        def recur(root: Optional[TreeNode]):
            if not root:
                return
            nonlocal i
            nonlocal ans
            if i > k:
                return
            recur(root.left)
            i += 1
            if i == k:
                ans = root.val
                return
            recur(root.right)
        recur(root)
        
        return ans