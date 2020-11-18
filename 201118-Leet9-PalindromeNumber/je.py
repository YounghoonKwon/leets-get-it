class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        return temp == temp[::-1]
