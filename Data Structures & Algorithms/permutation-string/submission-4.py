class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = {}
        r = 0
        count1 = Counter(s1)
        count2 = Counter(s2[:len(s1)])
        
        if count1 == count2:
            return True
        if len(s1)>len(s2):
            return False
        for i in range(len(s1),len(s2)):
            count2[s2[i]]+=1
            count2[s2[i-len(s1)]]-=1
            if count2[s2[i-len(s1)]] == 0:
                del(count2[s2[i-len(s1)]])
            if count1 == count2:
                return True
        return False