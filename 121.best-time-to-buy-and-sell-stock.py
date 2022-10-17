#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Method 1
        buyPriceIndex = 0
        profit = 0
        for curr in range(len(prices)):
            if prices[curr] < prices[buyPriceIndex]:
                buyPriceIndex = curr
            else:
                profit = max(profit, prices[curr] - prices[buyPriceIndex])
        return profit

        # Method 2
        # sellPriceIndex = len(prices) - 1
        # curr = len(prices) - 1
        # profit = 0
        # while curr >= 0:
        #     # print(prices[curr])
        #     if prices[curr] > prices[sellPriceIndex]:
        #         sellPriceIndex = curr
        #     else:
        #         profit = max(profit, prices[sellPriceIndex] - prices[curr])
        #     curr -= 1
        # return profit


# @lc code=end
