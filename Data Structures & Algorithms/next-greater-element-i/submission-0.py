class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        ans = [-1]* n1

        for i in range(n1):
            for j in range(n2):
                if nums2[j] == nums1[i]:
                    k = j
                    break
            for l in range(k,n2):
                print(nums2[l])
                if nums2[l]>nums1[i]:
                    ans[i] = nums2[l]
                    print(ans)
                    break
                
        return ans

