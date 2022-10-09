class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return int(dividend / divisor) if (2147483647 >= int(dividend / divisor) and -2147483648 <= int(dividend / divisor)) else -2147483648 if int(dividend / divisor) < 0 else 2147483647