class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Using Sum(n) = n(n+1)//2
        res = 0
        n = len(nums)
        sum_nums = n * (n+1)//2

        for num in nums:
            res += num
        
        return sum_nums - res


