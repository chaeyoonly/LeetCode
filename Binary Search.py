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
