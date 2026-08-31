class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_max = nums[0]
        ans = nums[0]
        n = len(nums)

        for i in range(1,n):
            curr_max = max(nums[i],nums[i]+prev_max)
            prev_max = curr_max
            ans = max(ans,prev_max)
        
        return ans