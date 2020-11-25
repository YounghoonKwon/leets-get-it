class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxVal = max(counter.values())
        rest = len([v for v in counter.values() if v == maxVal])
        result = (n + 1) * (maxVal - 1) + rest
        
        return max(len(tasks), result)
