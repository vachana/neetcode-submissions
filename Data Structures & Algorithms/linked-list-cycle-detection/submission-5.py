# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head       


        while fast and fast.next: #slow is always begind fast, so don't need to check
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

# TC:O(n) and SC:O(1)