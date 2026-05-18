class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        ans = 0
        s = set(nums)
        for i,val in enumerate(s):
            if val-1 not in s:
                temp = val
                count = 0
                while (temp+count) in s:
                    count+=1
                ans = max(count,ans)
        return ans