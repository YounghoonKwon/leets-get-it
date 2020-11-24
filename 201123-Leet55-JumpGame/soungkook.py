class Solution:
    def canJump(self, nums):
        bestJumper,i = nums[0],0
        # if bestJump is lesser than index, you couldn't make it the index already
        while i<len(nums) and i<= bestJumper: 
            # you are succesfully on that index
            print('i+nums[i]', i+nums[i])
            
            #update bestJump with maxJump + index
            bestJumper,i = max(bestJumper,i+nums[i]), i+1
            print('bestJumper', bestJumper, i)
        print('best', bestJumper)
        return bestJumper>=len(nums)-1
