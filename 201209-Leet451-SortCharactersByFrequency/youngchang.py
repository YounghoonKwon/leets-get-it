class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        order = sorted(c.keys(), key = c.get, reverse = True)
        answer = ''
        for char in order:
            answer += char * c[char]
        return answer