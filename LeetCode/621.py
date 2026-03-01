class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        seq = []
        freqs = Counter(tasks)
        print(freqs)
        pq = [(-freq, task) for task, freq in freqs.items()]
        heapq.heapify(pq)
        print(pq)
        while pq:
            next_pq = []
            execCount = 0
            while pq:
                top = heapq.heappop(pq)
                seq.append(top[1])
                execCount += 1
                top = (top[0]+1, top[1])
                if top[0] < 0:
                    next_pq.append(top)
            heapq.heapify(next_pq)
            pq = next_pq
            if pq:
                for i in range(max(0, n + 1 - execCount)):
                    seq.append("idle")
        print(seq)

        return len(seq)
        