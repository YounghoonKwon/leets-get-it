class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = collections.Counter(tasks)
        vals = sorted(c.values(), reverse = True)
        
        max_val = vals[0] - 1
        max_idle_slots = max_val * n
        vals.pop(0)
        
        for val in vals:
            max_idle_slots -= min(max_val, val)
        return max_idle_slots + len(tasks) if max_idle_slots > 0 else len(tasks)
