class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        high = n - 1
        low = 0
        while low <= high:
            mid = (low + high) // 2
            if nums[low] > nums[mid]:
                if nums[mid-1] < nums[mid]:
                    high = mid - 1
                else:
                    rot = mid
                    break
            elif nums[mid] > nums[high]:
                if nums[mid+1] > nums[mid]:
                    low = mid + 1
                else:
                    rot = mid + 1
                    break
            else:
                rot = low
                break
        bs = lambda x: (x + rot) % n
        high = n - 1
        low = 0
        while low <= high:
            mid = (low + high) // 2
            if nums[bs(mid)] == target:
                return bs(mid)
            elif nums[bs(mid)] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1