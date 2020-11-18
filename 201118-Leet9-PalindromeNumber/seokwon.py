class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = 0
        number = x
        if x <0:
            return False

        while number:
            result = result*10 + number%10
            number //= 10
        return x == result
