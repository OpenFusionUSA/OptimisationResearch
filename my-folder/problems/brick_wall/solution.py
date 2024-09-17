class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        mp=defaultdict(int)
        n=len(wall)
        maxsum=0
        for i in range(n):
            start=0
            for brick in wall[i]:
                start+=brick
                mp[start]+=1
            if maxsum==0:
                maxsum=start
        mp.pop(maxsum)
        return n-max(mp.values()) if mp else n

########## [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
########## [[1,3,5,6],[3,4,6],[1,4,6],[2,6],[3,4,6],[1,4,5,6]]
########## 1-> 3, 2-> 1, 3-> 3, 4-> 4, 5-> 2, 6-> 6 , 0-> 6
##########  O(m)-> space complexity , O(mn) -> time complexity 
