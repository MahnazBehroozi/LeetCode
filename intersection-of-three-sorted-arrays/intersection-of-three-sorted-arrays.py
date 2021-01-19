class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        result = []
        l = min(len(arr1), len(arr2), len(arr3))
        if l==len(arr1):
            L1 = arr1
            L2 = arr2
            L3 = arr3
        elif l==len(arr2):
            L1 = arr2
            L2 = arr1
            L3 = arr3
        else:
            L1 = arr3
            L2 = arr2
            L3 = arr1
        
        for i in range(l):
            if L1[i] in L2 and L1[i] in L3:
                result.append(L1[i])
            
        return result
        
