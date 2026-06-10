# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

#  DFS Solution ->O(n) TC and O(h) SC
# DFS — O(h) where h is the height of the tree

# The call stack only holds one path from root to leaf at a time
# Best case (balanced tree): O(log n)
# Worst case (skewed tree like a linked list): O(n)

# DFS — naturally gives you depth through the call stack,BFS is overkill 
# Both visit all n nodes — that's why time is O(n) for both, no difference there.Yes both visit all n nodes — that's why time is O(n) for both, no difference there.
# Space is different because it's not about how many nodes you visit, it's about how many nodes you need to hold in memory at the same time.

        if not root:
            return 0

        level =0
        queue = deque([root])

        while queue:
            level +=1

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return level

        # TC:O(n) and SC:O(h) for BFS 



















        # if not root:
        #     return 0
        # queue = deque([root])
        # level = 0

        # while queue:
        #     level +=1      #for each level increment
        #     for _ in range(len(queue)): #process all nodes in that level
        #         node = queue.popleft() 
        #         if node.left: queue.append(node.left)  
        #         if node.right: queue.append(node.right) 

        # return level
        # O(n) for both


    # def maxDepth(self, root):
    # if not root: return 0
    # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))