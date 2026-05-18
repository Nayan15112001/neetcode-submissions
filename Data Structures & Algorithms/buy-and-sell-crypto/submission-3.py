class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0 
        r = 1
        ans = 0
        while r<n:
            if prices[l]<prices[r]:
                ans = max(ans,prices[r]-prices[l])
                r+=1
            else:
                l=r
                r+=1
        return ans