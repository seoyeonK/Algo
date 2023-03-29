prices = [7,6,4,3,1]

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxP = 0
        L=0
        R=1
        for i in range(0,len(prices)-1):
            profit = prices[R] - prices[L]
            if profit > maxP:
                maxP = profit
            else:
                L=R
            R +=1
        return maxP 

print(Solution.maxProfit(prices))

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l, r = 0, 1 # left = buy, right = sell
#         maxP = 0

#         while r < len(prices) :
#             if prices[l] < prices[r]:
#                 profit = prices[r] - prices[l]
#                 maxP = max(profit, maxP)
#             else:
#                 l = r
#             r += 1
#         return maxP