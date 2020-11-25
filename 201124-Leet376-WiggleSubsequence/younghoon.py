class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        
        stack=[nums[0]]
        is_negative = None

        for i in nums[1:]:
            if stack[-1]==i:
                continue
                
            if stack[-1] - i < 0:
                curr = True
            else:
                curr = False
                
            if is_negative == curr:
                stack.pop()
                
            is_negative=curr
            stack.append(i)
        return len(stack)
