## 121. Best Time to Buy and Sell Stock

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0

        for price in prices[1:]:
            if (price - buy > maxProfit):
                maxProfit = price - buy

            if (price < buy):
                buy = price

        return maxProfit

    def maxProfitWithPosition(self, prices: List[int]) -> int:
        buy = tempBuy = (0, prices[0])
        sell = None
        maxProfit = 0

        for i, price in enumerate(prices):
            if (price - tempBuy[1] > maxProfit):
                maxProfit = price - tempBuy[1]
                buy = tempBuy
                sell = (i, price)

            if (price < tempBuy[1]):
                tempBuy = (i, price)

        return maxProfit, buy, sell

    def maxProfitWithSmallestHold(self, prices: List[int]) -> int:
        buy = tempBuy = (0, prices[0])
        sell = None
        maxProfit = 0

        for i, price in enumerate(prices):
            if (price - tempBuy[1] > maxProfit):
                maxProfit = price - tempBuy[1]
                buy = tempBuy
                sell = (i, price)

            if (price <= tempBuy[1]):
                tempBuy = (i, price)

        return maxProfit, buy, sell

if __name__ == "__main__":
    # input = [7,1,5,3,6,4]
    input = [14, 13, 12, 11, 7, 5, 3, 4, 3, 4, 3, 6, 4, 3, 7, 5, 8, 9, 10, 11, 12, 13, 14, 15, 7, 15, 20, 4, 3, 2, 1]
    print(Solution().maxProfit(input))
    # print(Solution().maxProfitWithPosition(input))
    # print(Solution().maxProfitWithSmallestHold(input))