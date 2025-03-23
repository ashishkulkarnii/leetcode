class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        while i < len(chars) - 1:
            n = 1
            while i + 1 < len(chars) and chars[i+1] == chars[i]:
                chars.pop(i)
                n += 1
            if n > 1:
                d = 0
                while n > 0:
                    chars.insert(i + 1, str(n % 10))
                    n //= 10
                    d += 1
                i += d
            i += 1
        return len(chars)
