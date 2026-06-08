class Solution:
    def reverseBits(self, n: int) -> int:
        # Check if bit i is set:  (n >> i) & 1 (if it's 0 or 1)
        # move that bit(0 or 1 to the reversed position i.e (31-i))
        # OR each of it
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | bit << (31 - i)
        
        return res

# SC:O(1)
# Time: O(1) — always exactly 32 iterations regardless of input, so it's a fixed constant.