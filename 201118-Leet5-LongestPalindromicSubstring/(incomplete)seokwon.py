class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        if len(s) <=1 or s==s[::-1]:
            return s
        else:
            for i in range(len(s)):
                print(i)
                if len(s)%2 ==0:
                    result = max(result, findSubstring(s,i,i+1), key=len)

                else:
                    result = max(result, findSubstring(s,i,i), key=len)
            return result

def findSubstring(string, left, right):
    while left >0 and right < len(string)-1 and string[left-1] == string[right+1]:
        left -=1
        right +=1
    print(left,right)
    print(string[left:right+1])
    print()
    return string[left:right+1]
