class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = len(heights)-1
        ans = 0

        while i < j:
            print(f'i : {i} and j:{j}')
            if heights[i]<heights[j]:
                product = heights[i]*(j-i)
                print(product)
                ans = max(product,ans)
                i+=1
            else:
                product = heights[j]*(j-i)
                print(product)
                ans = max(product,ans)
                j-=1
        return ans