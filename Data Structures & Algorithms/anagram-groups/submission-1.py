class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        ans = []
        for s in strs:
            temp = "".join(sorted(s))
            hmap[temp].append(s)
            # print(hmap)
        for val,c in enumerate(hmap):
            ans.append(hmap[c])

        return ans