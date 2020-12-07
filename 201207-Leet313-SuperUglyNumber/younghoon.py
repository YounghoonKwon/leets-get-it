class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        pq = [1]
        visited = set()
        nums = []
        for i in range(n):
            num = heapq.heappop(pq)
            nums.append(num)
            for prime in primes:
                new_num = num * prime
                if new_num in visited:
                    continue
                visited.add(new_num)
                heapq.heappush(pq, new_num)
        return nums[-1]
