class Solution:
    def toLowerCase(self, str: str) -> str:
        u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        l = "abcdefghijklmnopqrstuvwxyz"
        
        dic = dict(zip(u,l))
        
        return "".join(dic[i] if i in dic else i for i in str)
