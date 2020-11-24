class Solution(object):
    def reconstructQueue(self, people):
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        queue = []
        
        for i in people:
            k = i[1]
            queue.insert(k, i)
        return queue
