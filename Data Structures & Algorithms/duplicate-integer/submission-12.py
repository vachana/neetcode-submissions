class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()

        for n in nums:
            if n in nums_set:
                return True
            nums_set.add(n)
        
        return False


    

















        # # Solution1: O(N) for both but no early exit if duplicate found
        # # set_nums = set(nums)
        # # return len(set_nums) != len(nums)

        # # Solution2: O(N) for both
        # # A set gives you:
        # #  - Average O(1) lookup → if num in set_nums
        # #  - Average O(1) insert → set_nums.add(num)
        # # (Same for dict but O(N) for lookup in list)
        # #   A set is basically a dict without values
        # set_nums = set()
        
        # for num in nums:
        #     if num in set_nums:
        #         return True
        #     set_nums.add(num)
        # return False

        # # Solution3: O(N) for both
        # # Same as above with dictionary.
        # # dict_nums = {}

        # # for num in nums:
        # #     if num in dict_nums:
        # #         return True
        # #     dict_nums[num] = True
        # # return False

        # # Solutionx:
        # # temp = [0 for i in range(50000)]

        # # for n in nums:
        # #     if temp[n] == 1:
        # #         return True
        # #     else:
        # #         temp[n] = 1 
        # # return False




