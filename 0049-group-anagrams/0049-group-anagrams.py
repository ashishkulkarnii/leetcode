class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = dict()
        for s in strs:
            ss = "".join(sorted(list(s)))
            if ss in hm.keys():
                hm[ss].append(s)
            else:
                hm[ss] = [s]
        return list(hm.values())