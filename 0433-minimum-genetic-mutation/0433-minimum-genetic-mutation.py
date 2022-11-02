class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = [[start, 0]]
        hm = {start}
        while q:
            node, steps = q.pop(0)
            if node == end:
                return steps
            for c in "ACGT":
                for i in range(len(node)):
                    neighbor = node[:i] + c + node[i+1:]
                    if neighbor not in hm and neighbor in bank:
                        q.append([neighbor, steps + 1])
                        hm.add(neighbor)
        return -1