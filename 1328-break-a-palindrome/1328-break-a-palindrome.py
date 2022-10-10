class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        og = list(palindrome)
        palindrome = list(palindrome)
        for c in range(int(len(palindrome)/2)):
            if palindrome[c] > 'a':
                palindrome[c] = 'a'
                break
            else:
                pass
        if palindrome == og:
            for c in range(int(len(palindrome))-1, -1, -1):
                if palindrome[c] < 'z':
                    palindrome[c] = chr(ord(palindrome[c]) + 1)
                    break
                else:
                    pass
        if palindrome == og:
            return ''
        return ''.join(palindrome)