# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        curr = head
        # temp = ListNode(1)
        # res = temp

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next


        reverse = self.reverseList(slow.next)
        slow.next = None

        # while curr and reverse:
            # temp.next = curr
            # curr = curr.next
            # temp = temp.next

            # temp.next = reverse
            # reverse = reverse.next
            # temp = temp.next
    # temp pointer keeps walking forward to build the chain, 
    # so you need res to remember the head — but then you're forced to 
    # return res.next, which violates the in-place requirement.
    # the above modifies the original chain by adding extra node at the head
        while curr and reverse:
            curr_next = curr.next
            rev_next = reverse.next

            curr.next = reverse
            reverse.next = curr_next

            curr = curr_next
            reverse = rev_next


    
    def reverseList(self, mid: Optional[ListNode]):
        temp = mid
        prev = None 

        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt 

        return prev
    

