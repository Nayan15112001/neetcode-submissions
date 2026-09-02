class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        dist = 0
        if n == 1:
            return 0
        for i in range(n):
            if nums[i]+i >=n-1:
                jumps+=1
                return jumps
            elif i>=dist:
                jumps+=1
                dist = nums[i]+i
            

        
            

