class Solution:
    symbols = {
        1000: 'M',
        500: 'D',
        100: 'C',
        50: 'L',
        10: 'X',
        5: 'V',
        1: 'I'
    }
    def intToRoman(self, num: int) -> str:
        res = ""
        for i in self.symbols:
            if int(num / i) == 0:
                pass
            elif int(str(num)[0]) == 4:
                if len(str(num)) == 1:
                    num = num - 4
                    res = res + "IV"
                elif len(str(num)) == 2:
                    num = num - 40
                    res = res + "XL"
                elif len(str(num)) == 3:
                    num = num - 400
                    res = res + "CD"
            elif int(str(num)[0]) == 9:
                if len(str(num)) == 1:
                    num = num - 9
                    res = res + "IX"
                if len(str(num)) == 2:
                    num = num - 90
                    res = res + "XC"
                elif len(str(num)) == 3:
                    num = num - 900
                    res = res + "CM"
            else:
                res = res + int(num / i) * self.symbols[i]
                num = num - int(num / i) * i
        return res
                