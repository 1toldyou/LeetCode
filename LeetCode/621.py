class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        seq = []
        freqs = Counter(tasks)
        pq = [(-freq, task) for task, freq in freqs.items()]
        heapq.heapify(pq)
        while pq:
            next_pq = []
            for i in range(n+1):
                if pq:
                    top = heapq.heappop(pq)
                    seq.append(top[1])
                    top = (top[0]+1, top[1])
                    if top[0] < 0:
                        next_pq.append(top)
                else:
                    seq.append("idle")
            next_pq += pq
            heapq.heapify(next_pq)
            pq = next_pq

        while seq and seq[-1] == "idle":
            seq.pop()

        return len(seq)
        