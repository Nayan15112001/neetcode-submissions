class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        merged = [0,0,0]
        for i in range(n):
            if triplets[i][0]>target[0] or triplets[i][1]>target[1] or triplets[i][2]>target[2]:
                continue
            merged = [max(merged[0],triplets[i][0]),max(merged[1],triplets[i][1]),max(merged[2],triplets[i][2])]
            if merged == target or [triplets[i][0],triplets[i][1],triplets[i][2]] == target:
                return True
            
        
        return False
            
            
            