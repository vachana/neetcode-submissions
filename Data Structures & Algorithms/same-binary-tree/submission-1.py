# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        # p == q compares object identity, not values

        # TC: O(n) and SC: O(h)
        # Balanced tree: O(log n)
        # Skewed tree (essentially a linked list): O(n)