class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            hmap[nums[i]] = i

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hmap and hmap[difference]!=i:
                return [i,hmap[difference]]