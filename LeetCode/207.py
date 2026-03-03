class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for i in range(numCourses)]
        for course, preReq in prerequisites:
            courses[course].append(preReq)
        print(courses)

        for i, preReqs in enumerate(courses):
            print(i, preReqs)
            for preReq in preReqs:
                visited = [False] * numCourses
                def dfs(course: int) -> bool:
                    print("finding dependency of", course)
                    if len(courses[course]) == 0:
                        return True
                    if visited[course]:
                        print("cycle detected at", course)
                        return False
                    visited[course] = True
                    for preReq in courses[course]:
                        if not dfs(preReq):
                            return False
                    return True
                print("starting at", preReq)
                if not dfs(preReq):
                    return False

        return True