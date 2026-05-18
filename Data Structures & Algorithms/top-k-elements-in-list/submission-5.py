class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n]  = count.get(n,0) + 1
        for n,c in count.items():
            freq[c].append(n)
        print(freq)
        for i in range(len(freq)-1,0,-1):
            if freq[i]!=[]:
                for j in range(len(freq[i])):
                    ans.append(freq[i][j])
                    if len(ans)==k:
                        return ans
        print(ans)

        return ans
