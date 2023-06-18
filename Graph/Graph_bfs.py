graph = {
    'A' : ['B','C','E'],
    'B' : ['A','C','D'],
    'C' : ['B'],
    'D' : ['A','B'],
    'E' : ['A']
}
from collections import deque
def bfs(graph, start_visited):
    visited = [start_visited]
    q = deque(start_visited)
    while q:
        current = q.popleft()
        for i in graph[current]:
            if i not in visited:
                visited.append(i)
                q.append(i)
    return visited
bfs(graph, 'A')