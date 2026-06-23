"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {} # hashmap: original node -> cloned node

        def dfs(node):
            if node in visited:
                return visited[node]
            
            clone = Node(node.val)
            visited[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        if not node:
            return None
        else:
            return dfs(node)    


# Time: O(V + E)

# V = vertices (nodes), E = edges (neighbors)
# You visit every node once (hashmap prevents revisits), and for each node you iterate through all its neighbors

# Space: O(V)

# The visited hashmap stores one entry per node
# Recursion call stack is O(V) in the worst case (a linear chain of nodes)
# So O(V) + O(V) = O(V)    


        