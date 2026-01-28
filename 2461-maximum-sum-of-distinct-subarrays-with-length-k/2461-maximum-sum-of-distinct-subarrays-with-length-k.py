class Solution:
    def check_validity(self, c: dict) -> bool:
        for n, f in c.items():
            if f > 1:
                return False
        return True
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        c = collections.Counter(nums[:k])
        s = sum(n * f for n, f in c.items())
        m = s if self.check_validity(c) else 0
        valid = bool(m)
        i = 0
        while i < len(nums) - k:
            c[nums[i]] -= 1
            c[nums[i+k]] += 1
            s += nums[i+k] - nums[i]
            if c[nums[i]] > 1 or c[nums[i+k]] > 1:
                valid = False
            else:
                if valid:
                    m = max(m, s)
                elif self.check_validity(c):
                    m = max(m, s)
                    valid = True
            i += 1
        return m