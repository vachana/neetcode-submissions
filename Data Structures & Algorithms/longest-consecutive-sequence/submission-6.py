class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)

        for n in nums:
            if n-1 not in nums_set: #avoids worst case O(n2) by avoiding repetition
                temp = n
                count = 1
                
                while temp+1 in nums_set: #O(1) operation
                    count +=1
                    temp +=1
                
                res = max(res, count)
        
        return res       

# O(n) for both SC and TC






# if num - 1 not in nums_set  # O(1) ✓cuz uses hashing->looking for 4?→ hash(4) = some index
# if num - 1 not in nums_list # O(n) ❌ — has to scan every element

# Set  → O(1) lookup  but no order, no duplicates
# List → O(n) lookup  but keeps order and duplicates

        # Brute Force O(n2)
        # res = 0

        # for n in nums:
        #     temp = n
        #     count =1
            
        #     while temp+1 in nums: #O(n) operation
        #         count +=1
        #         temp +=1
            
        #     res = max(res, count)
        
        # return res




                
             