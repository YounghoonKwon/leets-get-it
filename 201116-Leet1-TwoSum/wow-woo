class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # One-pass hash table
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[target - nums[i]] = i
                # using needed value as a key of table and current index as value


# print(twoSum([3, 2, 4], 6))
#               3  4  2
#               0  1  2
