class Solution(object):
    def canJump(self, nums):
        end = len(nums) - 1
        for i in range(end - 1, -1, -1):
            if i + nums[i] >= end:
                end = i
        return end == 0
