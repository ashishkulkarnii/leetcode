class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        while len(people):
            i = 0
            j = len(people) - 1
            if people[j] == limit:
                people.pop(-1)
            elif len(people) >= 2 and people[i] + people[j] <= limit:
                people.pop(-1)
                people.pop(0)
            else:
                people.pop(-1)
            res += 1
        return res