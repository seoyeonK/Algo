
# #첫시도 -> FAIL   :  O(N^2) -> time out 

# class Solution(object):
#     def maxProfit(self, prices):
#         max=0
#         for i in range(len(prices)-1) :
#             for j in range(i+1, len(prices)):
#                 profit = prices[j] - prices[i]
#                 if profit > max:
#                     max = profit

#         return max

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left = buy, right = sell
        maxP = 0

        while r < len(prices) :
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1
        return maxP