class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: (x[0], -x[1]))
        i = 1
        while i < len(meetings):
            if meetings[i-1][1] >= meetings[i][0]:
                if meetings[i][1] > meetings[i-1][1]:
                    meetings[i-1][1] = meetings[i][1]
                meetings.pop(i)
            else:
                i += 1
        for start, end in meetings:
            days -= end - start + 1
        return days
        