from collections import defaultdict
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = defaultdict(list)
        for i, v in enumerate(s):
            dic[v].append(i)

        def recur(dic: dict, idx: int) -> str:
            if not dic: return ''
            for i in sorted(dic.keys()):
                for cand in dic[i]:
                    if cand > idx:
                        first = cand
                        break
                for j in dic.keys():
                    if i == j: continue
                    if dic[j][-1] < first:
                        break
                else:
                    chosen = i
                    break
            del dic[chosen]
            return chosen + recur(dic, first)
        
        return recur(dic, -1)