class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i :[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(node):
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n)
        count = 0
        for e in range(n):
            if e not in visited:
                dfs(e)
                count += 1
        return count
                