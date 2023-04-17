class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        result = []
        for kid in candies:
            if kid + extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)
        return result