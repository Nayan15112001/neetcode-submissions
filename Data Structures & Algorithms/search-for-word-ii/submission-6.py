class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            d = trie
            for c in word:
                if c not in d:
                    d[c] = {}
                d = d[c]
        
            d['#'] = word

        m = len(board)
        n = len(board[0])
        path = set()
        self.res = []
        d = trie
        def backtrack(r,c,d):
            #base condition
            if r<0 or c<0 or r>=m or c>=n or (r,c) in path or board[r][c] not in d:
                return 

            d = d[board[r][c]]

            if '#' in d:
                self.res.append(d['#'])
                d.pop('#')

            path.add((r,c))
            backtrack(r+1,c,d)
            backtrack(r-1,c,d)
            backtrack(r,c+1,d)
            backtrack(r,c-1,d)
            path.remove((r,c))

        
        for i in range(m):
            for j in range(n):
                backtrack(i,j,d)
        
        return self.res

        