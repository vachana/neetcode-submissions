class Solution:
    def hammingWeight(self, n: int) -> int:
        # Turn off rightmost set bit: n & (n - 1)
        count =0

        while n >0: #or while n:
            n = n & (n-1)
            count +=1
        
        return count

# O(1) TC and SC
    
