class Solution:
    def isHappy(self, n: int) -> bool:
        n_set =set()
        # if n in n_set is O(1) with a set vs O(n) if you used a list.
        while n!=1:
            n_set.add(n)
            n = self.squareSum(n)
            if n in n_set: 
                return False

        return True

    def squareSum(self,n):
        val = 0
        while n:
            val += (n%10) ** 2
            n = n//10
        return val

# This is one of those cases where the math of the problem bounds the space for you
# O(1) SC->however bit the n, the set never grows beyond ~20 elements 
# TC:O(logn)->The number of digits in n is log10(n)

        
