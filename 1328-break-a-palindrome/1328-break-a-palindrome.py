class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        og = palindrome
        palindrome = list(palindrome)
        for c in range(int(len(palindrome)/2)):
            if ord(palindrome[c]) > 97:
                palindrome[c] = chr(97)
                break
            else:
                pass
        if ''.join(palindrome) == og:
            for c in range(int(len(palindrome))-1, -1, -1):
                if ord(palindrome[c]) < 122:
                    palindrome[c] = chr(ord(palindrome[c]) + 1)
                    break
                else:
                    pass
        if ''.join(palindrome) == og:
            return ""
        return ''.join(palindrome)