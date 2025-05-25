class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        mid = False
        for i, word in enumerate(words):
            if word[::-1] in words[i+1:]:
                res += 4
            elif word[0] == word[1]:
                mid = True
        return res + mid * 2