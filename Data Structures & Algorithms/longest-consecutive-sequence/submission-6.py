class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        ans = 1
        s = set(nums)
        for i,val in enumerate(s):
            if val-1 not in s:
                temp = val
                count = 1
                while temp in s:
                    if temp+1 in s:
                        count+=1
                        temp+=1
                        ans = max(count,ans)
                    else:
                        break
                     
        return ans