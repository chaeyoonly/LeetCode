
## Solution (DFS)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image
      
      
      
      
## Discuss (BFS)
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:        
        h, w = len(image), len(image[0])       
        src_color = image[sr][sc]        
        visited = set()        
        traversal_queue = deque( [(sr, sc)] )        
        while traversal_queue:            
            cur_r, cur_c = traversal_queue.popleft()            
            if cur_r < 0 or cur_r >= h or cur_c < 0 or cur_c >= w or (cur_r, cur_c) in visited or image[cur_r][cur_c] != src_color:
                continue           
            # update color
            image[cur_r][cur_c] = newColor           
            # mark current coordinate as visited
            visited.add( (cur_r, cur_c) )            
            # BFS to 4-connected neighbors
            traversal_queue.append( (cur_r-1, cur_c) )
            traversal_queue.append( (cur_r+1, cur_c) )
            traversal_queue.append( (cur_r, cur_c-1) )
            traversal_queue.append( (cur_r, cur_c+1) )        
        return image
