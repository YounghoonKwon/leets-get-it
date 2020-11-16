class Solution(object):
    def isPalindrome(self, x):
        ## use str
        
        # return str(x) == str(x)[::-1]
        
        ## without converting integer to string
        
        if x < 0:
            return False
        
        temp = x
        reverse = 0
        
        while temp:
            reverse = reverse * 10 + temp % 10
            temp / /= 10

        return x == reverse
