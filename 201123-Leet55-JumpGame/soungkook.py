class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # array of positive integers
        last = len(nums) -1
        
        return self.rcs( nums, 0)
        
    def rcs(self, nums, current):
        if current == len(nums)-1:
            return True
        
        max = nums[current]
        if max <= 0:
            return False
            
        for i in range(1, max+1):
            if i <= len(nums)-1:
                test = self.rcs(nums, current + i)
                if test:
                    return True
        return False
