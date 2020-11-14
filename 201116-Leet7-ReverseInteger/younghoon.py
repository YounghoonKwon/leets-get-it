class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False
        overflow = 2**31
        if x < 0:
            is_neg = True
        
        x = abs(x)
        x = int(str(x)[::-1])
        
        if x < overflow:
            if is_neg ==True:
                x = -x
            return x
        return 0
