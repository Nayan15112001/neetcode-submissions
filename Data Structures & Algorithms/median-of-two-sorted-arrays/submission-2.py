class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        res = 0
        x = (m+n+1)//2
        print(f"x:{x}")
        
        
        l = 0
        r = m
        if n<m:
            return self.findMedianSortedArrays(nums2,nums1)
        while l<=r:
            mid1 = (l+r)//2
            print(f"mid1:{mid1}")
            mid2 = x - mid1
            left1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
            right1 = nums1[mid1] if mid1 < m else float("inf")

            left2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
            right2 = nums2[mid2] if mid2 < n else float("inf")
            print(f"l:{l},r:{r},mid1:{mid1},mid2:{mid2},left1:{left1},left2:{left2},right1:{right1},right2:{right2}")
            if left1<=right2 and left2<=right1 :
                if (m+n) % 2 == 0:
                    res = (max(left1,left2)+min(right1,right2))/2
                else:
                    res = max(left1,left2)
                return res
            elif left1>right2:
                r = mid1-1 
            else:
                l = mid1+1

