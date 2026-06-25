from collections import deque

class Solution:
    def foreignDictionary(self,words:list[str]) -> str:
        all_letter = set()
        for w in words:
            for l in w:
                all_letter.add(l)
        
        graph = {l: set() for l in all_letter}
        in_degree = {l : 0 for l in all_letter}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            min_l = min(len(w1), len(w2))

            found_diff = False
            for j in range(min_l):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    found_diff= True
                    break
            if not found_diff and len(w1) > len(w2):
                return ""

        queue = deque([l for l in all_letter if in_degree[l] == 0])
        result = []

        while queue:
            curr = queue.popleft()
            result.append(curr)

            for ne in graph[curr]:
                in_degree[ne] -= 1
                if in_degree[ne] == 0:
                    queue.append(ne)
        
        if len(result) != len(all_letter):
            return ""
        
        return "".join(result)