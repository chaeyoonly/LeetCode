class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        result = False
        while result == False:
            if(nums[i] == target):
                result = True
                return i
            elif(i == len(nums)-1):
                break
            else:
                i += 1
        return -1

    
# Discuss
# Faster than 99.34%
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = int(low + (high - low)/2)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
