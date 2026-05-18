class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        l,r,ans = 0,0,0
        n = len(s)
        while r<n:
            while s[r] in st:
                st.remove(s[l])
                l+=1
            st.add(s[r])
            
            ans = max(ans,r-l+1)
            r+=1
        return ans
            
                



            