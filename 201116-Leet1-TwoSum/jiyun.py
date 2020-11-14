class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            rest = target - n
            if not rest in d:
                d[n] = i
            else:
                return [d[rest], i]
