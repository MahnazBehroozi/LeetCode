class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = []
        
        max_candies = max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max_candies:
                out.append(True)
            else:
                out.append(False)
        return out
