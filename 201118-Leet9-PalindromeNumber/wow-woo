class Solution:
    def isPalindrome(self, x: int) -> bool:
        origin = x
        back_x = 0
        
        while x > 0:
            back_x = (back_x * 10) + (x % 10)
            
            x = x // 10
        return origin == back_x
