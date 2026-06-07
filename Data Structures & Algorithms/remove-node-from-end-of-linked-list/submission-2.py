# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        res = head
        l = 0
        temp = ListNode(0)
        temp.next = head
        res = temp

        while curr:
            l +=1
            curr = curr.next

        skip = l - n

        while temp and temp.next:
            if skip == 0:
                print(temp.val)
                temp.next = temp.next.next
                break #u don't need to traverse the rest, it remains the same
            skip -=1
            temp = temp.next
        
        return res.next

        # SC: O(1) and TC:O(n)
        
        

