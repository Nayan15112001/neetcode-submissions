class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list= {}
        for word in words:
            for char in word:
                adj_list[char] = set()

        for i in range(len(words)-1):
            word1,word2 = words[i],words[i+1]
            
            l1 = len(word1)
            l2 = len(word2)
            
            if l1>l2 and word1[:l2] == word2[:l2]:
                return ""
            min_l = min(l1,l2)
            j = 0
            while j<min_l:
                if word1[j] != word2[j]:
                    adj_list[word1[j]].add(word2[j])
                    break
                j+=1
        print(adj_list)
        
        visited =set()
        done = set()
        l=[]
        def dfs(k):
            if k in visited:
                return False
            if k in done:
                return True
            visited.add(k)
            for nei in adj_list[k]:
                if not dfs(nei):
                    return False
            visited.remove(k)
            done.add(k)
            l.append(k)
            return True
        for k,v in adj_list.items():
            # print(f'k:{k}')
            if not dfs(k):
                return ""
        


        return "".join(reversed(l))