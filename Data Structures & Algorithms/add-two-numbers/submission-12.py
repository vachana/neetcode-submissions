# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #    O(n) auxiliary space because of the strings a and b.
    # O(m+n) TC
    #     a = ""
    #     b = ""
    #     res = ""

    #     while l1:
    #         a = a + str(l1.val)
    #         l1 = l1.next
        
    #     while l2:
    #         b =  b + str(l2.val)
    #         l2 = l2.next

    #     res = self.reverseDigits(int(a)) + self.reverseDigits(int(b))

    #     head = ListNode(0)
    #     curr = head
    #     while res>0:
    #         head.next = ListNode(res%10)
    #         head = head.next
    #         res = res//10
        
    #     return curr.next
        
    # def reverseDigits(self, n):
    #     n_rev = 0
    #     while n > 0 :
    #         digit = n%10
    #         n_rev = n_rev * 10 + digit 
    #         # n_rev *= 10 + digit is wrong cuz *= tigtly couples n_rev 
    #         # ie, n_rev = n_rev * (10 +digit) -->WRONG
    #         n = n//10
        
    #     return n_rev



        head = ListNode(0)
        curr = head
        carry =0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry

            carry = total // 10

            curr.next = ListNode(total % 10)

            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return head.next

        
    # easier way and O(1) auxiliary time




        

