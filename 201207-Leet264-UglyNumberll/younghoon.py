import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2,3,5]
        pq = [1]
        visited = set()
        nums = []
        for i in range(n):
            num = heapq.heappop(pq)
            nums.append(num)
            for factor in factors:
                new_num = num * factor
                if new_num in visited:
                    continue
                visited.add(new_num)
                heapq.heappush(pq, new_num)
        return nums[-1]
