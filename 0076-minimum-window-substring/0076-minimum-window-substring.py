class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.defaultdict(int)
        t_counter = collections.Counter(t)
        i, j = 0, 0
        def check_counter(counter):
            for c in t:
                if counter[c] < t_counter[c]:
                    return False
            return True
        res = ""
        res_len = len(s) + 1
        while j < len(s):
            counter[s[j]] += 1
            if check_counter(counter):
                while check_counter(counter):
                    counter[s[i]] -= 1
                    i += 1
                if j - i + 1 <= res_len:
                    res = s[i-1:j+1]
                    res_len = j - i + 1
                # res = min(res, s[i-1:j+1], key=len)
            j += 1
        return res