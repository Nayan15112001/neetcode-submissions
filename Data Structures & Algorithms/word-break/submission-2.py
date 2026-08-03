class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {n:True}
        def words(i):
            if i in dp:
                return dp[i]
            # check for the substring if its in the wordDict
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    dp[i] = words(i+len(word))
                    if dp[i]:
                        break
                else:
                    dp[i] = False
            return dp[i]
        return words(0)
                
        