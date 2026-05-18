class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
  
        l,r,ans = 0,0,0
        n = len(s)
        while r<n:
            print(s[l:r])
            if s[r] not in s[l:r]:
                ans = max(ans,r-l+1)
                r+=1
            else:
                l+=1
                
        return ans



            