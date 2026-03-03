class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        courses = [[] for i in range(n)]
        for prerequisite in prerequisites:
            courses[prerequisite[0]].append(prerequisite[1])

        states = [0] * n
        ans = []
        def dfs(node: int) -> bool:
            if states[node] == 1:
                return False
            if states[node] == 2:
                return True
            
            states[node] = 1
            for adj in courses[node]:
                if not dfs(adj):
                    return False
            
            ans.append(node)
            states[node] = 2
            return True

        for course in range(n):
            if not dfs(course):
                return []
        return ans
            