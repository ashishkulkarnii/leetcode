class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = dict()
        for winner, loser in matches:
            if winner not in losses.keys():
                losses[winner] = 0
            if loser not in losses.keys():
                losses[loser] = 1
            else:
                losses[loser] += 1
        items = list(losses.items())
        items.sort(key=lambda x: x[0])
        lose0 = []
        lose1 = []
        for player, losses in items:
            if losses == 0:
                lose0.append(player)
            elif losses == 1:
                lose1.append(player)
        return [lose0, lose1]