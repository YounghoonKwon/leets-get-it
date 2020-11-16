class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        temp, y = x, 0
        while temp:
            y = y*10 + temp%10
            temp //= 10
        return x == y
