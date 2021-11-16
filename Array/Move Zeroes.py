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
                
