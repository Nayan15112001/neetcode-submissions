class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie 
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['.'] = '.'
 
    def search(self, word: str) -> bool:
        d = self.trie
        def dfs(i,d):
            if i == len(word):
                return '.' in d
            if word[i] == '.':
                for key,val in d.items():
                    if key == '.':
                        continue
                    if dfs(i + 1, val):
                        return True
                return False
            elif word[i] not in d :
                return False
            
            return dfs(i+1,d[word[i]])
        
        return dfs(0, self.trie)
        
