class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        return str(self.convert(num1)+self.convert(num2))
    
    
    
    def convert(self, num: str) -> int:
        dic= {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,'9':9}
        
        n = 0
        power = len(num)-1
        for i in range(len(num)):
            n = n + dic[num[i]]*(10**power)
            power = power - 1
        return n
    
    #def finalString(self, num: int) -> str:
       # dic= {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 9:'9'}
        
        
        #return result
