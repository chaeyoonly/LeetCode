# DFS Solution

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Step 1 : Check for an empty graph
        if not grid:
            return 0
        
        max_area = 0
        row, col = len(grid), len(grid[0])
        visited = set()
        
        # Step 2 : DFS function 
        def dfs(i, j):
            if (i, j) in visited:
                return 0
            visited.add((i,j))
            
            if i<0 or j<0 or i>=row or j>=col or grid[i][j] != 1:
                return 0

            max_area = 1
            max_area += dfs(i+1, j)
            max_area += dfs(i-1, j)
            max_area += dfs(i, j+1)
            max_area += dfs(i, j-1)

            return max_area
    
        # Step 3 : Recursive functino
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))                    
        return max_area
    
