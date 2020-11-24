from collections import defaultdict
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x : (-x[0], x[1]))
        answer = []
        for i in people:
            answer.insert(i[1], i)
        return answer