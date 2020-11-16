class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sums = dict()
        for x in range(len(nums)):
            secondPair = target - nums[x]
            if secondPair not in two_sums:
                two_sums[nums[x]] = x
            else:
                return [two_sums[secondPair], x]