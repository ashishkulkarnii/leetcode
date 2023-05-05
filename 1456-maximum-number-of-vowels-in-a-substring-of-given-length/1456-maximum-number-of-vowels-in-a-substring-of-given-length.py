class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        res = vow_count = sum(map(s[:k].count, vowels))
        i = 1
        while i + k <= len(s):
            if s[i-1] in vowels:
                vow_count -= 1
            if s[i+k-1] in vowels:
                vow_count += 1
            res = max(res, vow_count)
            i += 1
        return res
