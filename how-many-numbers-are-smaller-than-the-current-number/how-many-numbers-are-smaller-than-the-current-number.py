class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        numsTemp = sorted(nums)
        return [numsTemp.index(i) for i in nums]    
