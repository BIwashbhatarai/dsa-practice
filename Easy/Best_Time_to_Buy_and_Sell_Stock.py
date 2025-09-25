class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for curr_price in prices:
            if curr_price < min_price:
                min_price = curr_price
            profit = curr_price - min_price
                
            if profit > max_profit:
                max_profit = profit
        return max_profit
obj = Solution()
print(obj.maxProfit( [7,6,4,3,1]))