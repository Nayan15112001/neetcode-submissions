class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        if nums[l]<=nums[r]:
            return nums[0]
        while l<r:
            m  = l +((r-l)//2)
            print(f'm:{m}')
            print(f'l:{l} r:{r}')
            if r == m or l == m:
                return min(nums[r],nums[l])
            elif nums[l]>nums[m] and nums[r]>nums[m]:
                r = m
            elif nums[l]>nums[m] and nums[r]<nums[m]:
                l = m
            elif nums[r]>nums[m] and nums[l]<nums[m]:
                r = m
            else:
                l = m
        