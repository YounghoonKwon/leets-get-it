class Solution:
    def frequencySort(self, s: str) -> str:
        chardict = {}
        for char in s:
            chardict[char] = chardict.get(char, 0) + 1
        chardict = sorted(chardict.items(), key=lambda x: x[1], reverse=True)
        output = ""
        for char,freq in chardict:
            for _ in range(freq):
                output+=char
        return output
            
