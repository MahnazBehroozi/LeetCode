class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        
        number = 0
        dic_stones = Counter(stones)  # creating a hash map of the number of each stone type
          
        return sum(dic_stones[i] for i in dic_stones and jewels)
