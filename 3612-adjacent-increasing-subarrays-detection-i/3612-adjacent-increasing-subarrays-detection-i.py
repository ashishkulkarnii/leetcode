class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        s = 0
        salen = [0 for _ in nums]
        for i in range(1, len(nums)):
            print(salen)
            if nums[i] <= nums[i-1]:
                salen[s] = i - s
                s = i
        salen[s] = len(nums) - s
        print(salen)
        for i, l in enumerate(salen):
            if l >= k * 2:
                return True
            elif l >= k and i + l < len(salen) and salen[i+l] >= k:
                return True
        return False