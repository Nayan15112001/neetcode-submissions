class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['#'] = {}
 
    def search(self, word: str) -> bool:
        d = self.trie
        
        def rec(start,d):
            #base condition
            if start>=len(word):
                if '#' in d:
                    return True
                else:
                    return False


            if word[start] == '.':
                for k,v in d.items():
                    if rec(start+1,v):
                        return True
                return False    
            else:
                if word[start] in d:
                    if rec(start+1,d[word[start]]):
                        return True
                    else:
                        return False
                else:
                    return False
        return(rec(0,d))
        
