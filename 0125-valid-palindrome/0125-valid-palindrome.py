class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        while i < n:
            if not s[i].isalnum():
                s = s[:i] + s[i+1:]
                n -= 1
            else:
                i += 1
        s = s.lower()
        return s == s[::-1]