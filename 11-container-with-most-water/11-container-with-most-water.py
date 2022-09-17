class Solution:
    def maxArea(self, height: List[int]) -> int:
        lvl = max(height)
        temp = []
        water = 0
        while lvl:
            for i in range(len(height) - 1):
                if height[i] >= lvl:
                    temp.append(i)
                    break
            for i in range(len(height) - 1, 0, -1):
                if height[i] >= lvl:
                    temp.append(i)
                    break
            if len(temp) > 1:
                if water < abs(temp[0] - temp[-1]) * lvl:
                    water = abs(temp[0] - temp[-1]) * lvl
            temp = []
            lvl -= 1
            if lvl * len(height) < water:
                break
        return water