class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        string = str(n)
        prod = 1
        s = 0
        for i in range(len(string)):
            prod = prod * int(string[i])
            s = s + int(string[i])
        return prod-s
            
