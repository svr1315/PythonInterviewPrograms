class Solution:
    def maxProfit(self, prices: list[int])->int:
        buyP,sellP = 0, 1
        maxprofit = 0

        while sellP < len(prices):
            if prices[buyP] < prices[sellP]:
                profit = prices[sellP] - prices[buyP]
                maxprofit = max(maxprofit, profit)
            else:
                buyP = sellP
            sellP += 1

        return maxprofit

s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([2,2,2]))