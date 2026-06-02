class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        # prefix = [1, 1, 2, 8]

        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        # suffix = [48, 24, 6, 1]

        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]

        return res

    # O(n) for both

    # or define res=[] and use res.append(prefix[i] * suffix[i]), cuz append grows the list dynamically.

        










        # O(n2) - Brute Force
        # res = [1] *len(nums)

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             res[i] *= nums[j]
        
        # return res









