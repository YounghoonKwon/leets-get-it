class Solution(object):
    def canJump(self, nums):
     
        # far means the farthest index you can jump to
        far = nums[0]
        for i in range(len(nums)):
            if i > far:
                # it means we cannot reach i, break
                return False
            far = max(far, i + nums[i])
        return far >= len(nums)-1
