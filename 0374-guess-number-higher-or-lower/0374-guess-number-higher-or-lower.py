# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        b = 1
        e = n
        while guess(n) != 0:
            print(n)
            n = int((b + e) / 2)
            if guess(n) == -1:
                e = n - 1
            if guess(n) == 1:
                b = n + 1
        return n