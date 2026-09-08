class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        currentPrice = prices[0]

        for price in prices[1:]:
            if currentPrice > price:
                currentPrice = price
            profit = price - currentPrice
            max_profit = max(max_profit, profit)
        return max_profit
