class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        ans = []
        for s in strs:
            temp = "".join(sorted(s))
            hmap[temp].append(s)
            # print(hmap)
        return list(hmap.values())