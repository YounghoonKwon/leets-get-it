class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        size = len(nums)
        if size == 1:
            return False
        
        i = 1
        while i < size:
            diff = nums[i] -  nums[i-1]
            j=i+1
            p=1
            while j<size and diff == nums[j] - nums[j-1]:
                j+=1
                p+=1
            if j-i+1<3 and j-i+1 !=1:
                print('i', i , 'j',j)
                return False
            i=j+1
            
        return True
