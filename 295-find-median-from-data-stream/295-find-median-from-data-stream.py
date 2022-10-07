import bisect

class MedianFinder:

    def __init__(self):
        self.arr = []
        self.median = 0

        
    def addNum(self, num: int) -> None:        
        l = len(self.arr)
        bisect.insort(self.arr, num)
        l += 1
        if l % 2 == 0:
            self.median = (self.arr[int(l/2)-1] + self.arr[int(l/2)]) / 2
        else:
            self.median = self.arr[int((l-1)/2)]
        

    def findMedian(self) -> float:
        return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()