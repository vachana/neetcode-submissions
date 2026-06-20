class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtracking(start, current):
            sum_curr = sum(current)
            if sum_curr == target:
                res.append(current[:])
                return
            
            if sum_curr > target: #Without this check, you'd keep appending more numbers forever — since elements can be reused (i not i+1), there's no natural stopping point. The recursion never ends.
                return

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtracking(i, current)#i+1 should be i cuz number can be repeated
                current.pop()
            
        backtracking(0, [])
        
        return res
        # n = number of candidates, t = target value.
        #TC: O(t. 2^t)In the worst case the recursion tree has 2^t nodes (each step you either reuse the same element or move on).At each node you do sum(current) which costs O(t) in the worst case (current can hold at most t/min_element numbers).
        # SC:O(n.t).The recursion stack goes at most t / min_element levels deep — in the worst case every element is 1, so you go t levels deep.