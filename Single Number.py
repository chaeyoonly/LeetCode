class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        length = len(nums)
        result = 0
        nums.sort()
        for i in range(0,length,2):
            if(length == 1 or i == length-1):
                result = nums[i]
                break
            elif(nums[i] != nums[i+1]):
                result = nums[i]
                break
            else:
                continue
        return result
