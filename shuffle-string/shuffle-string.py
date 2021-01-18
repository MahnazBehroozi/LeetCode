class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        temp = list(s)
        for i in range(len(temp)):
            temp[indices[i]]=s[i]
        return "".join(temp)
