class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = dict()
        for index, n in enumerate(nums):
            if n in last_seen.keys():
                if index - last_seen[n] <= k:
                    return True
                else:
                    last_seen[n] = index
            else:
                last_seen[n] = index
        return False