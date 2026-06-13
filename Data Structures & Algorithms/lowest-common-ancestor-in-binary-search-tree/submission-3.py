# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        if p.val < root.val and q.val >root.val or q.val < root.val and p.val >root.val:
            return root
        

        if p.val == root.val:
            return p
        if q.val == root.val:
            return q
        
        return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)
    # SC: O(h) and TC:O(h)(You go down one path — at each node you eliminate one entire subtree. No backtracking)->Balanced tree: O(log n);Skewed tree: O(n)
    
    #  A or B returns the first truthy value — if A is not None, return A, otherwise return B.   
# LCA is unique — exactly one subtree will contain both p and q. So one side returns a node, the other returns None. or naturally picks the non-None result.
