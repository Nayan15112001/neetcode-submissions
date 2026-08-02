class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_min = nums[0]
        prev_max = nums[0]
        ans = -1*float('inf')
        if len(nums) == 1:
            return nums[0]
        for i in range(1,len(nums)):
            curr_max = max(nums[i],nums[i]*prev_max,nums[i]*prev_min)
            curr_min = min(nums[i],nums[i]*prev_max,nums[i]*prev_min)
            prev_max = curr_max
            prev_min = curr_min
            ans = max(ans,prev_max)
        return ans