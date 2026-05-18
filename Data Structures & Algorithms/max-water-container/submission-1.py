class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        product = 0
        while l<r:
            temp = min(heights[l],heights[r])*(r-l)
            product = max(temp,product)
            if heights[l]>heights[r]:
                r-=1
            elif heights[r]>heights[l]:
                l+=1
            else:
                r-=1
                l+=1
        return product
    