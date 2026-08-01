class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prev_min = nums[0]
        prev_max = nums[0]
        ans = nums[0]
        for i in range(1,n):
            a = nums[i]
            b = nums[i] * prev_min
            c = nums[i] * prev_max
            curr_max = max(a,b,c)
            curr_min = min(a,b,c)
            ans = max(ans,curr_max)
            prev_max = curr_max
            prev_min = curr_min
            
        return ans