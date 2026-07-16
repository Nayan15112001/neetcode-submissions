class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        visiting,done = set(),set()
        def ismatch(word1,word2):
            match = 0
            for i in range(n):
                if word1[i] == word2[i]:
                    match+=1
            
            if match == n-1:
                return True

        adj_list = {}
        adj_list[beginWord]=[]
        adj_list[endWord] = []

        for word in wordList:
            adj_list[word] = []
            if ismatch(word,beginWord):
                adj_list[beginWord].append(word)
        
        for word1 in wordList:
            for word2 in wordList:
                if word1 == word2:
                    continue
                if ismatch(word1,word2):
                    adj_list[word1].append(word2)
                
        print(adj_list)


        q = deque()
        q.append(beginWord)
        count = 1
        found = False
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for nei in adj_list[word]:
                    if nei not in visiting:
                        visiting.add(nei)
                        q.append(nei)
                

            count+=1
                
        return 0


        