class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # A B A B A B A B A B
        #             l r
        l = 0
        r = 0
        ans = 0
        hmap = {}
        while r<len(s):
            hmap[s[r]] = hmap.get(s[r],0)+1
            max_val = max(hmap.values())
            while r-l+1-max_val >k:
                hmap[s[l]]-=1
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans
