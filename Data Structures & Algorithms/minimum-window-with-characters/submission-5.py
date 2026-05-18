class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hmap1 = {}
        hmap2 = {}
        l,r = 0,0
        res = [-1,-1]
        for i in range(len(t)):
            hmap1[t[i]] = hmap1.get(t[i],0)+1
        need = len(hmap1)
        have = 0
        reslen = float('infinity')
        for r in range(len(s)):
            
            hmap2[s[r]] = hmap2.get(s[r],0)+1
            print(hmap2)
            print(hmap1)
            if s[r] in hmap1 and hmap2[s[r]]==hmap1[s[r]]:
                have+=1
            print(f'have:{have} and need:{need}')
            while have == need:
                
                if r-l+1 <reslen:
                    res = [l,r]

                    reslen = r-l+1
                    
                hmap2[s[l]]-=1
                if s[l] in hmap1 and hmap2[s[l]] < hmap1[s[l]]:
                    have-=1
                l+=1
        l,r  = res
        print(res)
        return s[l:r+1]