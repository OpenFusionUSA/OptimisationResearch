class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        output=1
        first_end=points[0][1]
        for start,end in points:
            if first_end<start:
                output+=1
                first_end=end
        return output