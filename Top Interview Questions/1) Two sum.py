class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}        
        for i in range(0, len(nums)):
            if nums[i] in dict.keys():              
                return [dict[nums[i]],i]            
            dict[target - nums[i]] = i
            
        return(0,len(nums)-1)
      
## Hash table interview

# Brute force way : inefficient & has a runtime of n squared
# We can do a lot better than brute force using a concept called complement.
# Complement : the number derived by subtracting a number from a base number. For example, the tens complement of 8 is 2.

# Hash table way : time complexity is O of n which is linear time
