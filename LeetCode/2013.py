class DetectSquares:

    def __init__(self):
        self.points: List[Tuple[int, int]] = []
        self.rows: List[int] = [[]] * 1001
        self.cols: List[int] = [[]] * 1001
        

    def add(self, point: List[int]) -> None:
        col = point[0]
        row = point[1]
        self.points.append((row, col))
        i = len(self.points)-1
        self.rows[row].append(i)
        self.cols[col].append(i)

    def count(self, point: List[int]) -> int:
        if len(self.points) < 3:
            return 0

        print(self.points)
        ans = 0

        self.points.append((point[1], point[0]))
        
        def bt(combo: List[int]):
            if len(combo) == 4:
                print(combo)
                nonlocal ans
                ans += 1
                return
            
            curr = self.points[combo[-1]]

            if len(combo) == 1:
                print("searching for second point at row", self.rows[curr[0]])
                for second in self.rows[curr[0]]:
                    combo.append(second)
                    bt(combo)
                    combo.pop()
            elif len(combo) == 2:
                print("searching for third point at col", self.cols[curr[1]])
                for third in self.cols[curr[1]]:
                    if third not in combo:
                        combo.append(third)
                        bt(combo)
                        combo.pop()
            else:
                for fourth in self.rows[curr[0]]:
                    if self.points[fourth][1] == self.points[combo[0]][1] and fourth not in combo:
                        combo.append(fourth)
                        bt(combo)
                        combo.pop()
        
        bt([len(self.points)-1])

        self.points.pop()
        return ans
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)