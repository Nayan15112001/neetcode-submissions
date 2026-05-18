class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = []
        print(count.most_common(k))
        for i in count.most_common(k):
            ans.append(i[0])
        return ans
