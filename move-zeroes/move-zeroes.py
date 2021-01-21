class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index_zero = 0
        index_non_zero = 0
        
        while index_non_zero<len(nums):
            if nums[index_zero] == 0 and nums[index_non_zero]!= 0:
                nums[index_zero] = nums[index_non_zero]
                nums[index_non_zero] = 0
                index_zero = index_zero + 1
                index_non_zero = index_non_zero + 1
            elif nums[index_non_zero]== 0:
                index_non_zero = index_non_zero + 1
            elif nums[index_zero] != 0 and nums[index_non_zero]!= 0:
                index_zero = index_zero + 1
                index_non_zero = index_non_zero + 1
            
        
        #itr = 0
        #ind = 0
        #while itr<len(nums):
            #if(nums[ind] == 0):
                #del nums[ind]
                #nums.append(0)
            #else:
                #ind = ind + 1
            #itr = itr + 1
