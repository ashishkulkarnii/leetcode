class Solution:
    def minInteger(self, num: str, k: int) -> str:
        if k == 0:
            return num
        N = len(num)
        if N * (N - 1) // 2 <= k:
            return ''.join(sorted(list(num)))
        for i in range(10):
            index = num.find(str(i))
            if 0 <= index <= k:
                return str(num[index]) + self.minInteger(''.join(num[:index] + num[index+1:]), k - index)
