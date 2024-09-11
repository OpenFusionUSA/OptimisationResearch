class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def dfs(i,j):
            if i==n:
                return j
            if j==0 and grid[i][j]==-1:
                return -1
            if j==m-1 and grid[i][j]==1:
                return -1
            if j<m-1 and grid[i][j]==1 and grid[i][j+1]==-1:
                return -1
            if j>0 and grid[i][j]==-1 and grid[i][j-1]==1:
                return -1
            return dfs(i+1, j+1) if grid[i][j]==1 else dfs(i+1, j-1)
        n=len(grid)
        m=len(grid[0])
        return [ dfs(0, j) for j in range(m)]