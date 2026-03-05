# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = root

        pV = p.val
        qV = q.val

        if pV > qV:
            pV, qV = qV, pV

        def recur(root: Optional[TreeNode]):
            if not root:
                return

            nonlocal ans
            if root is p or root is q:
                ans = root
                return
            if pV < root.val and qV > root.val:
                ans = root
                return
            if pV < root.val and qV < root.val:
                recur(root.left)
            elif pV > root.val and qV > root.val:
                recur(root.right)

        recur(root)

        return ans
        