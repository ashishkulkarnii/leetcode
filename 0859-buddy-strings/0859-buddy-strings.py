class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and ((s == goal and len(set(s)) < len(s)) or (len(l := [(x, y) for x, y in zip(s, goal) if x != y]) == 2 and l[0][0] == l[1][1] and l[0][1] == l[1][0]))