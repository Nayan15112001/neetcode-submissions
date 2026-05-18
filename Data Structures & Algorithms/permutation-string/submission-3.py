class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = {}
        r = 0
        count1 = Counter(s1)
        print(count1)
        if len(s1)>len(s2):
            return False
        for i in range(0,len(s2)-len(s1)+1):
            print(Counter(s2[i:i+len(s1)]))
            if (count1) == (Counter(s2[i:i+len(s1)])):
                return True
        return False