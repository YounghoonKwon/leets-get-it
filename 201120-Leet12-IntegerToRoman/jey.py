class Solution:
    def intToRoman(self, num):
       
        stl = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        ret = ""

        for i, j in enumerate(nums):
            while num >= j:
                ret += stl[i]
                num -= j
            if num == 0:
                return ret
