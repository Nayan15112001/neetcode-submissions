class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        res = 0
        while l<r:
            m = l + ((r-l)//2)
            
            if nums[m] > nums[r]:
                l = m+1
            else:
                r= m
            
        print(nums[l])

        if nums[l]<=target<=nums[n-1]:
            i = l 
            j = n-1
        else:
            i = 0
            j = l-1
        while i<j:
            m = i + ((j-i)//2)
            print(f'i:{i} and j:{j} and m:{m}')
            if nums[m] == target:
                return m
            elif nums[m]<target:
                i = m + 1
            else:
                j = m 
        print(f'i:{i} and j:{j} ')
        if nums[i] == target:
            res = i
        elif nums[j] == target:
            res = j
        else:
            res = -1
        return res                