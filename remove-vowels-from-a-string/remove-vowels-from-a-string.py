class Solution:
    def removeVowels(self, s: str) -> str:
        dic = ['a', 'e', 'i', 'o', 'u']
        for i in s:
                if i in dic:
                    s=s.replace(i,"")
        
        return s        
                
