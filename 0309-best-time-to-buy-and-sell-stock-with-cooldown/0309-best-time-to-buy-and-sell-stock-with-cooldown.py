class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_cash, cash, hold = 0, 0, -math.inf
        for i in range(len(prices)):
            prev_cash, cash, hold = cash, max(cash, hold + prices[i]), max(hold, prev_cash - prices[i])
        return cash