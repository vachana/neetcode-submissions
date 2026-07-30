class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0

        for r in range(len(prices)):
            while prices[r] < prices[l]:
                l +=1
            else:
                res = max(res, prices[r]-prices[l])
        
        return res

            
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        # l = 0
        # res = 0

        # for r in range(1,len(prices)):
        #     if prices[r] < prices[l]:
        #         l = r
        #     else:
        #         res = max(res, prices[r] - prices[l])

        # return res

# O(n) and O(1)

# They ask you to return the best days to buy and sell stock
# class Solution:
#     def maxProfitDays(self, prices):

#         l = 0
#         max_profit = 0

#         buy_day = 0
#         sell_day = 0

#         for r in range(1, len(prices)):

#             # found a cheaper buying price
#             if prices[r] < prices[l]:
#                 l = r

#             else:
#                 profit = prices[r] - prices[l]

#                 if profit > max_profit:
#                     max_profit = profit
#                     buy_day = l
#                     sell_day = r

#         return [buy_day, sell_day]
            



             
        