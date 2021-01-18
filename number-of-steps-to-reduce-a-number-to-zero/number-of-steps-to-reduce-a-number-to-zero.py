class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while num>0:
            if num%2==0:
                num = num//2
            else:
                num = num - 1
            steps = steps + 1
        return steps
        
        
        
        
        
        #return self.MyStep(num, 0)
        
    #def MyStep(self, num, steps) -> int: 
     #   if num == 0:
      #      return steps
​
       # elif num%2==0:
        #    steps = steps + 1
         #   print(steps)
          #  self.MyStep(num//2, steps)
       # else:
        #    steps = steps + 1
         #   self.MyStep(num-1, steps)
        
        
