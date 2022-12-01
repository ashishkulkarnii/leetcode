class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aieouAEIOU"
        v1, v2 = 0, 0
        for i, c in enumerate(s[:len(s)//2:]):
            if c in vowels:
                v1 += 1
        for i, c in enumerate(s[len(s)//2::]):
            if c in vowels:
                v2 += 1
        return v1 == v2