class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        if s == rev:
            return s
        for i in range(1, len(s)):
            t1 = s[:-i:]
            t2 = t1[::-1]
            if t1 == t2:
                middle = t1
                back = s[-i::]
                front = back[::-1]
                return front+middle+back
            