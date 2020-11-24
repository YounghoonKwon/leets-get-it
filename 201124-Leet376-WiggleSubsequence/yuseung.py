class Solution:
	def wiggleMaxLength(self, nums: List[int]) -> int:
		if len(nums) <= 1:
			return len(nums)
		if len(set(nums)) == 1:
			return 1
		ref = nums[0]
		status = 0        
		res = 1
		for i in nums[1:]:
			if i > nums[0]:
				status = 0
				break
			elif i < nums[0]:
				status = 1
				break
		for i in nums[1:]:
			if status == 0:
				if i > ref:
					ref = i
				elif i < ref:
					status = 1
					ref = i
					res += 1
			else:
				if i < ref:
					ref = i
				elif i > ref:
					status = 0
					ref = i
					res += 1
		return res + 1
