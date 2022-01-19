
# BFS + DFS in python

### BFS (Breadth First Search)
+ Queue : FIFO
+ Python BFS Code
```
from collections import deque
   
def bfs(graph, start, visited):
    queue = deque([start]) 
    visited[start] = True
    while queue:
       v = queue.popleft()
       for i in graph[v]:
           if not visited[i]:
               queue.append(i)
               visited[i] = True
```

### DFS (Depth First Search)
+ Stack : LIFO
+ Python DFS Code
```
def dfs(graph, v, visited):
    visited[v] = True 
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
```

