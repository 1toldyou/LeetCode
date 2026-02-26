# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def recur(root: Optional[TreeNode]) -> Tuple[int, int]:
            if not root:
                return 0, 0
            l = recur(root.left)
            r = recur(root.right)
            return 1 + max(l[0], r[0]), max(l[0] + r[0], l[1], r[1])
            
        return recur(root)[1]
