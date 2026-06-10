class Solution:
    def isHappy(self, n: int) -> bool:
        n_set =set()
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

        
