class Solution:
    def maximum69Number (self, num: int) -> int:
        #dic = {}
        numString = list(str(num))
        for i in range(len(numString)):
            #dic[i] = numString[i]
            if numString[i] == '6':
                numString[i] = '9'
                break
        
        return int("".join(i for i in numString))
