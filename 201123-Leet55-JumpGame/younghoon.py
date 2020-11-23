class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxjump = 0
        for i, num in enumerate(nums):
            if maxjump < i: return False 
            maxjump = max(maxjump, i+num)
        return True
