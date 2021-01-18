class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(i) for i in str(n)]
        prod = 1
        s = 0
        for i in range(len(digits)):
            prod = prod * digits[i]
            s = s + digits[i]
        return prod-s
            
