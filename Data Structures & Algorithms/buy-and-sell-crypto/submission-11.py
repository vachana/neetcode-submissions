class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0

        for r in range(1,len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])

        return res

# O(n) and O(1)

# They ask you to return the best days to buy and sell stock
            



             
        