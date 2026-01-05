class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1 and bits[i+1] in (0, 1):
                i += 2
            else:
                i += 1
        return bool(len(bits) - i)