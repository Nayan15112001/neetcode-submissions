class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def compare(a,b):
            if a<b:
                return -1
            if a>b:
                return 1
            return 0
        
        l = 0
        ans = 1
        for r in range(1,len(arr)):
            curr_comp = compare(arr[r-1],arr[r])
            if curr_comp==0:
                l = r
            elif r>=2:
                prev_comp = compare(arr[r-2],arr[r-1])
                if prev_comp == curr_comp:
                    l = r-1
            ans = max(ans,r-l+1)
        
        return ans
                