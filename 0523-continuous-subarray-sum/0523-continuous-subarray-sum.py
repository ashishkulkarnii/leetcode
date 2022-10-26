class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map = {0: 0}
        s = 0
        for i, n in enumerate(nums):
            s += n
            if s % k not in hash_map.keys():
                hash_map[s % k] = i + 1
            elif hash_map[s % k] < i:
                return True
        return False