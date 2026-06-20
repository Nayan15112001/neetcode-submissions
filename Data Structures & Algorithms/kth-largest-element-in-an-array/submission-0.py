import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        print(nums)
        n = len(nums)
        for i in range(n-k+1):
            ans = heapq.heappop(nums)

        return ans