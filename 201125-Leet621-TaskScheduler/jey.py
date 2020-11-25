class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ct = Counter(tasks)
        maxx = max(ct.values())
        nmax = len([v for v in ct.values() if v == maxx])
        return max(len(tasks), (maxx - 1) * (n + 1) + nmax)
