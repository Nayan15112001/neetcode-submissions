class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setc = set(nums)
        print(setc)
        ans = 0
        
        for i in range(len(nums)):
            j=i
           
            if nums[i]-1 not in setc:
                
                temp = 0
                while (nums[i]+temp) in setc:
                    
                    temp += 1
                    
                ans = max(temp,ans)
                    
        return ans

