# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -(2**32)
        def recur(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left = recur(root.left)
            right = recur(root.right)
            # print(f"val={root.val} left={left} right={right}")

            nonlocal ans
            ans = max(ans, left + root.val, left + root.val + right, root.val + right, root.val)
            return max(left + root.val, root.val + right, root.val)

        recur(root)

        return ans

        