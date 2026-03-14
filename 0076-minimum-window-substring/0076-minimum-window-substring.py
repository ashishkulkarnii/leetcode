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
        res = s
        while j < len(s):
            counter[s[j]] += 1
            if check_counter(counter):
                while check_counter(counter):
                    counter[s[i]] -= 1
                    i += 1
                res = min(res, s[i-1:j+1], key=len)
            j += 1
        return res if (res != s or check_counter(collections.Counter(res))) else ""