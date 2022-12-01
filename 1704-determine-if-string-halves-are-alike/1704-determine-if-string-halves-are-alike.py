class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return sum([s[:len(s)//2].count(i) for i in "aeiouAEIOU"]) == sum([s[len(s)//2:].count(i) for i in "aeiouAEIOU"])