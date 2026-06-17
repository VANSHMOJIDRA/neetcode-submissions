class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        graph = {i :[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(node,parent):
            visited.add(node)
            for ne in graph[node]:
                if ne == parent:
                    continue
                if ne not in visited:
                    dfs(ne,node)
        dfs(0,-1)
        return len(visited) == n
    
        