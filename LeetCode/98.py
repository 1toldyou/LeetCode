# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], lo=-(2**32), hi=2**32) -> bool:
        if not root:
            return True
        
        if root.left:
            if root.left.val >= root.val:
                return False
            if root.left.val <= lo or root.left.val >= hi:
                # print(f"{root.val}'s left child out of range", lo, hi)
                return False
        if root.right:
            if root.right.val <= root.val:
                return False
            if root.right.val <= lo or root.right.val>= hi:
                # print(f"{root.val}'s right child out of range", lo, hi)
                return False
        
        return self.isValidBST(root.left, lo=lo, hi=root.val) and self.isValidBST(root.right, lo=root.val, hi=hi)
