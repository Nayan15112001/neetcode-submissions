class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Prefix
        # [1,1,2,8]
        #suffix
        # [48,24,6,1]
        n = len(nums)
        ans = []
        product = 1
        prefix = [1]
        suffix = [1]
        for i in range(0,n-1):
            product *= nums[i]
            prefix.append(product)
        print(prefix)
        product = 1
        for i in range(n-1,0,-1):
            product *=nums[i]
            suffix.append(product)
        print(suffix)
        suffix = suffix[::-1]
        product = 1
        for i in range(0,n):
            product = suffix[i]*prefix[i]
            ans.append(product)
        return ans