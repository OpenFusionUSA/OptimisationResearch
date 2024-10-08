class Solution:
    def numSquares(self, n: int) -> int:
        sqs=[i**2 for i in range(int(math.sqrt(n))+1)]
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            for square in sqs:
                if i<square:
                    break
                dp[i]=min(dp[i],dp[i-square]+1)
        return dp[-1] 