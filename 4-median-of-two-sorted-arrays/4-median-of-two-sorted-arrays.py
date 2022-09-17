class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        ltot = len(nums1) + len(nums2)
        isOdd = (ltot) % 2
        while(len(nums1) and len(nums2)):
            if nums1[0] > nums2[0]:
                arr.append(nums2.pop(0))
            else:
                arr.append(nums1.pop(0))
        while (len(nums1) or len(nums2)) and len(arr) <= ltot/2:
            if len(nums1):
                arr.append(nums1.pop(0))
            if len(nums2):
                arr.append(nums2.pop(0))
        if isOdd: return arr[int(ltot/2)]
        else: return (arr[int(ltot/2)-1] + arr[int(ltot/2)]) / 2