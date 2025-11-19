class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        drunk = 0
        while numBottles:
            empty += numBottles
            drunk += numBottles
            numBottles = 0
            if empty >= numExchange:
                empty -= numExchange
                numBottles += 1
                numExchange += 1
        return drunk