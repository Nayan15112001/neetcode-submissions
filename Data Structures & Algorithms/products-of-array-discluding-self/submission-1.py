class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        ans = []
        prefix.append(1)
        suffix.append(1)
        for i in range(1,len(nums)):
            prefix.append(nums[i-1]*prefix[i-1])
        
        print(prefix)
        for i in range(len(nums),1,-1):
            suffix.append(nums[i-1]*suffix[len(nums)-i])
        print(suffix)

        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[len(nums)-i-1])
        return ans