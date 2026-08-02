class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp= {n-1:nums[n-1]}

        def rec(x):
            
            if x>=n:
                return 0
            if x in dp:
                return dp[x]
            
            curr = nums[x]+rec(x+2)
            skip = rec(x+1)

            dp[x] = max(curr,skip)
            return dp[x]
        ans = rec(0)
        print(dp)
        return ans