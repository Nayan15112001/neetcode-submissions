class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        
        for s in strs:
            count = [0]*26
            #calculate the key 
            for c in s:
                count[ord(c)-ord('a')]+=1
            hmap[tuple(count)].append(s)
            print(hmap)
        return list(hmap.values())
            