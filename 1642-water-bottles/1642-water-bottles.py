class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk = 0
        empty = 0
        while numBottles:
            drunk += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty %= numExchange
        return drunk