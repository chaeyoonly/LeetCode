class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}        
        for i in range(0, len(nums)):
            if nums[i] in dict.keys():              
                return [dict[nums[i]],i]            
            dict[target - nums[i]] = i
            
        return(0,len(nums)-1)
      
## Hash table
