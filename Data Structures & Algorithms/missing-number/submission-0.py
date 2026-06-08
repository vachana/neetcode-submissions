class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        sum_nums = n * (n+1)//2


        for n in nums:
            res += n
        
        return sum_nums - res


