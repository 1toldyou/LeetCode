# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def search(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root and not subRoot:
                return True
            elif not root:
                return False
            elif not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return search(root.left, subRoot.left) and search(root.right, subRoot.right)
        
        res = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return res or search(root, subRoot)
        