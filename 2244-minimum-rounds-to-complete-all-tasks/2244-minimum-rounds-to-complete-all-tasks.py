class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = dict(Counter(tasks))
        print(c)
        res = 0
        for value in c.values():
            if value == 1:
                return -1
            else:
                res += value // 3 + ((value - 3 * int(value / 3)) == 1 or value - 3 * int(value / 3) == 2)
        return res