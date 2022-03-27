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
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Step 1 : Check for an empty graph
        if not grid or not grid[0]:
            return 0  
        
        count = 0
        row, col = len(grid), len(grid[0])
        
        # Step 2 : DFS function 
        def dfs(i, j):            
            if i<0 or j<0 or i>=row or j>=col or grid[i][j] == '0':
                return 0

            grid[i][j] = '0'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        # Step 3 : Recursive function
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)                    
        return count
