class MedianFinder:

    def __init__(self):
        self.minq=[]
        self.maxq=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minq, -heapq.heappushpop(self.maxq, -num))
        if len(self.minq)-len(self.maxq)>1:
            heapq.heappush(self.maxq, -heapq.heappop(self.minq))

    def findMedian(self) -> float:
        if len(self.minq)==len(self.maxq):
            return (self.minq[0]-self.maxq[0])/2
        return self.minq[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()