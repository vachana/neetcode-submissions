class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # res = a ^ b
        # carry = (a & b) << 1

        # while carry:
        #     temp = res
        #     res = res ^ carry
        #     carry = (temp & carry) << 1
        
        # return res
# These two wont handle infite loop wit negative carry->In Python, 
# integers have infinite precision — unlike other languages where integers are 
# fixed 32 bits,Python will keep extending the carry left forever.
        # while b:
        #     carry = (a & b) << 1
        #     a = a ^ b
        #     b = carry
        # return a

        mask = 0xFFFFFFFF
        while b & mask:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry

        return a if a <= 0x7FFFFFFF else ~(a^mask)

    # SC and TC: O(1)