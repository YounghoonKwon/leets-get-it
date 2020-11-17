class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in d:
                d[num] = i
            else:
                return [d[n], i]