class StockSpanner:

    def __init__(self):
        self.prices = []
        self.stack = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        res = 1
        while len(self.stack) != 0 and self.stack[-1][0] <= price:
            res += self.stack[-1][1]
            self.stack.pop(-1)
        self.stack.append((price, res))
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)