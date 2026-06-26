class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        ans = []
        hmap = {}
        n2 = len(nums2)
        for num in nums2:
            while stk and num>stk[-1]:
                hmap[stk.pop()] = num
            stk.append(num)
            
        print(stk)
        for num in stk:
            hmap[num] = -1

        print(hmap)
        for num in nums1:
            ans.append(hmap[num])
        return ans

