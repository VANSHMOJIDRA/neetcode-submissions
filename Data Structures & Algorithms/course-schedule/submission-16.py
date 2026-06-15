class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        for c,preq in prerequisites:
            graph[c].append(preq)
        current = set()
        complete = set()
        def dfs(node):
            if node in current:
                return False
            if node in complete:
                return True
            current.add(node)
            for n in graph[node]:
                if not dfs(n):
                    return False
            current.remove(node)
            complete.add(node)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        