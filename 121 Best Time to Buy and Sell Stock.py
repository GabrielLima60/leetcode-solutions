'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0

        max_profit = 0

        min_price = prices[0] 
        
        for price in prices:

            if price < min_price:
                min_price = price

            max_profit = max(max_profit, price - min_price)

        return max(max_profit, 0)
