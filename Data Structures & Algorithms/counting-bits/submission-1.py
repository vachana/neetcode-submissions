class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        i = 0
        print(res)

        while i <= n:
            res[i] = self.hammingWeight(i)
            i +=1
        return res
    

    def hammingWeight(self, n: int) -> int:
    # Turn off rightmost set bit: n & (n - 1)
        count =0

        while n >0:
            n = n & (n-1)
            count +=1
        
        return count