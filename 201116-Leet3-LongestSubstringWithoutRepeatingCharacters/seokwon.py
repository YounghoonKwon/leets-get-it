class Solution(object):
    def lengthOfLongestSubstring(self, s):
        result = ''
        maxLength = 0
        for idx, char in enumerate(s):
            if char not in result:
                result += char
                print('result: ', result)
            else:
                result = result[result.find(char)+1:]+char
            maxLength = max(maxLength, len(result))
        return maxLength
