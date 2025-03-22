class Solution(object):
    def twoSum(self, nums, target):
        mappin = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in mappin:
                return [mappin[compliment], i]
            mappin[nums[i]] = i
        return []
        