class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashmap = dict()
        for n in nums:
            if n in hashmap.keys():
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        double = 1
        missing = 1
        for i in range(1, len(nums) + 1):
            if i not in hashmap.keys():
                missing  = i
            elif hashmap[i] == 2:
                double = i
        return [double, missing]