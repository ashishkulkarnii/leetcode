class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def is_peak(i):
            if i > 0 and nums[i] < nums[i-1]:
                return False
            if i + 1 < len(nums) and nums[i] < nums[i+1]:
                return False
            return True
        def slope(i):
            prev = nums[i-1] if i > 0 else -float('inf')
            nex = nums[i+1] if i < len(nums) - 1 else -float('inf')
            if prev < nums[i] < nex:
                return 1
            elif prev > nums[i] > nex:
                return -1
            else:
                return 0
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if is_peak(mid):
                return mid
            elif slope(mid) > 0:
                low = mid + 1
            else:
                high = mid - 1
