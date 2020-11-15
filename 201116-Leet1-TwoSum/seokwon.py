class Solution:
    def twoSum(self, nums, target):
        idxList = []
        for idx, num in enumerate(nums):
            idxList.append((num,idx))
        i = 0
        j = len(nums)-1
        idxList.sort(key=lambda x: x[0])
        print(idxList)
        while i<j:
            result = idxList[i][0]+idxList[j][0]
            if result < target:
                i +=1
            elif result > target:
                j -=1
            else:
                return [idxList[i][1],idxList[j][1]]
