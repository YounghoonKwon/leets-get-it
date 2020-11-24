class Solution(object):
    def removeKdigits(self, num, k):
        if not num or num == "0" or k >= len(num):
            return "0"
        if k == 0:
            return num
        
        curr = []
        i = 0
        while k > 0 and i < len(num):
            if curr:
                while curr and k > 0 and curr[-1] > num[i]:
                    curr.pop()
                    k -= 1
            curr.append(num[i])
            i += 1
        if k > 0:
            curr = curr[:-k]
        
        if not ''.join(curr) + num[i:]:
            return '0'
        return str(int(''.join(curr) + num[i:]))
