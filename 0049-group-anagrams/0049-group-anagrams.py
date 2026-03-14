class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        def sort_str(s):
            return "".join(sorted(list(s)))
        for s in strs:
            groups[sort_str(s)].append(s)
        return list(groups.values())