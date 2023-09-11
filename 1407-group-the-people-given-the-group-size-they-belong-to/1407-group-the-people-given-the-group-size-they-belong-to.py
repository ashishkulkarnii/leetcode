class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = collections.defaultdict(list)
        for person, groupSize in enumerate(groupSizes):
            groups[groupSize].append(person)
        res = []
        for groupSize, people in groups.items():
            while people:
                temp = people[:groupSize]
                people = people[groupSize:]
                res.append(temp)
        return res