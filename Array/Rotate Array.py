class Solution(object):
    def rotate(self, nums, k):
        length = len(nums)
        if(k >= length):
            k = k % length
        
        length = length - k
        rotate = nums[length:]
        del nums[length:]
        rotate.extend(nums)
        nums[:] = rotate
