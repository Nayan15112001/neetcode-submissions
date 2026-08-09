class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        ans = dp[0]
        for i in range (n-2,-1,-1):
            for j in range(i+1,n):
                if nums[i]>=nums[j]:
                    continue
                dp[i] = max(dp[i],1+dp[j])
            ans = max(dp[i],ans)
        return ans
            