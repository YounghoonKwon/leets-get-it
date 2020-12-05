class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        f = max(c.values())
        fcnt = 0
        for i in c:
            if c[i] == f:
                fcnt += 1
        return max((f - 1) * (n + 1) + fcnt, len(tasks))