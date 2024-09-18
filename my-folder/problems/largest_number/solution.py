class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numString=[str(num) for num in nums]
        numString.sort(key=lambda a:a*10, reverse=True)
        if numString[0]=="0":
            return "0"
        return "".join(numString)