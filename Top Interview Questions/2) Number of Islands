# BFS Solution

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
             return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    queue = collections.deque()
                    queue.append((i, j))
                    grid[i][j] = '0'
                    while queue:
                        x, y = queue.popleft()
                        directions = [(0,1), (0,-1), (-1,0), (1,0)]
                        for d in directions:
                            xx, yy = x+d[0], y+d[1]
                            if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == '1':
                                queue.append((xx, yy))
                                grid[xx][yy] = '0'
                    count += 1            
        return count
        
        
        
# DFS Solution
