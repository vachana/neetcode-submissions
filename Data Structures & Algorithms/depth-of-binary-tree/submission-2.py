# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        level = 0

        while queue:
            level +=1      #for each level increment
            for _ in range(len(queue)): #process all nodes in that level
                node = queue.popleft() 
                if node.left: queue.append(node.left)  
                if node.right: queue.append(node.right) 

        return level
        # O(n) for both

#  DFS Solution ->O(n) TC and O(h) SC
    # def maxDepth(self, root):
    # if not root: return 0
    # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))