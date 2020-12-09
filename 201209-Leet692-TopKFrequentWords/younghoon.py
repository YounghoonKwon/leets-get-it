class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        worddict = {}
        for word in words:
            worddict[word] = worddict.get(word, 0) + 1
        worddict = sorted(worddict.items(), key=lambda x: (-x[1], x[0]))
        output = []
        for i in range(k):
            output.append(worddict[i][0])
        return output
            
