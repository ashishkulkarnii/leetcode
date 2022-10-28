class Solution:
    def same(self, s1, s2):
        return sorted(s1) == sorted(s2)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = dict()
        for word in strs:
            sw = ''.join(sorted(list(word)))
            if sw not in hmap.keys():
                hmap[sw] = [word]
            else:
                hmap[sw].append(word)
        return hmap.values()