class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        n = len(s)
        count = Counter(s)
        temp = 0
        keys = set()
        for i in range(n):
            count[s[i]]-=1
            if count[s[i]]>0:
                temp += 1
                keys.add(s[i])
            else:
                flag = True
                for c in keys:
                    if count[c] > 0:
                        flag = False
                    
                temp+=1
                    
                if flag:
                    ans.append(temp)
                    temp = 0

        return ans

