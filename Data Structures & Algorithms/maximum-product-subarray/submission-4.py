class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = [0]*n
        min_dp = [0]*n
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        ans = nums[0]
        for i in range(1,n):
            a = nums[i]
            b = nums[i] * min_dp[i-1]
            c = nums[i] * max_dp[i-1]

            max_dp[i] = max(a,b,c)
            min_dp[i] = min(a,b,c)
            ans = max(ans,max_dp[i])
            

        return ans