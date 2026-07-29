class Solution:
    def rob(self, nums: List[int]) -> int:
        memo1,memo2 = {},{}
        n = len(nums)
        if n == 1:
            return nums[0]
        def rec1(x):
            if x >= n-1:
                return 0

            if x in memo1:
                return memo1[x]
            
            curr = nums[x] +rec1(x+2)
            skip = rec1(x+1)
            memo1[x] = max(curr,skip)

            return memo1[x]
        def rec2(x):
            if x >= n:
                return 0

            if x in memo2:
                return memo2[x]
            
            curr = nums[x] +rec2(x+2)
            skip = rec2(x+1)
            memo2[x] = max(curr,skip)

            return memo2[x]

        return max(rec1(0),rec2(1))