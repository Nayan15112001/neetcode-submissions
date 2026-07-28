class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans  = ''
        temp = ''
        for i in range(len(s)):
            for j in range(i,len(s)):
                temp = s[i:j+1]
                if len(temp)<len(ans):
                    continue
                elif temp == temp[::-1]:
                    if len(temp)>len(ans):
                        ans = temp

        return ans
            