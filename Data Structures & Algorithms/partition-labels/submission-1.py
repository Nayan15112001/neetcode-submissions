class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        n = len(s)
        last_occurence = {}
        for i in range(n):
            last_occurence[s[i]] = i 
        max_,temp = 0,0
        for i in range(n):
            temp+=1
            max_ = max(max_,last_occurence[s[i]])
            if i == max_:
                ans.append(temp)
                temp = 0

        print(last_occurence)
        return ans

