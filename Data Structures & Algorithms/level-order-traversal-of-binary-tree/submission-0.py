# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []

        queue = deque([root])

        while queue:
            nodes_lvl = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node: 
                    nodes_lvl.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if len(nodes_lvl) > 0: res.append(nodes_lvl)
        
        return res