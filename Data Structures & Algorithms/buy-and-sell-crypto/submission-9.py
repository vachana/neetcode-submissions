class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r, l = 1, 0
        res = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r +=1 
            else:
                res = max(res, prices[r] - prices[l])
                r += 1

        return res

# O(n) and O(1)
            



             
        