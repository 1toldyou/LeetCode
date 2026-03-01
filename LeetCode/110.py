# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recur(root: Optional[TreeNode]) -> Tuple[bool, int]:
            if not root:
                return True, 0
            
            left = recur(root.left)
            right = recur(root.right)
            if (not left[0]) or (not right[0]):
                return False, 0

            return abs(left[1]-right[1]) <= 1, max(left[1], right[1]) + 1

        return recur(root)[0]
        