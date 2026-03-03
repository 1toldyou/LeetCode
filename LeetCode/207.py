class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for i in range(numCourses)]
        for course, preReq in prerequisites:
            courses[course].append(preReq)
        # print(courses)

        checked = [False] * numCourses

        def dfs(course: int, visited: List[bool]) -> bool:
            # print("finding dependency of", course, visited)
            if checked[course]:
                return True
            if visited[course]:
                # print("cycle detected at", course)
                return False
            visited[course] = True
            for preReq in courses[course]:
                if not dfs(preReq, visited):
                    return False
            checked[course] = True
            return True

        for i in range(numCourses):
            if not dfs(i, [False] * numCourses):
                return False

        return True