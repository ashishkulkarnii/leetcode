class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = Counter()
        distinct = 0
        res = 0
        left = right = 0
        while right < len(fruits):
            if types[fruits[right]] == 0:
                distinct += 1
            types[fruits[right]] += 1
            while distinct > 2:
                types[fruits[left]] -= 1
                if types[fruits[left]] == 0:
                    distinct -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res