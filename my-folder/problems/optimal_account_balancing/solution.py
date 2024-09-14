class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        gr=defaultdict(int)
        for f,t,a in transactions:
            gr[f]-=a
            gr[t]+=a
        acc=[x for x in gr.values() if x]
        n=len(acc)
        f=[inf]*(1<<n)
        f[0]=0
        for i in range(1,1<<n):
            s=0
            for j,x in enumerate(acc):
                if i>>j&1:
                    s+=x
            if s==0:
                f[i]=i.bit_count()-1
                j=(i-1)&i
                while j>0:
                    f[i]=min(f[i],f[j]+f[i^j])
                    j=(j-1)&i
        return f[-1]
