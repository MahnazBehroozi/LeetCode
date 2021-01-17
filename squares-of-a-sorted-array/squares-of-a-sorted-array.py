class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        
        nums.sort()  # always keep in mind that after sorting just return the actual list
        return nums
