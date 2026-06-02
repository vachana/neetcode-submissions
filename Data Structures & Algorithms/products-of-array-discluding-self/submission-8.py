class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] *len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    res[i] *= nums[j]
        
        return res


























        product, temp = 1, 1

        for n in nums:
            if n == 0:
                temp = product
            product *= n
            if n !=0:
                temp *= n

        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = temp
            else:
                nums[i] = product // nums[i]
        
        return nums

        # O(1) SC and O(n) TC
