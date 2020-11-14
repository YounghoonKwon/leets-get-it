class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = list(enumerate(nums))
        arr.sort(key=lambda x: x[1])
        l = 0
        r = len(nums)-1
        while l<=r:
            if arr[l][1] + arr[r][1] == target:
                return [arr[l][0], arr[r][0]]
            if arr[l][1] + arr[r][1] < target:
                l += 1
                continue
            if arr[l][1] + arr[r][1] > target:
                r -= 1
                continue
