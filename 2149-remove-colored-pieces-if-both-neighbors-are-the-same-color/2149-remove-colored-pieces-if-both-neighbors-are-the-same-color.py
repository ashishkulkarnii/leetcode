class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        i = 1
        count = 0
        curr = None
        scores = {
            'A': 0,
            'B': 0,
        }
        while i < len(colors) - 1:
            if colors[i-1] == colors[i] == colors[i+1]:
                curr = colors[i]
                count += 1
                i += 1
            else:
                if curr:
                    scores[curr] += count
                count = 0
                curr = None
                i += 1
        if curr:
            scores[curr] += count
        return scores['A'] > scores['B']
