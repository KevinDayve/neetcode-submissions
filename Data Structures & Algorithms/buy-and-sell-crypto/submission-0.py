class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_price = prices[0]
        for price in prices[1:]:
            if curr_price > price:
                curr_price = price
            profit = price - curr_price
            max_profit = max(max_profit, profit)
        return max_profit