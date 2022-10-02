def gcd(a, b):
    result = min(a, b)
    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
    return result

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for den in range(2, n + 1):
            for num in range(1, den):
                if gcd(num, den) == 1:
                    res.append(str(num) + '/' + str(den))
        return res