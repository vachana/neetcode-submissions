"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        map_newNode = {}

        curr = head
        # create new nodes for all.
        while curr:
            map_newNode[curr] = Node(curr.val)
            curr = curr.next 
        
        # point to the new next and random nodes
        curr = head
        while curr:
            if curr.next:
                map_newNode[curr].next = map_newNode[curr.next] 
                #curr.next is old and map[curr].next is new node
            if curr.random:
                map_newNode[curr].random = map_newNode[curr.random]
            curr = curr.next
        
        return map_newNode[head]
        
        # TC and SC: O(n)
