class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        for i, t in enumerate(timeSeries[:-1:]):
            if timeSeries[i+1] - t < duration:
                total += timeSeries[i+1] - t
            else:
                total += duration
        return total + duration