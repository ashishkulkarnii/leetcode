class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        new = list(palindrome)
        palindrome = list(palindrome)
        for c in range(int(len(palindrome)/2)):
            if palindrome[c] > 'a':
                new[c] = 'a'
                break
            else:
                pass
        if palindrome == new:
            for c in range(int(len(palindrome))-1, -1, -1):
                if palindrome[c] < 'z':
                    new[c] = chr(ord(palindrome[c]) + 1)
                    break
                else:
                    pass
        if new == palindrome:
            return ''
        return ''.join(new)