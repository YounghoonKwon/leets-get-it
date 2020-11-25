class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        
        up=down=1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                down = up + 1
            elif nums[i] < nums[i+1]:
                up = down +1
        return max(up, down)
