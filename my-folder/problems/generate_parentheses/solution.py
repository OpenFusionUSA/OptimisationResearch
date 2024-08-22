class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output=[]
        curr=[]
        def backtrack(left,right):
            if(left==right==n):
                output.append("".join(curr))
                return
            if left<n:
                curr.append("(")
                backtrack(left+1, right)
                curr.pop()
            if right<left:
                curr.append(")")
                backtrack(left, right+1)
                curr.pop()
        backtrack(0, 0)
        return output