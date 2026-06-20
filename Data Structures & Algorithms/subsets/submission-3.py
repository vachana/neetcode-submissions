class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(start, current):
            res.append(current[:])#store copy of current
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i+1, current)
                current.pop()
        
        backtrack(0, [])
        return res

        # TC: O(n · 2^n),  There are 2^n subsets (each element is either in or out). For each subset, you do current[:] which costs O(n) to copy. So total = O(n · 2^n).
        # SC: O(n), The recursive call stack goes at most n levels deep (one level per element). current also holds at most n elements at any point.
  