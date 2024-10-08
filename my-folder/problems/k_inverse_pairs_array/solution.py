class Solution:
    def kInversePairs(self, n, k):
        MOD = 1000000007
        prev = [0]*(k+1)
        prev[0]=1
        for N in range(1,n+1):
            cur=[0]*(k+1)
            total=0
            for K in range(k+1):
                if K>=N:
                    total-=prev[K-N]
                total=(total+prev[K])%MOD
                cur[K]=total
            prev=cur
        return prev[k]