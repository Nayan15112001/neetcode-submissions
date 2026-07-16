class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        visiting,done = set(),set()
        # def ismatch(word1,word2):
        #     match = 0
        #     for i in range(n):
        #         if word1[i] == word2[i]:
        #             match+=1
            
        #     return match == n-1
                

        # adj_list = {}
        # adj_list[beginWord]=[]
        # adj_list[endWord] = []

        # for word in wordList:
        #     adj_list[word] = []
        #     if ismatch(word,beginWord):
        #         adj_list[beginWord].append(word)
        
        # for word1 in wordList:
        #     for word2 in wordList:
        #         if word1 == word2:
        #             continue
        #         if ismatch(word1,word2):
        #             adj_list[word1].append(word2)
                
        # print(adj_list)
        pattern_map = {}
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                if pattern not in pattern_map:
                    pattern_map[pattern]= [word]
                else:
                    pattern_map[pattern].append(word)
        print(pattern_map)


        q = deque()
        q.append(beginWord)
        count = 1
        found = False
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for i in range(len(word)):
                    pattern = word[:i]+"*"+word[i+1:]
                    for nei in pattern_map[pattern]:
                        if nei not in visiting:
                            visiting.add(nei)
                            q.append(nei)
    
            count+=1
                
        return 0


        