class Solution:
    def rotatedDigits(self, N: int) -> int:
        goodDigits = ['2','5','6','9']
        badDigits = ['3', '4', '7']
        result = 0
        
        for j in range(1,N+1):
            S = str(j)
            flag = 0
            for i in range(len(S)):
                if S[i] in badDigits:
                    flag = 0
                    break
                if S[i] in goodDigits:
                    flag = 1
            if flag:
                result = result + 1
                
        return result
