class Solution(object):
    def wiggleMaxLength(self, nums):
        if len(nums) < 2:
            return len(nums)
        ups = [1 for i in range(len(nums))]
        downs = [1 for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                ups[i] = downs[i - 1] + 1
                downs[i] = downs[i - 1]
            elif nums[i] < nums[i - 1]:
                downs[i] = ups[i - 1] + 1
                ups[i] = ups[i - 1]
            else:
                ups[i] = ups[i - 1]
                downs[i] = downs[i - 1]
                
        return max(ups[-1], downs[-1])
