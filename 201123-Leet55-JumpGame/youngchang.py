class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        bools = [True] + [False]*(length-1)
        reach = 0
        for i in range(length):
            if bools[i] and i+nums[i]>reach:
                for idx in range(reach+1, i+nums[i]+1):
                    try:
                        bools[idx] = True
                    except:
                        break
                reach = i+nums[i]
        return bools[-1]