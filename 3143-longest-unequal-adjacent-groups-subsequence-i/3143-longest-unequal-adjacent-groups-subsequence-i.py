class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        cg = not groups[0]
        res = []
        for word, group in zip(words, groups):
            if group != cg:
                cg = group
                res.append(word)
        return res