class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = [[] for _ in range(numCourses)]
        num_prereqs = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            prereqs[a].append(b)
            num_prereqs[a] += 1
        def rec(remaining: list, completed: set):
            if not remaining:
                return True
            len_completed = len(completed)
            possible = [course for course in remaining if all(prereq in completed for prereq in prereqs[course])]
            for course in possible:
                completed.add(course)
                remaining.remove(course)
            if len(completed) == len_completed:
                return False
            return rec(remaining, completed)
        return rec(list(range(numCourses)), set())
