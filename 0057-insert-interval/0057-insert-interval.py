class Solution:
    def rec(self, intervals):
        for i, (b, e) in enumerate(intervals[:-1]):
            if e >= intervals[i+1][0]:
                intervals[i] = [b, max(intervals[i+1][1], e)]
                intervals.pop(i+1)
                return self.rec(intervals)
        return intervals
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        intervals = self.rec(intervals)
        return intervals