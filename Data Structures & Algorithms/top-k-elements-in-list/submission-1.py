class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
       
        for num in nums:
            hmap[num] = hmap.get(num,0) + 1
        hmap = dict(sorted(hmap.items(), key = lambda x: x[1]))
        print(hmap)
        return list(hmap.keys())[-k:]