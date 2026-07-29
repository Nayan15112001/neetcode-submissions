class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def rec(x):
            if x >= n:
                return 0

            if x in memo:
                return memo[x]
            
            curr = nums[x] +rec(x+2)
            skip = rec(x+1)
            memo[x] = max(curr,skip)

            return memo[x]

        return rec(0)