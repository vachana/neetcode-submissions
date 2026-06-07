class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # a^a = 0
        # 0 ^ b = b
        res = 0

        for n in nums:
            res = res^n
        
        return res
    
    # TC: O(n) and SC: O(1)
