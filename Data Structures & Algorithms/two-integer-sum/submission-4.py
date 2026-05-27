class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}


        for i in range(len(nums)):
            if nums[i] in nums_map.keys():
                return [nums_map.get(nums[i]), i]

            nums_map[target - nums[i]] = i



















#         temp = {}

#         # for i in range(len(nums)):
#         #     if nums[i] in temp:
#         #         return [temp[nums[i]], i]
#         #     temp[target - nums[i]] = i

# # Same with enumerate

#         for i, n in enumerate(nums):
#             if n in temp:
#                 return [temp[n], i]
#             temp[target - n] = i

# # O(N) for both