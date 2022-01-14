class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        move = len(nums)
        i = 0
        while i < move:
            if(nums[i] == 0):
                nums.append(nums[i])
                nums.pop(i)
                move -= 1
            else:
                i += 1
                
# Discuss
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
