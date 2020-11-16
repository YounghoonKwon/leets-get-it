class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i in range(len(nums)):
            need = target - nums[i]
            if need in dic:
                return [dic[need], i]
            dic[nums[i]] = i