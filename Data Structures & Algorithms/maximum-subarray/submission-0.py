class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        sum_n = 0

        for n in nums:
            # check if restart or extend
            if n > (n + sum_n):
                sum_n = n #restart
            else:
                sum_n += n #extend
            
            max_sum = max(sum_n, max_sum)
        

        return max_sum



