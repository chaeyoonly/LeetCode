class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        result = False
        if target < nums[0]:
            return 0
        while result == False:
            if(nums[i] == target):
                result = True
                return i
            elif(i == len(nums)-1):
                return i+1;
            elif nums[i] < target and nums[i+1] > target:
                return i+1;
            else:
                i += 1
                
# Discuss
# Faster Solution

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        while low <= high:
            mid = int(low + (high - low)/2)            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
