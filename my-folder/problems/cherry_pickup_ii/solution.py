class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[[0]*n for _ in range(n)] for _ in range(m)]
        for row in reversed(range(m)):
            for col1 in range(n):
                for col2 in range(n):
                    result=0
                    result+=grid[row][col1]
                    if col1!=col2:
                        result+=grid[row][col2]
                    if row!=m-1:
                        result+=max(dp[row+1][nc1][nc2] 
                                    for nc1 in [col1,col1+1,col1-1]
                                    for nc2 in [col2,col2+1,col2-1]
                                    if 0<=nc1<n and 0<=nc2<n)
                    dp[row][col1][col2]=result
        return dp[0][0][n-1]
