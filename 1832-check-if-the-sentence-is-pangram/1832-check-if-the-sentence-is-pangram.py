class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = [0] * 26
        for c in sentence:
            alpha[ord(c) - 97] = 1
        return not 0 in alpha