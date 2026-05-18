class Solution:
    def trap(self, height: List[int]) -> int:
        l =0
        r =len(height) - 1 
        maxl = 0
        maxr = 0
        i = 0
        ans = 0
        while l<r:
            maxl = max(maxl,height[l])
            maxr = max(maxr,height[r])

            if maxl<=maxr:
                ans += maxl-height[l]
                l+=1
            elif maxr<maxl:
                ans += maxr-height[r]
                r-=1
            
        return ans

        
    
    # r = 1
    # sum = 2-0 = 2
    # r = 2
    # arr = [2]
    # sum = 0
    # l = 2
    # r = 3
    # sum = 3-2

