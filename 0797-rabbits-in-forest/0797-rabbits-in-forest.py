class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        forest = [0] * (max(answers) + 1)
        for nr in answers:
            forest[nr] += 1
        return sum(math.ceil(x / (i + 1)) * (i + 1) for i, x in enumerate(forest))