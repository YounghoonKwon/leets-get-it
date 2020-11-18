class Solution(object):
    def intToRoman(self, num):
        roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        result = ''
        mul = 1
        
        while num > 0:
            cur = num % 10
            num //= 10
            if cur % 5 == 4:
                result = roman[mul] + roman[(cur + 1) * mul] + result
            elif cur >= 5:
                result = roman[5*mul] + roman[mul] * (cur - 5) + result
            else:
                result = roman[mul] * cur + result
            mul *= 10
        return result
