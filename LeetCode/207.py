class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for i in range(numCourses)]
        for course, preReq in prerequisites:
            courses[course].append(preReq)
        # print(courses)

        checked = [False] * numCourses

        for i, preReqs in enumerate(courses):
            print(i, preReqs)
            def dfs(course: int, visited: List[bool]) -> bool:
                # print("finding dependency of", course, visited)
                if checked[course]:
                    return True
                if len(courses[course]) == 0:
                    return True
                if visited[course]:
                    # print("cycle detected at", course)
                    return False
                visited[course] = True
                if len(courses[course]) == 1:
                    if not dfs(courses[course][0], visited):
                        return False
                else:
                    for preReq in courses[course]:
                        if not dfs(preReq, copy.deepcopy(visited)):
                            return False
                checked[course] = True
                return True
            if not dfs(i, [False] * numCourses):
                return False

        return True