class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for point in points:
            dists.append((pow(point[0], 2)+pow(point[1], 2), point))
        dists.sort()
        return [pair[1] for pair in dists[:k]]
        