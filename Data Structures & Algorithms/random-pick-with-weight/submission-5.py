class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        n = len(w)
        self.sum = 0
        for num in w:
            self.sum+=num
            self.prefix.append(self.sum)
        
    



    def pickIndex(self) -> int:
        if len(self.prefix)<=1:
            return 0
        target = random.randint(1,self.sum)
        l = 0
        r = len(self.prefix)-1
        while l<=r:
            mid = l + (r-l)//2

            if self.prefix[mid] >= target:
                ans = mid
                r = mid-1
            
            else:
                l = mid+1
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()