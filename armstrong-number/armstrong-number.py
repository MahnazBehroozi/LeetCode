class Solution:
    def isArmstrong(self, N: int) -> bool:
        S = str(N)
        result = 0
        for i in S:
            result = result + int(i)**len(S)
        return result==N
