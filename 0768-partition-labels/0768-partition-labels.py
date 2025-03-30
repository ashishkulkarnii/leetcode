class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ranges = [[-1, -1] for _ in range(26)]
        for i, c in enumerate(s):
            if ranges[ord(c) - ord('a')][0] == -1:
                ranges[ord(c) - ord('a')][0] = i
            ranges[ord(c) - ord('a')][1] = i
        while [-1, -1] in ranges:
            ranges.remove([-1, -1])
        ranges.sort()
        start, end = ranges[0]
        partitions = []
        for i in range(1, len(ranges) + 1):
            if i == len(ranges):
                partitions.append(end - start + 1)
            elif ranges[i][0] > end:
                partitions.append(end - start + 1)
                start, end = ranges[i]
            elif ranges[i][0] <= end:
                if ranges[i][1] > end:
                    end = ranges[i][1]
        return partitions

