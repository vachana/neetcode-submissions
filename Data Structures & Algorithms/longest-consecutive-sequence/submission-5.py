class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:











        # Brute Force O(n2)
        res = 0

        for n in nums:
            temp = n
            count =1
            
            while temp+1 in nums: #O(n) operation
                count +=1
                temp +=1
            
            res = max(res, count)
        
        return res





















        # new_nums = set(nums)
        # max_length = 0

        # for n in nums:
        #     length = 1
        #     if n-1 not in new_nums:
        #         i = 1
        #         while (n+i) != n and (n+i) in new_nums:
        #             # for case :[-1,0] add (n+i) != n above
        #             length += 1
        #             i +=1
        #     if max_length < length:
        #         max_length = length

        # return max_length

        # # O(n) TC and SC



                
             