class Solution:
    def isPalindrome(self, x: int) -> bool:
        from collections import deque
        str_Num = str(x)
        front = 0
        end = len(str_Num) - 1
        flag = 1
        while(end-front>0 and flag==1):
            if(str_Num[front]!=str_Num[end]):
                flag = 0
                return False
            front = front + 1
            end = end - 1
            
        return True
                
