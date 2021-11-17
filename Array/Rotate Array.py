class Solution(object):
    def rotate(self, nums, k):
        length = len(nums) - k
        if(len(nums) > 1):
            rotate = nums[length:]
            del nums[length:]
            nums = rotate + nums
