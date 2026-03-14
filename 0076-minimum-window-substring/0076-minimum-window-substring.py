class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_freq = collections.Counter(s[0])
        target_freq = collections.Counter(t)
        def check():
            for char, freq in target_freq.items():
                if freq > window_freq[char]:
                    return False
            return True
        i, j = 0, 0
        res = ""
        res_len = len(s) + 1
        while i <= j < len(s):
            if check():
                if j + 1 - i < res_len:
                    res = s[i:j+1]
                    res_len = j + 1 - i
                window_freq[s[i]] -= 1
                i += 1
            else:
                j += 1
                if j < len(s): window_freq[s[j]] += 1
        return res