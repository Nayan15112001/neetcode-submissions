class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {n:True}


        def dfs(i):
            if i in dp:
                return dp[i]
            
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    print('hi')
                    dp[i] = dfs(i+len(word))
                    print(dp[i])
                    if dp[i]:
                        break
            if i not in dp:
                return False
            return dp[i]


        return dfs(0)