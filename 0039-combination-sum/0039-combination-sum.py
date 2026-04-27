class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def rec(chose=[], i=0):
            if sum(chose) == target: res.append(chose)
            elif sum(chose) > target or i == len(candidates): return
            else:
                rec(chose+[candidates[i]], i)
                rec(chose, i + 1)
        rec()
        return res