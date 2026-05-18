class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        n = len(s)
        l,r = 0,0
        ans = 0
        count = 0
        
        while r<n:
            hmap[s[r]]= hmap.get(s[r],0)+1
            
            while (r-l+1)-max(hmap.values()) >k:
                print(hmap)
                hmap[s[l]]= hmap.get(s[l],0)-1
                if hmap[s[l]]==0:
                    hmap.pop(s[l])
                l+=1
                
                
            ans = max(ans,r-l+1)
            r+=1
        return ans
        
                
